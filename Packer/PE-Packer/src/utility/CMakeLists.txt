add_library(utility "")

target_compile_definitions(utility PRIVATE -D_UNICODE -DUNICODE)

set(HEADER_PATH ${PROJECT_SOURCE_DIR}/include/utility)

target_include_directories(utility PUBLIC ${HEADER_PATH})

target_sources(utility
    PUBLIC
        ${HEADER_PATH}/error_handling.h
        ${HEADER_PATH}/file_access.h
        ${HEADER_PATH}/platform_check.h
        ${HEADER_PATH}/encrypt.h
    PRIVATE
        error_handling.c
        file_access.c
        encrypt.c
)

if(CMAKE_SIZEOF_VOID_P EQUAL 8)
    target_sources(utility
        PRIVATE
            platform_check_x64.c
    )
else()
    target_sources(utility
        PRIVATE
            platform_check_x86.c
    )
endif()