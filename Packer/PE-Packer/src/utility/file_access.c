/**
 * @file file_access.c
 * @brief File reading and writing.
 * 
 * @author Chen Zhenshuo (chenzs108@outlook.com)
 * @version 1.0
 * @date 2020-01-10
 * @par GitHub
 * https://github.com/czs108
 */

#include "file_access.h"
#include "error_handling.h"

#include <assert.h>


bool WriteAllToFile(const HANDLE file, const BYTE* const data,
                    const DWORD size) {
    assert(file != INVALID_HANDLE_VALUE);

    if (size == 0) {
        return true;
    }

    assert(data != NULL);

    DWORD remaining = size;
    const BYTE* current = data;
    while (remaining > 0) {
        DWORD written = 0;
        if (WriteFile(file, current, remaining, &written, NULL) == FALSE) {
            SetLastErrorCode();
            return false;
        }

        remaining -= written;
        current += written;
    }

    return true;
}


bool OpenReadViewOfFile(const HANDLE file, FILE_VIEW* const file_view) {
    assert(IsFileSmallerThan2G(file));
    assert(file_view != NULL);

    bool success = false;
    ZeroMemory(file_view, sizeof(file_view));

    file_view->size = GetFileSize(file, NULL);
    file_view->map = CreateFileMapping(file, NULL, PAGE_READONLY, 0, 0, NULL);
    if (file_view->map == NULL) {
        SetLastErrorCode();
        goto _Exit;
    }

    file_view->base =
        (BYTE*)MapViewOfFile(file_view->map, FILE_MAP_READ, 0, 0, 0);
    if (file_view->base == NULL) {
        SetLastErrorCode();
        goto _Exit;
    }

    success = true;

_Exit:
    if (!success) {
        CloseViewOfFile(file_view);
        ZeroMemory(file_view, sizeof(file_view));
    }

    return success;
}


void CloseViewOfFile(const FILE_VIEW* const file_view) {
    assert(file_view != NULL);

    if (file_view->base != NULL) {
        UnmapViewOfFile(file_view->base);
    }

    if (file_view->map != NULL) {
        CloseHandle(file_view->map);
    }
}


bool IsFileSmallerThan2G(const HANDLE file) {
    assert(file != INVALID_HANDLE_VALUE);

    DWORD size_low = GetFileSize(file, NULL);
    return !(size_low & 0x80000000);
}