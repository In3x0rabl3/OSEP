from pwn import *
import encoder

context.arch = 'amd64'
context.bits = 64

def check_r64(r64):
    if r64 not in ['rax', 'rcx', 'rdx', 'rbx', 'rsp', 'rbp', 'rsi', 'rdi', 'r8', 'r9', 'r10', 'r11,' 'r12', 'r13', 'r14', 'r15']:
        raise ValueError("register %s not supported" % (r64,))

def check_o16(o16):
    if o16 > 0xffff or o16 < -0xffff:
        raise ValueError("offset %x out of bounds" % (o16,))

def load_rdx_r64(r64):
    check_r64(r64)
    shellcode = ''
    if r64 != 'rdx':
        shellcode += asm('push %s; pop rdx' % (r64,))
    return shellcode

def load_rdx_i64(i64):
    shellcode  = encoder.zero_rax() # save zero into rbx for next step
    shellcode += encoder.set_rax(i64)
    shellcode += load_rdx_r64('rax')
    return shellcode

def load_rdx_offset(r64, o16):
    check_r64(r64)
    check_o16(o16)
    shellcode  = asm('push %s; push rax' % (r64,)) # save value and allocate space
    shellcode += encoder.zero_rax() # save zero into rbx for next step
    shellcode += asm('pop rax; pop rax') # deallocate space and restore value
    shellcode += encoder.add_ax(o16)
    shellcode += load_rdx_r64('rax')
    return shellcode

def load_rdx_indirect_r64_r64(r64, or64):
    check_r64(r64)
    check_r64(or64)
    if r64 == 'rsp':
        raise ValueError('register offset indirect to rsp not supported')
    shellcode = ''
    shellcode += asm('push %s; push rax' % (r64,)) # save value and allocate space
    shellcode += encoder.zero_rax() # zero rsi
    shellcode += asm('pop rax; pop rax') # deallocate space and restore value
    if r64 != 'rax':
        shellcode += asm('push %s; pop rax;' % (r64,))
    if or64 != 'rdi':
        shellcode += asm('push %s; pop rdi;' % (or64,))
    shellcode += asm('xor rsi, [rax + rdi]')
    shellcode += load_rdx_r64('rsi')
    return shellcode

def load_rdx_indirect_r64_i64(r64, o64):
    check_r64(r64)
    if r64 == 'rsp':
        return load_rdx_indirect_rsp(o64)
    shellcode = ''
    shellcode += asm('push %s; push rax' % (r64,)) # save value and allocate space
    shellcode += encoder.zero_rax() # save zero into rbx for next step. also zeroes rsi
    if o64 != 0:
        shellcode += encoder.set_rax(o64)
    shellcode += asm('push rax; pop rdi')
    shellcode += asm('pop rax; pop rax') # deallocate space and restore value
    shellcode += asm('xor rsi, [rax + rdi]')
    shellcode += load_rdx_r64('rsi')
    return shellcode

def load_rdx_indirect_i64(i64):
    shellcode  = encoder.zero_rax()
    shellcode += encoder.set_rax(i64)
    shellcode += load_rdx_indirect_r64_i64('rax', 0)
    return shellcode

def load_rdx_indirect_rsp(o8): # mov rdx, [rsp+o8] without clobbering
    if o8 % 8 != 0:
        raise ValueError('rsp offset %d is not supported' % (o8,))

    shellcode = ''
    o8 += 16 # we need to make sure that before starting rsp = rsp+o8+16.
    o8 /= 8
    if o8 > 0:
        shellcode += o8 * asm('pop rax') # allocate down to not overwrite target
    else:
        shellcode += o8 * asm('push rax')  # deallocate up to match up to target

    shellcode += asm( # do magic
'''
push rsp /* zero rsi */
pop r9
pop r8
push rsi
xor rsi, [r9]
push rsi
pop rax /* now set rax to 0x10 */
xor eax, 0x20202020
xor eax, 0x20202030
push rsp
pop r9
pop r8
push rax /* r9 now points to rax */
sub sp, [r9] /* decrement sp without overwriting (pushing) */
pop rdx /* ptr to return value (shellcode) now in rdx */
''')
    return shellcode

def load_rdx(expr):
    def parse_operand(operand):
        if operand.startswith('0x'):
            operand = int(operand,16)
        elif operand.isdigit():
            operand = int(operand)
        return operand

    def parse_indirect(indirect):
        if indirect.count('+') != 1:
            raise ValueError('malformed indirect expression %s' % (indirect,))
        base, offset = indirect.split('+')
        offset = parse_operand(offset)
        return base,offset

    if '[' in expr:
        if expr[0] != '[' or expr[-1] != ']':
            raise ValueError('malformed indirect expression %s' % (expr,))
        if expr.count('[') != 1 or expr.count(']') != 1:
            raise ValueError('multiple indirects are not supported')
        indirect = expr[1:-1]
        offset = 0
        if '+' in indirect:
            base,offset = parse_indirect(indirect)
            if isinstance(offset, (int,long)):
                return load_rdx_indirect_r64_i64(base, offset)
            else:
                return load_rdx_indirect_r64_r64(base, offset)
        else:
            indirect = parse_operand(indirect)
            if isinstance(indirect, (int,long)):
                return load_rdx_indirect_i64(indirect)
            else:
                return load_rdx_indirect_r64_i64(indirect, 0)
    else:
        if '+' in expr:
            base, offset = parse_indirect(expr)
            if isinstance(offset, (int,long)):
                return load_rdx_offset(base, offset)
            else:
                raise ValueError('sorry, loading shellcode pointer as reg+reg is not supported')
        else:
            operand = parse_operand(expr)
            if isinstance(operand, (int,long)):
                return load_rdx_i64(operand)
            else:
                return load_rdx_r64(operand)
