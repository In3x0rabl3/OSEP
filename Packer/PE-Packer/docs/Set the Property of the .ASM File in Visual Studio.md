# Set the Property of the .ASM File in Visual Studio

The entry code of the shell is written in Microsoft Assembly Language in `.asm` files.

1. Right-click the `.asm` file and open "***Properties***" -> "***General***" page.
   - Set `Excluded From Build` to `No`.
   - Set `Item Type` to `Custom Build Tool`.
2. Right-click the `.asm` file and open "***Properties***" -> "***Custom Build Tool***" page.
   - Set `Command Line` to `"ml /c /coff /Fo $(SolutionDir)$(ProjectName)\$(Configuration)\%(FileName).obj $(SolutionDir)$(ProjectName)\%(FileName).asm"`.
   - Set `Outputs` to `"$(SolutionDir)$(ProjectName)\$(Configuration)\%(FileName).obj"`.
3. Right-click the project and open "***Properties***" -> "***Linker***" -> "***Advanced***" page.
   - Set `Image Has Safe Exception Handlers` to `No (/SAFESEH:NO)`.