/**
 * @file file_access.h
 * @brief File reading and writing.
 * 
 * @author Chen Zhenshuo (chenzs108@outlook.com)
 * @version 1.0
 * @date 2020-01-10
 * @par GitHub
 * https://github.com/czs108
 */

#pragma once

#include <windows.h>

#include <stdbool.h>

/**
 * @brief The view of a file.
 */
typedef struct _FILE_VIEW {
    //! The file-mapping returned by @em CreateFileMapping API.
    HANDLE map;

    //! The base address of the file content returned by @em MapViewOfFile API.
    const BYTE* base;

    //! The size of the file.
    DWORD size;

} FILE_VIEW;


/**
 * @brief Write all data to a file.
 * 
 * @param file  The file.
 * @param data  The base address of the data.
 * @param size  The size of the data.
 * @return @em true if the method succeeds, otherwise @em false.
 */
bool WriteAllToFile(const HANDLE file, const BYTE* const data,
                    const DWORD size);


/**
 * @brief Open a read-only view for a file.
 * 
 * @param file              The file.
 * @param[out] file_view    The read-only view.
 * @return @em true if the method succeeds, otherwise @em false.
 * 
 * @note The constructor of @em _FILE_VIEW structure.
 */
bool OpenReadViewOfFile(const HANDLE file, FILE_VIEW* const file_view);


/**
 * @brief Close the view of a file.
 * 
 * @param file_view The view.
 * 
 * @note The destructor of @em _FILE_VIEW structure.
 */
void CloseViewOfFile(const FILE_VIEW* const file_view);


/**
 * @brief Check if the size of a file is smaller than 2GB.
 * 
 * @param file  The file.
 * @return @em true if the size of the file is smaller than 2GB, otherwise @em false.
 * 
 * @warning The program can only process files smaller than 2GB.
 */
bool IsFileSmallerThan2G(const HANDLE file);