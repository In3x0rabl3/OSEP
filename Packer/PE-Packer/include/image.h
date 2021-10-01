/**
 * @file image.h
 * @brief Basic PE image methods.
 * 
 * @author Chen Zhenshuo (chenzs108@outlook.com)
 * @version 1.0
 * @date 2020-01-07
 * @par GitHub
 * https://github.com/czs108
 */

#pragma once

#include "extra_data.h"

#include <windows.h>

#include <stdbool.h>

/**
 * @brief Store PE image information, most methods are based on this structure.
 * 
 * @see https://docs.microsoft.com/en-us/windows/win32/debug/pe-format
 */
typedef struct _PE_IMAGE_INFO {
    //! The size of the PE image.
    DWORD image_size;

    //! The base address of the PE image when it is loaded in memory.
    BYTE* image_base;

    //! The base address of the @em IMAGE_NT_HEADERS structure.
    IMAGE_NT_HEADERS* nt_header;

    //! The base address of the first @em IMAGE_SECTION_HEADER structure.
    IMAGE_SECTION_HEADER* section_header;

    //! The thread-local storage table.
    IMAGE_TLS_DIRECTORY tls_table;

    //! If the image is a DLL.
    bool is_dll;

} PE_IMAGE_INFO;


/**
 * @brief Load a PE file to memory.
 * 
 * @param file_base         The base address of the file content.
 * @param file_size         The size of the file.
 * @param[out] image_info   The PE image related to the file.
 * @param[out] extra_data   The extra data behind the PE image.
 * @return @em true if the method succeeded, otherwise @em false.
 * 
 * @note The constructor of @em _PE_IMAGE_INFO structure.
 * @note The constructor of @em _EXTRA_DATA_VIEW structure.
 */
bool LoadPeImage(const BYTE* const file_base, const DWORD file_size,
                 PE_IMAGE_INFO* const image_info,
                 EXTRA_DATA_VIEW* const extra_data);


/**
 * @brief Free the memory of a PE image.
 * 
 * @param image_info    The PE image.
 * 
 * @note The destructor of @em _PE_IMAGE_INFO structure.
 */
void FreePeImage(const PE_IMAGE_INFO* const image_info);


/**
 * @brief Write a PE image to a new file.
 * 
 * @param image_info    The PE image.
 * @param file          The file.
 * @return @em true if the method succeeded, otherwise @em false.
 */
bool WriteImageToFile(const PE_IMAGE_INFO* const image_info, const HANDLE file);


/**
 * @brief Convert a relative virtual address to a virtual address.
 * 
 * @param image_info    The PE image.
 * @param rva           A relative virtual address.
 * @return The virtual address.
 */
BYTE* RvaToVa(const PE_IMAGE_INFO* const image_info, const DWORD rva);


/**
 * @brief Check whether a PE image is x64 or x86.
 * 
 * @param image_info    The PE image.
 * @return @em true if the image is a x64 file, otherwise @em false.
 */
bool IsPe64(const PE_IMAGE_INFO* const image_info);


/**
 * @brief Align a value according to the alignment.
 * 
 * @param value     A value to be aligned.
 * @param align     A value of alignment.
 * @return The value after alignment.
 */
DWORD Align(const DWORD value, const DWORD align);


/**
 * @brief Check if a file is a PE file.
 * 
 * @param file_base The base address of the file content.
 * @return @em true if the file is a PE file, otherwise @em false.
 */
bool IsPeFile(const BYTE* const file_base);


/**
 * @brief
 * Calculate the size of PE headers,
 * including @em IMAGE_DOS_HEADER, @em IMAGE_NT_HEADERS and all @em IMAGE_SECTION_HEADER structures.
 * 
 * @param file_base             The base address of the file content.
 * @param[out] dos_header_size  The size of the @em IMAGE_DOS_HEADER structure. It's optional.
 * @param[out] nt_header_size   The size of the @em IMAGE_NT_HEADERS structure. It's optional.
 * @return The size of PE headers.
 */
DWORD CalcHeadersSize(const BYTE* const file_base, DWORD* const dos_header_size,
                      DWORD* const nt_header_size);