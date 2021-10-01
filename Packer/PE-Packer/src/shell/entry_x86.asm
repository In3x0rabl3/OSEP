; @file entry_x86.asm
; @brief The entry code of the shell.
; 
; @author Chen Zhenshuo (chenzs108@outlook.com)
; @version 1.0
; @date 2020-01-07
; @par GitHub
; https://github.com/czs108

; @note This implementation is for x86 platforms.

.586p
.model flat, stdcall
option casemap: none

include /masm32/include/windows.inc


; The maximum number of encrypted sections supported by the program.
MAX_ENCRY_SECTION_COUNT     equ     040h


; ----- The exported data, used to relocation and data storage. -----

; The beginning of the shell template.
public shell_begin_lbl


; The beginning of the import table template of the shell itself.
public imp_table_begin_lbl
; The end of the import table template of the shell itself.
public imp_table_end_lbl


; The beginning of the boot segment template.
public boot_seg_begin_lbl
; The end of the boot segment template.
public boot_seg_end_lbl


; The beginning of the load segment template.
public load_seg_begin_lbl
; The end of the load segment template.
public load_seg_end_lbl


; The encryption information of the load segment.
public load_seg_encry_info


; The original PE information.
public origin_pe_info


; The thread-local storage table.
public tls_table


; @brief The encryption information of a segment.
SEG_ENCRY_INFO      struct
    ; The offset, relative to the shell.
    seg_offset          dword   ?
    ; The size.
    seg_size            dword   ?
SEG_ENCRY_INFO      ends


; @brief The encryption information of a section.
SECTION_ENCRY_INFO  struct
    ; The relative virtual address.
    sec_rva             dword   ?
    ; The size.
    sec_size            dword   ?
SECTION_ENCRY_INFO  ends


; @brief The original PE information.
ORIGIN_PE_INFO      struct
    ; The entry point.
    entry_point         dword   ?
    ; The offset of the original import table, relative to the load segment.
    imp_table_offset    dword   ?
    ; The relative virtual address of the relocation table.
    reloc_table_rva     dword   ?
    ; The image base.
    image_base          dword   ?
    ; The encryption information of sections, up to 0x40 sections and a blank structure.
    section_encry_info  SEG_ENCRY_INFO  MAX_ENCRY_SECTION_COUNT + 1 dup(<?>)
ORIGIN_PE_INFO      ends


; @brief Decrypt data.
;
; @param src    The base address of the encrypted data.
; @param dest   The space where the decrypted data will be saved.
; @param count  The size of the data.
;
; @see `EncryptData()`
DecryptData         proto   src: dword, dest: dword, count: dword


; @brief Set the protection of sections.
;
; @param virtual_protect_addr   The address of `VirtualProtect` API.
; @param module                 The PE image.
; @param new_protect
; The base address of a DWORD array, saving the new protection of each section.
; @param[out] old_protect
; The base address of a DWORD array, saving the old protection of each section.
SetSectionProtect   proto   virtual_protect_addr: dword, module: dword, new_protect: dword, old_protect: dword


; @brief Get the information of sections.
;
; @param module The PE image.
; @return eax   The base address of the `IMAGE_SECTION_HEADER` array.
; @return ecx   The number of sections.
GetSectionHeader    proto   module: dword


assume fs: nothing

.code
shell_begin_lbl     label   dword

; ------------------------ Boot Segment ------------------------
boot_seg_begin_lbl  label   dword
    pushad
    call    _boot

    ; ------------------------ Import Table ------------------------
    imp_table_begin_lbl     label   dword

        ; All relative virtual addresses are relative to the beginning of the import table,
        ; the adjustment will be done when installing the shell.
        import_table        IMAGE_IMPORT_DESCRIPTOR     <<first_thunk - imp_table_begin_lbl>, 0, 0, dll_name - imp_table_begin_lbl, first_thunk - imp_table_begin_lbl>
                            IMAGE_IMPORT_DESCRIPTOR     <<0>, 0, 0, 0, 0>

        first_thunk         IMAGE_THUNK_DATA            <<first_func_name - imp_table_begin_lbl>>
        second_thunk        IMAGE_THUNK_DATA            <<second_func_name - imp_table_begin_lbl>>
        third_thunk         IMAGE_THUNK_DATA            <<third_func_name - imp_table_begin_lbl>>
                            IMAGE_THUNK_DATA            <<0>>

        dll_name            db      'Kernel32.dll', 0

        ; The `IMAGE_IMPORT_BY_NAME` structures.
        first_func_name     dw      0
                            db      'GetProcAddress', 0
        second_func_name    dw      0
                            db      'GetModuleHandleA', 0
        third_func_name     dw      0
                            db      'LoadLibraryA', 0

    imp_table_end_lbl       label   dword
    ; --------------------------------------------------------------

    ; The handle of the current process, just used in the boot segment.
    process_handle_boot         dd      0

    load_seg_encry_info     SEG_ENCRY_INFO  <?>

    tls_table               IMAGE_TLS_DIRECTORY     <?>

    get_current_process_name    db      'GetCurrentProcess', 0

    ; The address of `GetCurrentProcess` API.
    get_current_process_addr    dd      0

    virtual_alloc_name          db      'VirtualAlloc', 0

    ; The address of `VirtualAlloc` API, just used in the boot segment.
    virtual_alloc_addr_boot     dd      0

    flush_instruction_cache_name        db      'FlushInstructionCache', 0

    ; The address of `FlushInstructionCache` API, just used in the boot segment.
    flush_instruction_cache_addr_boot   dd      0

    ; The base address of the load segment after decryption.
    load_seg_base               dd      0

_boot:
    ; Self-relocation.
    pop     ebp
    ; `ebp` is the base address of the boot segment.
    sub     ebp, imp_table_begin_lbl - boot_seg_begin_lbl

    ; Get the address of `GetCurrentProcess` API.
    lea     esi, [ebp + (dll_name - boot_seg_begin_lbl)]
    push    esi
    call    dword ptr [ebp + (second_thunk - boot_seg_begin_lbl)]
    lea     esi, [ebp + (get_current_process_name - boot_seg_begin_lbl)]
    push    esi
    push    eax
    call    dword ptr [ebp + (first_thunk - boot_seg_begin_lbl)]
    mov     dword ptr [ebp + (get_current_process_addr - boot_seg_begin_lbl)], eax

    ; Get the address of `VirtualAlloc` API.
    lea     esi, [ebp + (dll_name - boot_seg_begin_lbl)]
    push    esi
    call    dword ptr [ebp + (second_thunk - boot_seg_begin_lbl)]
    lea     esi, [ebp + (virtual_alloc_name - boot_seg_begin_lbl)]
    push    esi
    push    eax
    call    dword ptr [ebp + (first_thunk - boot_seg_begin_lbl)]
    mov     dword ptr [ebp + (virtual_alloc_addr_boot - boot_seg_begin_lbl)], eax

    ; Get the address of `FlushInstructionCache` API.
    lea     esi, [ebp + (dll_name - boot_seg_begin_lbl)]
    push    esi
    call    dword ptr [ebp + (second_thunk - boot_seg_begin_lbl)]
    lea     esi, [ebp + (flush_instruction_cache_name - boot_seg_begin_lbl)]
    push    esi
    push    eax
    call    dword ptr [ebp + (first_thunk - boot_seg_begin_lbl)]
    mov     dword ptr [ebp + (flush_instruction_cache_addr_boot - boot_seg_begin_lbl)], eax

    ; Allocate memory for the load segment.
    push    PAGE_EXECUTE_READWRITE
    push    MEM_COMMIT or MEM_RESERVE
    mov     eax, load_seg_encry_info - boot_seg_begin_lbl
    add     eax, ebp
    assume  eax: ptr SEG_ENCRY_INFO
    push    [eax].seg_size
    assume  eax: nothing
    push    NULL
    call    dword ptr [ebp + (virtual_alloc_addr_boot - boot_seg_begin_lbl)]
    mov     dword ptr [ebp + (load_seg_base - boot_seg_begin_lbl)], eax

    ; Decrypt the load segment.
    mov     ecx, load_seg_encry_info - boot_seg_begin_lbl
    add     ecx, ebp
    assume  ecx: ptr SEG_ENCRY_INFO
    push    [ecx].seg_size
    assume  ecx: nothing
    push    eax
    mov     ebx, load_seg_encry_info - boot_seg_begin_lbl
    add     ebx, ebp
    assume  ebx: ptr SEG_ENCRY_INFO
    mov     ebx, [ebx].seg_offset
    add     ebx, ebp
    assume  ebx: nothing
    push    ebx
    call    DecryptData

    ; Format a jump instruction to the load segment.
    push    ebp     ; Save the base address of the boot segment.
    mov     eax, dword ptr [ebp + (load_seg_base - boot_seg_begin_lbl)]
    mov     edx, ebp
    add     edx, (_jmp_load_seg - boot_seg_begin_lbl) + sizeof(BYTE) * 5
    sub     eax, edx
    mov     dword ptr [ebp + (_jmp_load_seg - boot_seg_begin_lbl) + sizeof(BYTE)], eax

    call    dword ptr [ebp + (get_current_process_addr - boot_seg_begin_lbl)]
    mov     dword ptr [ebp + (process_handle_boot - boot_seg_begin_lbl)], eax
    push    0
    push    NULL
    push    eax
    call    dword ptr [ebp + (flush_instruction_cache_addr_boot - boot_seg_begin_lbl)]

_jmp_load_seg:
    ; Jump to the load segment.
    DB      0E9h, 0FFh, 0FFh, 0FFh, 0FFh

    DecryptData proc    src: dword, dest: dword, count: dword
        pushad
        mov     ecx, count
        mov     esi, src
        mov     edi, dest
        .while  ecx != 0
            lodsb
            sub     al, 0CCh
            stosb
            dec     ecx
        .endw
        popad
        ret
    DecryptData endp

boot_seg_end_lbl    label   dword
; --------------------------------------------------------------


; ------------------------ Load Segment ------------------------
load_seg_begin_lbl  label   dword
    call    _next
_next:
    ; Self-relocation.
    pop     ebp
    ; `ebp` is the base address of the load segment.
    sub     ebp, _next - load_seg_begin_lbl
    ; `edx` is the base address of the boot segment.
    pop     edx

    ; Copy some data of the boot segment to the load segment.
    mov     ecx, 3
    lea     esi, [edx + (first_thunk - boot_seg_begin_lbl)]
    lea     edi, [ebp + (get_proc_address_addr - load_seg_begin_lbl)]
    cld
    rep     movsd

    mov     eax, dword ptr [edx + (process_handle_boot - boot_seg_begin_lbl)]
    mov     dword ptr [ebp + (process_handle - load_seg_begin_lbl)], eax
    lea     eax, [edx + (DecryptData - boot_seg_begin_lbl)]
    mov     dword ptr [ebp + (decrypt_data_addr - load_seg_begin_lbl)], eax
    mov     eax, dword ptr [edx + (virtual_alloc_addr_boot - boot_seg_begin_lbl)]
    mov     dword ptr [ebp + (virtual_alloc_addr - load_seg_begin_lbl)], eax
    mov     eax, dword ptr [edx + (flush_instruction_cache_addr_boot - boot_seg_begin_lbl)]
    mov     dword ptr [ebp + (flush_instruction_cache_addr - load_seg_begin_lbl)], eax

    ; Get the address of `VirtualProtect` API.
    lea     esi, [ebp + (kernel32_name - load_seg_begin_lbl)]
    push    esi
    call    dword ptr [ebp + (get_module_handle_addr - load_seg_begin_lbl)]
    lea     esi, [ebp + (virtual_protect_name - load_seg_begin_lbl)]
    push    esi
    push    eax
    call    dword ptr [ebp + (get_proc_address_addr - load_seg_begin_lbl)]
    mov     dword ptr [ebp + (virtual_protect_addr - load_seg_begin_lbl)], eax

    ; Get the actual base address of the PE image after loading.
    push    NULL
    call    dword ptr [ebp + (get_module_handle_addr - load_seg_begin_lbl)]
    mov     dword ptr [ebp + (module - load_seg_begin_lbl)], eax

    ; Set the protection of sections.
    mov     ecx, lengthof section_protections
    mov     eax, PAGE_EXECUTE_READWRITE
    lea     edi, [ebp + (section_protections - load_seg_begin_lbl)]
    cld
    rep     stosd

    lea     esi, [ebp + (section_protections - load_seg_begin_lbl)]
    lea     edi, [ebp + (section_protections - load_seg_begin_lbl)]
    push    edi
    push    esi
    push    dword ptr [ebp + (module - load_seg_begin_lbl)]
    push    dword ptr [ebp + (virtual_protect_addr - load_seg_begin_lbl)]
    call    SetSectionProtect

    ; Decrypt sections.
    mov     edx, origin_pe_info - load_seg_begin_lbl
    add     edx, ebp
    assume  edx: ptr ORIGIN_PE_INFO
    lea     edx, [edx].section_encry_info
    assume  edx: ptr SECTION_ENCRY_INFO
    mov     eax, [edx].sec_rva
    .while  eax != NULL
        ; Get the virtual address.
        mov     esi, dword ptr [ebp + (module - load_seg_begin_lbl)]
        add     esi, eax
        mov     edi, esi
        ; Get the size.
        mov     ecx, [edx].sec_size
        push    ecx
        push    edi
        push    esi
        call    dword ptr [ebp + (decrypt_data_addr - load_seg_begin_lbl)]
        add     edx, sizeof(SECTION_ENCRY_INFO)
        mov     eax, [edx].sec_rva
    .endw
    assume  edx: nothing

    ; Initialize the original import table.
    mov     esi, origin_pe_info - load_seg_begin_lbl
    add     esi, ebp
    assume  esi: ptr ORIGIN_PE_INFO
    mov     esi, [esi].imp_table_offset
    add     esi, ebp
    assume  esi: ptr nothing
    mov     edi, [esi]
    ; The `FirstThunk`.
    .while  edi != NULL
        add     edi, dword ptr [ebp + (module - load_seg_begin_lbl)]
        ; The DLL name.
        add     esi, sizeof(DWORD) + sizeof(BYTE)
        ; Load the DLL.
        push    esi
        call    dword ptr [ebp + (get_module_handle_addr - load_seg_begin_lbl)]
        .if     eax == NULL
            push    esi
            call    dword ptr [ebp + (load_library_addr - load_seg_begin_lbl)]
        .endif
        mov     edx, eax
        movzx   ecx, byte ptr [esi - sizeof(BYTE)]
        add     esi, ecx
        ; The number of functions.
        mov     ecx, dword ptr [esi]
        add     esi, sizeof(DWORD)
        .while  ecx != 0
            push    ecx
            push    edx
            ; The size of the function name.
            movzx   ebx, byte ptr [esi]
            inc     esi
            ; Imported by the order.
            .if     ebx == 0
                ; The function order
                mov     ebx, dword ptr [esi]
                add     esi, sizeof(DWORD)
                push    ebx
            ; Imported by the name.
            .else
                ; The function name.
                push    esi
                add     esi, ebx
            .endif
            push    edx
            ; Get the address of the function.
            call    dword ptr [ebp + (get_proc_address_addr - load_seg_begin_lbl)]
            ; Save the address to the import address table (IAT).
            mov     dword ptr [edi], eax
            add     edi, sizeof(DWORD)
            pop     edx
            pop     ecx
            dec     ecx
        .endw
        mov     edi, dword ptr [esi]
    .endw

    ; Relocation.
    mov     edx, origin_pe_info - load_seg_begin_lbl
    add     edx, ebp
    assume  edx: ptr ORIGIN_PE_INFO
    ; `edx` is the default base address of the PE image.
    mov     edx, [edx].image_base
    assume  edx: ptr nothing
    mov     ebx, dword ptr [ebp + (module - load_seg_begin_lbl)]
    .if     ebx != edx
        mov     esi, origin_pe_info - load_seg_begin_lbl
        add     esi, ebp
        assume  esi: ptr ORIGIN_PE_INFO
        mov     esi, [esi].reloc_table_rva
        assume  esi: ptr nothing
        .if     esi != NULL
            add     esi, ebx
            assume  esi: ptr IMAGE_BASE_RELOCATION
            mov     edi, [esi].VirtualAddress
            .while  edi != NULL
                mov     ecx, [esi].SizeOfBlock
                sub     ecx, sizeof(IMAGE_BASE_RELOCATION)
                shr     ecx, 1
                add     esi, sizeof(IMAGE_BASE_RELOCATION)
                .while  ecx != 0
                    xor     eax, eax
                    mov     ax, word ptr [esi]
                    and     ax, 0F000h
                    shr     ax, 12
                    ; Check the relocation type.
                    .if     ax == IMAGE_REL_BASED_HIGHLOW
                        xor     eax, eax
                        mov     ax, word ptr [esi]
                        ; Get the relocation offset.
                        and     ax, 0FFFh
                        push    edi
                        add     edi, eax
                        add     edi, ebx
                        ; Adjust the address.
                        mov     eax, dword ptr [edi]
                        sub     eax, edx
                        add     eax, ebx
                        mov     dword ptr [edi], eax
                        pop     edi
                    .endif
                    add     esi, sizeof(WORD)
                    dec     ecx
                .endw
                mov     edi, [esi].VirtualAddress
            .endw
            assume  esi: nothing
        .endif
    .endif

    ; Recover the original protection of sections.
    lea     esi, [ebp + (section_protections - load_seg_begin_lbl)]
    lea     edi, [ebp + (section_protections - load_seg_begin_lbl)]
    push    edi
    push    esi
    push    dword ptr [ebp + (module - load_seg_begin_lbl)]
    push    dword ptr [ebp + (virtual_protect_addr - load_seg_begin_lbl)]
    call    SetSectionProtect

    ; Jump to the original entry.
    mov     eax, origin_pe_info - load_seg_begin_lbl
    add     eax, ebp
    assume  eax: ptr ORIGIN_PE_INFO
    mov     eax, [eax].entry_point
    assume  eax: ptr nothing
    add     eax, dword ptr [ebp + (module - load_seg_begin_lbl)]
    mov     dword ptr [ebp + (_ret_oep - load_seg_begin_lbl) + sizeof(BYTE)], eax

    push    0
    push    NULL
    mov     eax, dword ptr [ebp + (process_handle - load_seg_begin_lbl)]
    push    eax
    call    dword ptr [ebp + (flush_instruction_cache_addr - load_seg_begin_lbl)]

    popad

_ret_oep:
    ; Push the entry point.
    DB      68h, 0FFh, 0FFh, 0FFh, 0FFh
    ret


    GetSectionHeader        proc    module: dword
        mov     eax, module
        assume  eax: ptr IMAGE_DOS_HEADER
        add     eax, [eax].e_lfanew
        assume  eax: ptr IMAGE_NT_HEADERS
        ; `ecx` is the number of sections.
        movzx   ecx, [eax].FileHeader.NumberOfSections
        add     ax, [eax].FileHeader.SizeOfOptionalHeader
        add     eax, sizeof(DWORD)
        add     eax, sizeof(IMAGE_FILE_HEADER)
        assume  eax: nothing
        ret
    GetSectionHeader        endp


    SetSectionProtect       proc   virtual_protect_addr: dword, module: dword, new_protect: dword, old_protect: dword
        pushad
        push    module
        call    GetSectionHeader
        ; `ecx` is the number of sections.
        ; `edx` is base address of the `IMAGE_SECTION_HEADER` array.
        mov     ebx, eax
        assume  ebx: ptr IMAGE_SECTION_HEADER
        mov     esi, new_protect
        mov     edi, old_protect
        xor     edx, edx
        .while  edx != ecx
            pushad
            lea     eax, [edi + sizeof(DWORD) * edx]
            push    eax
            mov     eax, dword ptr [esi + sizeof(DWORD) * edx]
            push    eax
            push    [ebx].Misc.VirtualSize
            mov     eax, [ebx].VirtualAddress
            add     eax, module
            push    eax
            call    virtual_protect_addr
            popad
            add     ebx, sizeof(IMAGE_SECTION_HEADER)
            inc     edx
        .endw
        assume  ebx: nothing
        popad
        ret
    SetSectionProtect       endp


    origin_pe_info          ORIGIN_PE_INFO  <>

    ; The order of the following 3 variables is the same as that of APIs in the import table,
    ; it's convenient for data copy.
    get_proc_address_addr   dd      0
    get_module_handle_addr  dd      0
    load_library_addr       dd      0

    flush_instruction_cache_addr    dd      0
    virtual_alloc_addr              dd      0
    virtual_protect_addr            dd      0
    decrypt_data_addr               dd      0

    ; The handle of the current process.
    process_handle          dd      0

    ; The actual base address of the PE image after loading.
    module                  dd      0

    ; The protection of sections.
    section_protections     dd      MAX_ENCRY_SECTION_COUNT dup(?)

    kernel32_name           db      'Kernel32.dll', 0
    virtual_protect_name    db      'VirtualProtect', 0

load_seg_end_lbl    label   dword
; --------------------------------------------------------------

end