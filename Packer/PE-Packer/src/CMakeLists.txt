add_subdirectory(utility)
add_subdirectory(shell)

add_executable(PE-Packer "")

target_compile_definitions(PE-Packer PRIVATE -D_UNICODE -DUNICODE)

set(HEADER_PATH ${PROJECT_SOURCE_DIR}/include)

target_include_directories(PE-Packer PRIVATE ${HEADER_PATH})

target_sources(PE-Packer
    PRIVATE
        main.c
        extra_data.c
        image.c
        import_table.c
        section.c
        ${HEADER_PATH}/extra_data.h
        ${HEADER_PATH}/image.h
        ${HEADER_PATH}/import_table.h
        ${HEADER_PATH}/section.h
)

target_link_libraries(PE-Packer PRIVATE utility)
target_link_libraries(PE-Packer PRIVATE shell)