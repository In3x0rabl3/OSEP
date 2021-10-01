/**
 * @file main.c
 * @brief The main program.
 * 
 * @author Chen Zhenshuo (chenzs108@outlook.com)
 * @version 1.0
 * @date 2020-01-19
 * @par GitHub
 * https://github.com/czs108
 */

#include "image.h"
#include "import_table.h"
#include "install_shell.h"
#include "section.h"
#include "utility/error_handling.h"
#include "utility/file_access.h"
#include "utility/platform_check.h"

#include <windows.h>

#include <stdio.h>
#include <stdlib.h>


int main(int argc, char* argv[]) {
    int arg_size = 0;
    const LPWSTR* const args = CommandLineToArgvW(GetCommandLineW(), &arg_size);
    if (arg_size < 3) {
        wprintf(L" [!] Usage: PE-Packer <input-file> <output-file>\r\n");
        return EXIT_SUCCESS;
    }

    const WCHAR* const in_file_name = args[1];
    const WCHAR* const out_file_name = args[2];

    bool success = false;
    bool api_error = false;

    FILE_VIEW in_file_view = { 0 };
    PE_IMAGE_INFO image_info = { 0 };
    EXTRA_DATA_VIEW extra_data = { 0 };
    BYTE* new_imp_table = NULL;
    ENCRY_INFO* encry_info = NULL;
    IMAGE_SECTION_HEADER shell_section_header = { 0 };
    HANDLE out_file = INVALID_HANDLE_VALUE;

    HANDLE in_file =
        CreateFile(in_file_name, GENERIC_READ, FILE_SHARE_READ, NULL,
                   OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, NULL);
    if (in_file == INVALID_HANDLE_VALUE) {
        SetLastErrorCode();
        api_error = true;
        goto _Exit;
    }

    if (IsFileSmallerThan2G(in_file) != true) {
        wprintf(L" [!] ERROR: The program can only process files smaller than "
                L"2GB.\r\n");
        goto _Exit;
    }

    if (OpenReadViewOfFile(in_file, &in_file_view) != true) {
        api_error = true;
        goto _Exit;
    }

    if (IsPeFile(in_file_view.base) != true) {
        wprintf(L" [!] ERROR: The input file is not a PE file.\r\n");
        goto _Exit;
    }

    wprintf(L" [*] Load the PE image.\r\n");
    DWORD file_size = GetFileSize(in_file, NULL);
    if (LoadPeImage(in_file_view.base, file_size, &image_info, &extra_data)
        != true) {
        api_error = true;
        goto _Exit;
    }

    if (image_info.is_dll) {
        wprintf(L" [!] ERROR: The program cannot process a DLL file.\r\n");
        goto _Exit;
    }

    if (IsPeMatchPlatform(&image_info) != true) {
        wprintf(L" [!] ERROR: The PE image doesn't match the program "
                L"platform.\r\n");
        goto _Exit;
    }

    wprintf(L" [*] Transform the import table.\r\n");
    const DWORD new_imp_table_size = CalcNewImpTableSize(&image_info);
    new_imp_table = (BYTE*)VirtualAlloc(
        NULL, new_imp_table_size, MEM_RESERVE | MEM_COMMIT, PAGE_READWRITE);
    if (new_imp_table == NULL) {
        SetLastErrorCode();
        api_error = true;
        goto _Exit;
    }

    ZeroMemory(new_imp_table, new_imp_table_size);
    TransformImpTable(&image_info, new_imp_table);
    ClearImpTable(&image_info);

    wprintf(L" [*] Encrypt sections.\r\n");
    const DWORD encry_count = GetEncryptableSectionNumber(&image_info);
    encry_info =
        (ENCRY_INFO*)VirtualAlloc(NULL, encry_count * sizeof(ENCRY_INFO),
                                  MEM_RESERVE | MEM_COMMIT, PAGE_READWRITE);
    if (encry_info == NULL) {
        SetLastErrorCode();
        api_error = true;
        goto _Exit;
    }

    ZeroMemory(encry_info, encry_count * sizeof(ENCRY_INFO));
    EncryptSections(&image_info, encry_info);

    wprintf(L" [*] Clear section names.\r\n");
    ClearSectionNames(&image_info);

    if (CanAppendNewSection(&image_info) != true) {
        wprintf(
            L" [!] ERROR: The PE image has no space for a new section.\r\n");
        goto _Exit;
    }

    wprintf(L" [*] Append a new section for the shell.\r\n");
    const DWORD shell_size = CalcShellSize(new_imp_table_size);
    if (AppendNewSection(&image_info, ".shell", shell_size,
                         &shell_section_header)
        != true) {
        api_error = true;
        goto _Exit;
    }

    wprintf(L" [*] Install the shell.\r\n");
    if (InstallShell(&image_info, new_imp_table, new_imp_table_size, encry_info,
                     encry_count)
        != true) {
        api_error = true;
        goto _Exit;
    }

    wprintf(L" [*] Write the new PE image to the output file.\r\n");
    out_file = CreateFile(out_file_name, GENERIC_WRITE, FILE_SHARE_READ, NULL,
                          CREATE_ALWAYS, FILE_ATTRIBUTE_NORMAL, NULL);
    if (out_file == INVALID_HANDLE_VALUE) {
        SetLastErrorCode();
        api_error = true;
        goto _Exit;
    }

    if (WriteImageToFile(&image_info, out_file) != true) {
        api_error = true;
        goto _Exit;
    }

    wprintf(L" [*] Write the extra data to the output file.\r\n");
    if (WriteExtraDataToFile(&extra_data, out_file) != true) {
        api_error = true;
        goto _Exit;
    }

    wprintf(L" [*] The packing has finished.\r\n");
    success = true;

_Exit:
    if (!success) {
        if (api_error) {
            const DWORD error_code = GetLastErrorCode();
            TCHAR* error_message = FormatErrorMessage(error_code);
            wprintf(L" [!] ERROR: %ls\r\n", error_message);
            FreeErrorMessage(error_message);
            error_message = NULL;
        }

        DeleteFile(out_file_name);
    }

    if (new_imp_table != NULL) {
        VirtualFree(new_imp_table, 0, MEM_RELEASE);
        new_imp_table = NULL;
    }

    if (encry_info != NULL) {
        VirtualFree(encry_info, 0, MEM_RELEASE);
        encry_info = NULL;
    }

    FreePeImage(&image_info);

    CloseViewOfFile(&in_file_view);

    if (in_file != INVALID_HANDLE_VALUE) {
        CloseHandle(in_file);
        in_file = INVALID_HANDLE_VALUE;
    }

    if (out_file != INVALID_HANDLE_VALUE) {
        CloseHandle(out_file);
        out_file = INVALID_HANDLE_VALUE;
    }

    return EXIT_SUCCESS;
}