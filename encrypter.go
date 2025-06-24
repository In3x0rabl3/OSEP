package main

import (
	"crypto/rc4"
	"encoding/hex"
	"fmt"
	"io/ioutil"
	"os"
)

func main() {
	if len(os.Args) < 4 {
		fmt.Println("Usage: rc4_encryptor <input_shellcode.bin> <hex_key> <output_encrypted.bin>")
		return
	}

	inputPath := os.Args[1]
	keyHex := os.Args[2]
	outputPath := os.Args[3]

	key, err := hex.DecodeString(keyHex)
	if err != nil {
		fmt.Printf("[-] Invalid hex key: %v\n", err)
		return
	}

	shellcode, err := ioutil.ReadFile(inputPath)
	if err != nil {
		fmt.Printf("[-] Failed to read input file: %v\n", err)
		return
	}

	cipher, err := rc4.NewCipher(key)
	if err != nil {
		fmt.Printf("[-] Failed to initialize RC4 cipher: %v\n", err)
		return
	}

	encrypted := make([]byte, len(shellcode))
	cipher.XORKeyStream(encrypted, shellcode)

	err = ioutil.WriteFile(outputPath, encrypted, 0644)
	if err != nil {
		fmt.Printf("[-] Failed to write encrypted output: %v\n", err)
		return
	}

	fmt.Printf("[+] Encrypted shellcode written to: %s\n", outputPath)
}
