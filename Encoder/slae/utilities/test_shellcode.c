#include <stdio.h>
#include <string.h>

int main(void)
{
    unsigned char code[] = "place shell code here";

    printf("Shellcode length: %d\n", strlen(code));

    void (*s)() = (void *)code;
    s();

    return 0;
}
