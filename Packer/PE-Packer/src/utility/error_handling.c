/**
 * @file error_handling.c
 * @brief Error handling.
 * 
 * @author Chen Zhenshuo (chenzs108@outlook.com)
 * @version 1.0
 * @date 2020-01-09
 * @par GitHub
 * https://github.com/czs108
 * 
 * @see https://docs.microsoft.com/en-us/windows/win32/debug/system-error-codes
 */

#include "error_handling.h"

static DWORD last_error_code = ERROR_SUCCESS;


DWORD GetLastErrorCode() {
    return last_error_code;
}


void SetLastErrorCode() {
    last_error_code = GetLastError();
}


void ResetLastErrorCode() {
    last_error_code = ERROR_SUCCESS;
}


TCHAR* FormatErrorMessage(const DWORD error_code) {
    TCHAR* const message = NULL;
    FormatMessage(FORMAT_MESSAGE_ALLOCATE_BUFFER | FORMAT_MESSAGE_FROM_SYSTEM
                      | FORMAT_MESSAGE_IGNORE_INSERTS,
                  NULL, error_code,
                  MAKELANGID(LANG_ENGLISH, SUBLANG_ENGLISH_US),
                  (LPTSTR)&message, 0, NULL);
    return message;
}


void FreeErrorMessage(TCHAR* const message) {
    if (message != NULL) {
        LocalFree(message);
    }
}