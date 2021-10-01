add_executable(hello "")

target_compile_definitions(hello PRIVATE -D_UNICODE -DUNICODE)

target_sources(hello
    PRIVATE
        main.c
)