/**
 * @file import_table.c
 * @brief Transform the import table.
 * 
 * @author Chen Zhenshuo (chenzs108@outlook.com)
 * @version 1.0
 * @date 2020-01-10
 * @par GitHub
 * https://github.com/czs108
 */

#include "import_table.h"

#include <assert.h>
#include <string.h>

/**
 * @brief A callback method, called when enumerating the import table.
 * 
 * @param image_info    The PE image.
 * @param descriptor    The @em IMAGE_IMPORT_DESCRIPTOR structure.
 * @param arg           An optional custom argument.
 * @return An optional custom value.
 * 
 * @see EnumImpTable()
 */
typedef DWORD (*LPFN_ENUM_IMP_CALLBACK)(
    const PE_IMAGE_INFO* const image_info,
    IMAGE_IMPORT_DESCRIPTOR* const descriptor, void* const arg);


/******************************************************************************/
// Callback methods
/******************************************************************************/

/**
 * @brief
 * A @em ::LPFN_ENUM_IMP_CALLBACK method,
 * used to calculate the size required for the import table of the new format.
 * 
 * @param image_info    The PE image.
 * @param descriptor    The @em IMAGE_IMPORT_DESCRIPTOR structure.
 * @param[in, out] size The required size.
 * @return Useless.
 */
static DWORD CalcSizeCallBack(const PE_IMAGE_INFO* const image_info,
                              IMAGE_IMPORT_DESCRIPTOR* const descriptor,
                              void* const size);


/**
 * @brief
 * A @em ::LPFN_ENUM_IMP_CALLBACK method,
 * used to clear the original import table.
 * 
 * @param image_info    The PE image.
 * @param descriptor    The @em IMAGE_IMPORT_DESCRIPTOR structure.
 * @param arg           Useless.
 * @return Useless.
 */
static DWORD ClearCallBack(const PE_IMAGE_INFO* const image_info,
                           IMAGE_IMPORT_DESCRIPTOR* const descriptor,
                           void* const arg);


/**
 * @brief
 * A @em ::LPFN_ENUM_IMP_CALLBACK method,
 * used to transform the import table into the new format.
 * 
 * @param image_info            The PE image.
 * @param descriptor            The @em IMAGE_IMPORT_DESCRIPTOR structure.
 * @param[in, out] new_table    The space where the new table will be constructed.
 * @return Useless.
 */
static DWORD TransformCallBack(const PE_IMAGE_INFO* const image_info,
                               IMAGE_IMPORT_DESCRIPTOR* const descriptor,
                               void* const new_table);

/******************************************************************************/

/**
 * @brief Enumerate the import table.
 * 
 * @param image_info    The PE image.
 * @param callback
 * A @em ::LPFN_ENUM_IMP_CALLBACK method,
 * it will be called on each @em IMAGE_IMPORT_DESCRIPTOR structure.
 * @param arg           An optional custom argument, it will be passed to @em callback.
 */
static void EnumImpTable(const PE_IMAGE_INFO* const image_info,
                         const LPFN_ENUM_IMP_CALLBACK callback,
                         void* const arg);


DWORD CalcNewImpTableSize(const PE_IMAGE_INFO* const image_info) {
    assert(image_info != NULL);

    DWORD size = 0;
    EnumImpTable(image_info, &CalcSizeCallBack, &size);
    return size;
}


DWORD TransformImpTable(const PE_IMAGE_INFO* const image_info,
                        BYTE* const new_table) {
    assert(image_info != NULL);

    const DWORD new_size = CalcNewImpTableSize(image_info);
    if (new_table != NULL) {
        EnumImpTable(image_info, &TransformCallBack, (void*)&new_table);
    }

    return new_size;
}


void ClearImpTable(const PE_IMAGE_INFO* const image_info) {
    assert(image_info != NULL);

    // Clear the import table.
    EnumImpTable(image_info, &ClearCallBack, NULL);

    /* Clear the `DataDirectory`. */

    // Get the base address of the `DataDirectory` array.
    IMAGE_DATA_DIRECTORY* const dirs =
        image_info->nt_header->OptionalHeader.DataDirectory;

    // Clear the `DataDirectory` of the bound import table.
    IMAGE_DATA_DIRECTORY* const bound_dir =
        &dirs[IMAGE_DIRECTORY_ENTRY_BOUND_IMPORT];
    if (bound_dir->VirtualAddress != 0 && bound_dir->Size > 0) {
        void* const data = RvaToVa(image_info, bound_dir->VirtualAddress);
        ZeroMemory(data, bound_dir->Size);
    }

    ZeroMemory(bound_dir, sizeof(IMAGE_DATA_DIRECTORY));

    // Clear the `DataDirectory` of the import address table (IAT).
    IMAGE_DATA_DIRECTORY* const iat_dir = &dirs[IMAGE_DIRECTORY_ENTRY_IAT];
    if (iat_dir->VirtualAddress != 0 && iat_dir->Size > 0) {
        void* const data = RvaToVa(image_info, iat_dir->VirtualAddress);
        ZeroMemory(data, iat_dir->Size);
    }

    ZeroMemory(iat_dir, sizeof(IMAGE_DATA_DIRECTORY));

    // Clear the `DataDirectory` of the delay import table.
    IMAGE_DATA_DIRECTORY* const delay_dir =
        &dirs[IMAGE_DIRECTORY_ENTRY_DELAY_IMPORT];
    ZeroMemory(delay_dir, sizeof(IMAGE_DATA_DIRECTORY));
}


void EnumImpTable(const PE_IMAGE_INFO* const image_info,
                  const LPFN_ENUM_IMP_CALLBACK callback, void* const arg) {
    assert(image_info != NULL);
    assert(callback != NULL);

    const IMAGE_DATA_DIRECTORY* const imp_dir =
        &image_info->nt_header->OptionalHeader
             .DataDirectory[IMAGE_DIRECTORY_ENTRY_IMPORT];
    if (imp_dir->VirtualAddress != 0 && imp_dir->Size > 0) {
        IMAGE_IMPORT_DESCRIPTOR* descriptor = (IMAGE_IMPORT_DESCRIPTOR*)RvaToVa(
            image_info, imp_dir->VirtualAddress);
        for (; descriptor->Name != 0; ++descriptor) {
            callback(image_info, descriptor, arg);
        }
    }
}


DWORD CalcSizeCallBack(const PE_IMAGE_INFO* const image_info,
                       IMAGE_IMPORT_DESCRIPTOR* const descriptor,
                       void* const size) {
    assert(image_info != NULL);
    assert(descriptor != NULL);
    assert(size != NULL);

    // Get the accumulative size.
    DWORD curr_size = *(DWORD*)size;

    // The `FirstThunk` structure.
    curr_size += sizeof(IMAGE_THUNK_DATA);

    // The size of the DLL name, including the '\0'.
    curr_size += sizeof(BYTE);

    // The DLL name.
    const CHAR* const dll_name = RvaToVa(image_info, descriptor->Name);
    curr_size += (strlen(dll_name) + 1) * sizeof(CHAR);

    // The number of functions.
    curr_size += sizeof(DWORD);

    // Get the import name table (INT) or import address table (IAT).
    const IMAGE_THUNK_DATA* thunk = NULL;
    if (descriptor->OriginalFirstThunk != 0) {
        thunk = (IMAGE_THUNK_DATA*)RvaToVa(image_info,
                                           descriptor->OriginalFirstThunk);
    } else {
        thunk = (IMAGE_THUNK_DATA*)RvaToVa(image_info, descriptor->FirstThunk);
    }

    for (; thunk->u1.AddressOfData != 0; ++thunk) {
        // The size of the function name, including the '\0'.
        // Or the flag 0x00.
        curr_size += sizeof(BYTE);

        if (IMAGE_SNAP_BY_ORDINAL(thunk->u1.Ordinal)) {
            // The function order.
            curr_size += sizeof(VOID*);
        } else {
            // The function name.
            const IMAGE_IMPORT_BY_NAME* const func_name =
                (IMAGE_IMPORT_BY_NAME*)RvaToVa(image_info,
                                               thunk->u1.AddressOfData);
            curr_size += (strlen((CHAR*)func_name->Name) + 1) * sizeof(CHAR);
        }
    }

    // Update the accumulative size.
    *(DWORD*)size = curr_size;
    return 0;
}


DWORD ClearCallBack(const PE_IMAGE_INFO* const image_info,
                    IMAGE_IMPORT_DESCRIPTOR* const descriptor,
                    void* const arg) {
    assert(image_info != NULL);
    assert(descriptor != NULL);

    // Clear the DLL name.
    CHAR* const dll_name = RvaToVa(image_info, descriptor->Name);
    ZeroMemory(dll_name, strlen(dll_name) * sizeof(CHAR));

    // Clear the import name table (INT).
    if (descriptor->OriginalFirstThunk != 0) {
        for (IMAGE_THUNK_DATA* thunk = (IMAGE_THUNK_DATA*)RvaToVa(
                 image_info, descriptor->OriginalFirstThunk);
             thunk->u1.AddressOfData != 0; ++thunk) {
            if (!IMAGE_SNAP_BY_ORDINAL(thunk->u1.Ordinal)) {
                // Clear the function name.
                IMAGE_IMPORT_BY_NAME* const func_name =
                    (IMAGE_IMPORT_BY_NAME*)RvaToVa(image_info,
                                                   thunk->u1.AddressOfData);
                ZeroMemory(func_name,
                           sizeof(WORD)
                               + strlen((CHAR*)func_name->Name) * sizeof(CHAR));
            }

            ZeroMemory(thunk, sizeof(IMAGE_THUNK_DATA));
        }
    }

    // Clear the import address table (IAT).
    for (IMAGE_THUNK_DATA* thunk =
             (IMAGE_THUNK_DATA*)RvaToVa(image_info, descriptor->FirstThunk);
         thunk->u1.AddressOfData != 0; ++thunk) {
        ZeroMemory(thunk, sizeof(IMAGE_THUNK_DATA));
    }

    // Clear the `IMAGE_IMPORT_DESCRIPTOR` structure.
    ZeroMemory(descriptor, sizeof(IMAGE_IMPORT_DESCRIPTOR));

    return 0;
}


DWORD TransformCallBack(const PE_IMAGE_INFO* const image_info,
                        IMAGE_IMPORT_DESCRIPTOR* const descriptor,
                        void* const new_table) {
    assert(image_info != NULL);
    assert(descriptor != NULL);
    assert(new_table != NULL);

    // Get the current address of the new table.
    BYTE* buffer = *(BYTE**)new_table;

    // Save the `FirstThunk` structure.
    CopyMemory(buffer, &descriptor->FirstThunk, sizeof(IMAGE_THUNK_DATA));
    buffer += sizeof(IMAGE_THUNK_DATA);

    // Save the size of the DLL name, including the '\0'.
    const CHAR* const dll_name = RvaToVa(image_info, descriptor->Name);
    const BYTE dll_name_size = (strlen(dll_name) + 1) * sizeof(CHAR);
    *buffer = dll_name_size;
    buffer += sizeof(BYTE);

    // Save the DLL name.
    CopyMemory(buffer, dll_name, dll_name_size);
    buffer += dll_name_size;

    // Get the location where the number of functions being saved.
    DWORD* const func_num = (DWORD*)buffer;
    *func_num = 0;
    buffer += sizeof(DWORD);

    // Get the import name table (INT) or import address table (IAT).
    const IMAGE_THUNK_DATA* thunk = NULL;
    if (descriptor->OriginalFirstThunk != 0) {
        thunk = (IMAGE_THUNK_DATA*)RvaToVa(image_info,
                                           descriptor->OriginalFirstThunk);
    } else {
        thunk = (IMAGE_THUNK_DATA*)RvaToVa(image_info, descriptor->FirstThunk);
    }

    for (; thunk->u1.AddressOfData != 0; ++thunk) {
        if (IMAGE_SNAP_BY_ORDINAL(thunk->u1.Ordinal)) {
            // Save the flag 0x00.
            *buffer = 0;
            buffer += sizeof(BYTE);

            // Save the function order.
            *(VOID**)buffer = (VOID*)IMAGE_ORDINAL(thunk->u1.Ordinal);
            buffer += sizeof(VOID*);
        } else {
            // Save the size of the function name, including the '\0'.
            const IMAGE_IMPORT_BY_NAME* const func_name =
                (IMAGE_IMPORT_BY_NAME*)RvaToVa(image_info,
                                               thunk->u1.AddressOfData);
            const BYTE func_name_size =
                (strlen(func_name->Name) + 1) * sizeof(CHAR);
            *buffer = func_name_size;
            buffer += sizeof(BYTE);

            // Save the function name.
            CopyMemory(buffer, func_name->Name, func_name_size);
            buffer += func_name_size;
        }

        // Update the number of functions.
        ++*func_num;
    }

    // Update the current address.
    *(BYTE**)new_table = buffer;
    return 0;
}