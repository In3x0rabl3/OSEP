enable_language(ASM_MASM)

add_library(shell "")

target_compile_definitions(shell PRIVATE -D_UNICODE -DUNICODE)

set(HEADER_PATH ${PROJECT_SOURCE_DIR}/include/shell)

target_include_directories(shell PUBLIC ${HEADER_PATH})

target_sources(shell
    PUBLIC
        ${HEADER_PATH}/install_shell.h
    PRIVATE
        install_shell.c
        entry_export.h
)

if(CMAKE_SIZEOF_VOID_P EQUAL 8)
    message(FATAL_ERROR "[!] Must configuring on/for x86 platform")
else()
    target_sources(shell
        PRIVATE
            entry_x86.asm
    )

    set_source_files_properties(entry_x86.asm PROPERTIES COMPILE_FLAGS "/c /coff")
    set_source_files_properties(entry_x86.asm PROPERTIES LINKER_FLAGS "/SAFESEH:NO")
endif()