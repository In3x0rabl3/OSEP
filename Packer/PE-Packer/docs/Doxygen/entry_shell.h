/**
 * @file entry_shell.h
 * @brief The Doxygen page about the entry code of the shell.
 * 
 * @author Chen Zhenshuo (chenzs108@outlook.com)
 * @version 1.0
 * @date 2020-01-14
 * @par GitHub
 * https://github.com/czs108
 */

/**
 * @page entry-code-of-shell The Entry Code of the Shell
 * @brief Documents about the entry code of the shell
 * @details The entry code is written in Microsoft Assembly Language in `.asm` files.
 * 
 * @section set-src-property How to Set the Property of the .ASM File in Visual Studio
 * 1. Right-click this file and open "Properties" -> "General" page.
 *   - Set `Excluded From Build` to `No`.
 *   - Set `Item Type` to `Custom Build Tool`.
 * 2. Right-click this file and open "Properties" -> "Custom Build Tool" page.
 *   - Set `Command Line` to `"ml /c /coff /Fo $(SolutionDir)$(ProjectName)\$(Configuration)\%(FileName).obj $(SolutionDir)$(ProjectName)\%(FileName).asm"`.
 *   - Set `Outputs` to `"$(SolutionDir)$(ProjectName)\$(Configuration)\%(FileName).obj"`.
 * 3. Right-click the project and open "Properties" -> "Linker" -> "Advanced" page.
 *   - Set `Image Has Safe Exception Handlers` to `No (/SAFESEH:NO)`.
 * 
 * @section process-of-entry-code The Process of the Entry Code
 * - The *Boot* Segment
 *   1. Decrypt and run the *Load* segment.
 * - The *Load* Segment
 *   1. Decrypt sections.
 *   2. Initialize the original import table.
 *   3. Relocation.
 */