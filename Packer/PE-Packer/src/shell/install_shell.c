/**
 * @file install_shell.c
 * @brief Install the shell.
 * 
 * @author Chen Zhenshuo (chenzs108@outlook.com)
 * @version 1.0
 * @date 2020-01-15
 * @par GitHub
 * https://github.com/czs108
 */

#include "install_shell.h"
#include "../utility/encrypt.h"
#include "../utility/error_handling.h"
#include "entry_export.h"

#include <assert.h>

/**
 * @brief Get the information about the import table of the shell.
 * 
 * @param[out] offset   The offset, relative to the shell. It's optional.
 * @param[out] size     The size. It's optional.
 * @return The beginning of the segment template.
 */
static BYTE* GetShellImpTable(DWORD* const offset, DWORD* const size);


/**
 * @brief Adjust the import table of the shell.
 * 
 * @param shell_base    The base address of the shell.
 * @param shell_section
 * The @em IMAGE_SECTION_HEADER structure of the section where the shell is installed.
 */
static void AdjustShellImpTable(
    BYTE* const shell_base, const IMAGE_SECTION_HEADER* const shell_section);


/**
 * @brief Get the information about the boot segment.
 * 
 * @param[out] offset   The offset, relative to the shell. It's optional.
 * @param[out] size     The size. It's optional.
 * @return The beginning of the segment template.
 */
static BYTE* GetBootSegment(DWORD* const offset, DWORD* const size);


/**
 * @brief Get the information about the load segment.
 * 
 * @param[out] offset   The offset, relative to the shell. It's optional.
 * @param[out] size     The size. It's optional.
 * @return The beginning of the segment template.
 */
static BYTE* GetLoadSegment(DWORD* const offset, DWORD* const size);


/**
 * @brief Get the encryption information of the load segment.
 * 
 * @param shell_base    The base address of the shell.
 * @return The encryption information.
 */
static SEG_ENCRY_INFO* GetLoadSegmentEncryInfo(const BYTE* const shell_base);


/**
 * @brief Get the original PE information.
 * 
 * @param shell_base    The base address of the shell.
 * @return The original PE information.
 */
static ORIGIN_PE_INFO* GetOriginPeInfo(const BYTE* const shell_base);


/**
 * @brief Get the thread-local storage table in the shell.
 * 
 * @param shell_base    The base address of the shell.
 * @param[out] offset   The offset, relative to the shell. It's optional.
 * @return The thread-local storage table.
 */
static IMAGE_TLS_DIRECTORY* GetShellTlsTable(const BYTE* const shell_base,
                                             DWORD* const offset);


bool InstallShell(const PE_IMAGE_INFO* const image_info,
                  const BYTE* const new_imp_table,
                  const DWORD new_imp_table_size,
                  const ENCRY_INFO* const encry_info, const DWORD encry_count) {
    assert(image_info != NULL);
    assert(new_imp_table != NULL);
    assert(encry_info != NULL);

    IMAGE_NT_HEADERS* const nt_header = image_info->nt_header;
    const WORD section_num = nt_header->FileHeader.NumberOfSections;
    IMAGE_SECTION_HEADER* const shell_section_header =
        &image_info->section_header[section_num - 1];

    // Calculate the size of the entire shell.
    const DWORD shell_size = CalcShellSize(new_imp_table_size);
    BYTE* const shell_base = (BYTE*)VirtualAlloc(
        NULL, shell_size, MEM_RESERVE | MEM_COMMIT, PAGE_READWRITE);
    if (shell_base == NULL) {
        SetLastErrorCode();
        return false;
    }

    // Copy the boot segment.
    DWORD boot_seg_size = 0;
    DWORD boot_seg_offset = 0;
    const BYTE* const boot_seg_begin =
        GetBootSegment(&boot_seg_offset, &boot_seg_size);
    BYTE* const boot_seg_base = shell_base + boot_seg_offset;
    CopyMemory(boot_seg_base, boot_seg_begin, boot_seg_size);

    // Copy the load segment.
    DWORD load_seg_size = 0;
    DWORD load_seg_offset = 0;
    const BYTE* const load_seg_begin =
        GetLoadSegment(&load_seg_offset, &load_seg_size);
    BYTE* const load_seg_base = shell_base + load_seg_offset;
    CopyMemory(load_seg_base, load_seg_begin, load_seg_size);

    // Copy the transformed import table.
    CopyMemory(load_seg_base + load_seg_size, new_imp_table,
               new_imp_table_size);

    // Set the values of the fields used by the shell.
    ORIGIN_PE_INFO* const pe_info = GetOriginPeInfo(shell_base);
    ZeroMemory(pe_info, sizeof(ORIGIN_PE_INFO));
    pe_info->entry_point = nt_header->OptionalHeader.AddressOfEntryPoint;
    pe_info->imp_table_offset = load_seg_size;
    pe_info->reloc_table_rva =
        nt_header->OptionalHeader.DataDirectory[IMAGE_DIRECTORY_ENTRY_BASERELOC]
            .VirtualAddress;
    pe_info->image_base = (void*)nt_header->OptionalHeader.ImageBase;

    // Copy the thread-local storage table.
    IMAGE_DATA_DIRECTORY* const tls_dir =
        &nt_header->OptionalHeader.DataDirectory[IMAGE_DIRECTORY_ENTRY_TLS];
    if (tls_dir->VirtualAddress != 0 && tls_dir->Size > 0) {
        DWORD offset = 0;
        IMAGE_TLS_DIRECTORY* const table =
            GetShellTlsTable(shell_base, &offset);
        CopyMemory(table, &image_info->tls_table, sizeof(IMAGE_TLS_DIRECTORY));

        tls_dir->VirtualAddress = shell_section_header->VirtualAddress + offset;
        tls_dir->Size = sizeof(IMAGE_TLS_DIRECTORY);
    }

    // Copy the encryption information of sections.
    assert(encry_count <= MAX_ENCRY_SECTION_COUNT);

    CopyMemory(pe_info->section_encry_info, encry_info,
               encry_count * sizeof(ENCRY_INFO));
    ZeroMemory(pe_info->section_encry_info + encry_count, sizeof(ENCRY_INFO));

    // Encrypt the load segment and transformed import table.
    EncryptData(load_seg_base, load_seg_size + new_imp_table_size);

    // Save the encryption information of the segment and import table.
    SEG_ENCRY_INFO* const seg_encry_info = GetLoadSegmentEncryInfo(shell_base);
    seg_encry_info->seg_offset = load_seg_offset;
    seg_encry_info->seg_size = load_seg_size + new_imp_table_size;

    // Adjust the import table of the shell.
    AdjustShellImpTable(shell_base, shell_section_header);

    // Install the shell to the section.
    CopyMemory(image_info->image_base + shell_section_header->VirtualAddress,
               shell_base, shell_size);

    const DWORD file_align = nt_header->OptionalHeader.FileAlignment;
    const DWORD section_align = nt_header->OptionalHeader.SectionAlignment;

    shell_section_header->SizeOfRawData = Align(shell_size, file_align);
    shell_section_header->Misc.VirtualSize = Align(shell_size, section_align);

    // Change the entry point to the shell.
    nt_header->OptionalHeader.AddressOfEntryPoint =
        shell_section_header->VirtualAddress;
    nt_header->OptionalHeader.CheckSum = 0;

    // Change the import table directory to the shell.
    DWORD imp_table_offset = 0;
    DWORD imp_table_size = 0;
    GetShellImpTable(&imp_table_offset, &imp_table_size);
    nt_header->OptionalHeader.DataDirectory[IMAGE_DIRECTORY_ENTRY_IMPORT]
        .VirtualAddress =
        shell_section_header->VirtualAddress + imp_table_offset;
    nt_header->OptionalHeader.DataDirectory[IMAGE_DIRECTORY_ENTRY_IMPORT].Size =
        imp_table_size;

    ZeroMemory(
        &nt_header->OptionalHeader.DataDirectory[IMAGE_DIRECTORY_ENTRY_DEBUG],
        sizeof(IMAGE_DATA_DIRECTORY));
    ZeroMemory(&nt_header->OptionalHeader
                    .DataDirectory[IMAGE_DIRECTORY_ENTRY_LOAD_CONFIG],
               sizeof(IMAGE_DATA_DIRECTORY));
    ZeroMemory(&nt_header->OptionalHeader
                    .DataDirectory[IMAGE_DIRECTORY_ENTRY_ARCHITECTURE],
               sizeof(IMAGE_DATA_DIRECTORY));
    ZeroMemory(&nt_header->OptionalHeader
                    .DataDirectory[IMAGE_DIRECTORY_ENTRY_BASERELOC],
               sizeof(IMAGE_DATA_DIRECTORY));

    return true;
}


DWORD CalcShellSize(const DWORD new_imp_table_size) {
    DWORD boot_seg_size = 0;
    DWORD load_seg_size = 0;
    GetBootSegment(NULL, &boot_seg_size);
    GetLoadSegment(NULL, &load_seg_size);
    return boot_seg_size + load_seg_size + new_imp_table_size;
}


BYTE* GetShellImpTable(DWORD* const offset, DWORD* const size) {
    if (size != NULL) {
        *size = (BYTE*)&imp_table_end_lbl - (BYTE*)&imp_table_begin_lbl;
    }

    if (offset != NULL) {
        DWORD boot_seg_offset = 0;
        GetBootSegment(&boot_seg_offset, NULL);
        *offset = boot_seg_offset
                  + ((BYTE*)&imp_table_begin_lbl - (BYTE*)&boot_seg_begin_lbl);
    }

    return (BYTE*)&imp_table_begin_lbl;
}


void AdjustShellImpTable(BYTE* const shell_base,
                         const IMAGE_SECTION_HEADER* const shell_section) {
    assert(shell_base != NULL);
    assert(shell_section != NULL);

    DWORD imp_offset = 0;
    GetShellImpTable(&imp_offset, NULL);

    const DWORD imp_rva_base = shell_section->VirtualAddress + imp_offset;
    for (IMAGE_IMPORT_DESCRIPTOR* descriptor =
             (IMAGE_IMPORT_DESCRIPTOR*)(shell_base + imp_offset);
         descriptor->Name != 0; ++descriptor) {
        if (descriptor->OriginalFirstThunk != 0) {
            descriptor->OriginalFirstThunk += imp_rva_base;
        }

        descriptor->Name += imp_rva_base;

        IMAGE_THUNK_DATA* thunk = (IMAGE_THUNK_DATA*)(shell_base + imp_offset
                                                      + descriptor->FirstThunk);

        descriptor->FirstThunk += imp_rva_base;

        for (; thunk->u1.AddressOfData != 0; ++thunk) {
            thunk->u1.AddressOfData += imp_rva_base;
        }
    }
}


SEG_ENCRY_INFO* GetLoadSegmentEncryInfo(const BYTE* const shell_base) {
    assert(shell_base != NULL);

    // Relocation.
    DWORD seg_offset = 0;
    const BYTE* const seg_begin = GetBootSegment(&seg_offset, NULL);
    const BYTE* const seg_base = shell_base + seg_offset;
    const DWORD info_offset = (BYTE*)&load_seg_encry_info - seg_begin;
    return (SEG_ENCRY_INFO*)(seg_base + info_offset);
}


ORIGIN_PE_INFO* GetOriginPeInfo(const BYTE* const shell_base) {
    assert(shell_base != NULL);

    // Relocation.
    DWORD seg_offset = 0;
    const BYTE* const seg_begin = GetLoadSegment(&seg_offset, NULL);
    const BYTE* const seg_base = shell_base + seg_offset;
    const DWORD info_offset = (BYTE*)&origin_pe_info - seg_begin;
    return (ORIGIN_PE_INFO*)(seg_base + info_offset);
}


IMAGE_TLS_DIRECTORY* GetShellTlsTable(const BYTE* const shell_base,
                                      DWORD* const offset) {
    assert(shell_base != NULL);

    // Relocation.
    DWORD seg_offset = 0;
    const BYTE* const seg_begin = GetBootSegment(&seg_offset, NULL);
    const BYTE* const seg_base = shell_base + seg_offset;
    const DWORD info_offset = (BYTE*)&tls_table - seg_begin;

    if (offset != NULL) {
        *offset = seg_offset + info_offset;
    }

    return (IMAGE_TLS_DIRECTORY*)(seg_base + info_offset);
}


BYTE* GetBootSegment(DWORD* const offset, DWORD* const size) {
    if (size != NULL) {
        *size = (BYTE*)&boot_seg_end_lbl - (BYTE*)&boot_seg_begin_lbl;
    }

    if (offset != NULL) {
        *offset = (BYTE*)&boot_seg_begin_lbl - (BYTE*)&shell_begin_lbl;
    }

    return (BYTE*)&boot_seg_begin_lbl;
}


BYTE* GetLoadSegment(DWORD* const offset, DWORD* const size) {
    if (size != NULL) {
        *size = (BYTE*)&load_seg_end_lbl - (BYTE*)&load_seg_begin_lbl;
    }

    if (offset != NULL) {
        *offset = (BYTE*)&load_seg_begin_lbl - (BYTE*)&shell_begin_lbl;
    }

    return (BYTE*)&load_seg_begin_lbl;
}