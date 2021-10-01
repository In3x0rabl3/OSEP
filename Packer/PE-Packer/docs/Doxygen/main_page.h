/**
 * @file main_page.h
 * @brief The main page of Doxygen.
 * 
 * @author Chen Zhenshuo (chenzs108@outlook.com)
 * @version 1.0
 * @date 2020-01-20
 * @par GitHub
 * https://github.com/czs108
 */

/**
 * @mainpage PE-Packer
 * 
 * @section about-the-project About The Project
 * 
 * ***PE-Packer*** is a simple packer for **Windows PE** files. The new PE file after packing can obstruct the process of *reverse engineering*.
 * 
 * It will do the following things when packing a PE file:
 * 
 * - Transforming the original import table.
 * - Encrypting sections.
 * - Clearing section names.
 * - Installing the *shell-entry*.
 * 
 * When running a packed PE file, the *shell-entry* will decrypt and load the original program as follows:
 * 
 * - Decrypting sections.
 * - Initializing the original import table.
 * - Relocation.
 * 
 * @subsection warning Warning
 * 
 * > This project is just a demo for beginners to study *PE Format* and *Assembly Language*. It still has some compatibility problems and bugs that cannot be used in practice.
 * 
 * @section getting-started Getting Started
 * 
 * @subsection prerequisites Prerequisites
 * 
 * The project must configure on/for **Windows 32-bit** and can only process **32-bit** `.exe` programs now.
 * 
 * - Install [*MASM32*](http://www.masm32.com).
 * - Install [*MinGW-w64*](https://www.mingw-w64.org), select `i686` architecture.
 * - Install [*CMake*](https://cmake.org).
 * - Set the `PATH` environment variables of these three tools.
 * 
 * @subsection building Building
 * 
 * ```bash
 * mkdir -p build
 * cd build
 * cmake .. -D CMAKE_C_COMPILER=gcc -G "MinGW Makefiles"
 * cmake --build .
 * ```
 * 
 * Or run the `build.ps1` file directly:
 * 
 * ```console
 * PS> .\build.ps1
 * ```
 * 
 * @section usage Usage
 * 
 * To pack a program, you must specify its *input name* and the *output name*.
 * 
 * ```console
 * PE-Packer <input-file> <output-file>
 * ```
 * 
 * For example:
 * 
 * ```console
 * PE-Packer hello.exe hello-pack.exe
 * ```
 * 
 * @section documents Documents
 * 
 * You can use [*Doxygen*](http://www.doxygen.nl) to generate the document.
 * 
 * In order to avoid scanning `.md` files, you must add `*.md` to the `EXCLUDE_PATTERNS` configuration option.
 * 
 * ```
 * EXCLUDE_PATTERNS = *.md
 * ```
 * 
 * This option is in "Expert" -> "Input" page.
 * 
 * @section references References
 * 
 * [*《加密与解密（第3版）》段钢*](https://book.douban.com/subject/3091212)
 * 
 * [PE Format - Windows Dev Center](https://docs.microsoft.com/en-us/windows/win32/debug/pe-format)
 * 
 * @section license License
 * 
 * Distributed under the *GNU General Public License*. See `LICENSE` for more information.
 * 
 * @section contact Contact
 * 
 * ***GitHub***: https://github.com/czs108
 * 
 * ***E-Mail***: chenzs108@outlook.com
 * 
 * ***WeChat***: chenzs108
 */