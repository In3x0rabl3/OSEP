using System;
using System.Runtime.InteropServices;

namespace CheeseRDP
{
    class PEStructures
    {

        [StructLayout(LayoutKind.Sequential)]
        public struct _MANUAL_INJECT
        {
            public IntPtr ImageBase;
            public IMAGE_NT_HEADERS64 NtHeaders;
            public IMAGE_BASE_RELOCATION BaseRelocation;
            public IMAGE_IMPORT_DESCRIPTOR ImportDirectory;
        }

        [StructLayout(LayoutKind.Explicit, Size = 8)]
        internal readonly struct IMAGE_BASE_RELOCATION
        {
            [FieldOffset(0x0)]
            internal readonly int VirtualAddress;

            [FieldOffset(0x4)]
            internal readonly int SizeOfBlock;
        }

        [StructLayout(LayoutKind.Explicit)]
        public struct IMAGE_IMPORT_DESCRIPTOR
        {
            [FieldOffset(0)]
            public UInt32 Characteristics;

            [FieldOffset(0)]
            public UInt32 OriginalFirstThunk;

            [FieldOffset(4)]
            public UInt32 TimeDateStamp;

            [FieldOffset(8)]
            public UInt32 ForwarderChain;

            [FieldOffset(12)]
            public UInt32 Name;

            [FieldOffset(16)]
            public UInt32 FirstThunk;
        }

        [StructLayout(LayoutKind.Explicit)]
        public struct IMAGE_NT_HEADERS32
        {
            [FieldOffset(0)]
            [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4)]
            public char[] Signature;

            [FieldOffset(4)]
            public IMAGE_FILE_HEADER FileHeader;

            [FieldOffset(24)]
            public IMAGE_OPTIONAL_HEADER32 OptionalHeader;

            private string _Signature
            {
                get { return new string(Signature); }
            }

            public bool isValid
            {
                get { return _Signature == "PE\0\0" && OptionalHeader.Magic == MagicType.IMAGE_NT_OPTIONAL_HDR32_MAGIC; }
            }
        }

        [StructLayout(LayoutKind.Sequential)]
        public struct IMAGE_FILE_HEADER
        {
            public UInt16 Machine;
            public UInt16 NumberOfSections;
            public UInt32 TimeDateStamp;
            public UInt32 PointerToSymbolTable;
            public UInt32 NumberOfSymbols;
            public UInt16 SizeOfOptionalHeader;
            public UInt16 Characteristics;
        }

        [StructLayout(LayoutKind.Sequential, Pack = 1)]
        struct IMAGE_EXPORT_DIRECTORY
        {
            public UInt32 Characteristics;
            public UInt32 TimeDateStamp;
            public UInt16 MajorVersion;
            public UInt16 MinorVersion;
            public UInt32 Name;
            public UInt32 Base;
            public UInt32 NumberOfFunctions;
            public UInt32 NumberOfNames;
            public UInt32 AddressOfFunctions;     // RVA from base of image
            public UInt32 AddressOfNames;         // RVA from base of image
            public UInt32 AddressOfNameOrdinals;  // RVA from base of image
        }

        [StructLayout(LayoutKind.Explicit)]
        public struct IMAGE_NT_HEADERS64
        {
            [FieldOffset(0)]
            [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4)]
            public char[] Signature;

            [FieldOffset(4)]
            public IMAGE_FILE_HEADER FileHeader;

            [FieldOffset(24)]
            public IMAGE_OPTIONAL_HEADER64 OptionalHeader;

            private string _Signature
            {
                get { return new string(Signature); }
            }

            public bool isValid
            {
                get { return _Signature == "PE\0\0" && OptionalHeader.Magic == MagicType.IMAGE_NT_OPTIONAL_HDR64_MAGIC; }
            }
        }

        public enum MachineType : UInt16
        {
            Native = 0,
            I386 = 0x014c,
            Itanium = 0x0200,
            x64 = 0x8664
        }
        public enum MagicType : UInt16
        {
            IMAGE_NT_OPTIONAL_HDR32_MAGIC = 0x10b,
            IMAGE_NT_OPTIONAL_HDR64_MAGIC = 0x20b
        }
        public enum SubSystemType : UInt16
        {
            IMAGE_SUBSYSTEM_UNKNOWN = 0,
            IMAGE_SUBSYSTEM_NATIVE = 1,
            IMAGE_SUBSYSTEM_WINDOWS_GUI = 2,
            IMAGE_SUBSYSTEM_WINDOWS_CUI = 3,
            IMAGE_SUBSYSTEM_POSIX_CUI = 7,
            IMAGE_SUBSYSTEM_WINDOWS_CE_GUI = 9,
            IMAGE_SUBSYSTEM_EFI_APPLICATION = 10,
            IMAGE_SUBSYSTEM_EFI_BOOT_SERVICE_DRIVER = 11,
            IMAGE_SUBSYSTEM_EFI_RUNTIME_DRIVER = 12,
            IMAGE_SUBSYSTEM_EFI_ROM = 13,
            IMAGE_SUBSYSTEM_XBOX = 14

        }
        public enum DllCharacteristicsType : UInt16
        {
            RES_0 = 0x0001,
            RES_1 = 0x0002,
            RES_2 = 0x0004,
            RES_3 = 0x0008,
            IMAGE_DLL_CHARACTERISTICS_DYNAMIC_BASE = 0x0040,
            IMAGE_DLL_CHARACTERISTICS_FORCE_INTEGRITY = 0x0080,
            IMAGE_DLL_CHARACTERISTICS_NX_COMPAT = 0x0100,
            IMAGE_DLLCHARACTERISTICS_NO_ISOLATION = 0x0200,
            IMAGE_DLLCHARACTERISTICS_NO_SEH = 0x0400,
            IMAGE_DLLCHARACTERISTICS_NO_BIND = 0x0800,
            RES_4 = 0x1000,
            IMAGE_DLLCHARACTERISTICS_WDM_DRIVER = 0x2000,
            IMAGE_DLLCHARACTERISTICS_TERMINAL_SERVER_AWARE = 0x8000
        }

        [StructLayout(LayoutKind.Explicit)]
        public struct IMAGE_OPTIONAL_HEADER32
        {
            [FieldOffset(0)]
            public MagicType Magic;

            [FieldOffset(2)]
            public byte MajorLinkerVersion;

            [FieldOffset(3)]
            public byte MinorLinkerVersion;

            [FieldOffset(4)]
            public UInt32 SizeOfCode;

            [FieldOffset(8)]
            public UInt32 SizeOfInitializedData;

            [FieldOffset(12)]
            public UInt32 SizeOfUninitializedData;

            [FieldOffset(16)]
            public UInt32 AddressOfEntryPoint;

            [FieldOffset(20)]
            public UInt32 BaseOfCode;

            // PE32 contains this additional field
            [FieldOffset(24)]
            public UInt32 BaseOfData;

            [FieldOffset(28)]
            public UInt32 ImageBase;

            [FieldOffset(32)]
            public UInt32 SectionAlignment;

            [FieldOffset(36)]
            public UInt32 FileAlignment;

            [FieldOffset(40)]
            public UInt16 MajorOperatingSystemVersion;

            [FieldOffset(42)]
            public UInt16 MinorOperatingSystemVersion;

            [FieldOffset(44)]
            public UInt16 MajorImageVersion;

            [FieldOffset(46)]
            public UInt16 MinorImageVersion;

            [FieldOffset(48)]
            public UInt16 MajorSubsystemVersion;

            [FieldOffset(50)]
            public UInt16 MinorSubsystemVersion;

            [FieldOffset(52)]
            public UInt32 Win32VersionValue;

            [FieldOffset(56)]
            public UInt32 SizeOfImage;

            [FieldOffset(60)]
            public UInt32 SizeOfHeaders;

            [FieldOffset(64)]
            public UInt32 CheckSum;

            [FieldOffset(68)]
            public SubSystemType Subsystem;

            [FieldOffset(70)]
            public DllCharacteristicsType DllCharacteristics;

            [FieldOffset(72)]
            public UInt32 SizeOfStackReserve;

            [FieldOffset(76)]
            public UInt32 SizeOfStackCommit;

            [FieldOffset(80)]
            public UInt32 SizeOfHeapReserve;

            [FieldOffset(84)]
            public UInt32 SizeOfHeapCommit;

            [FieldOffset(88)]
            public UInt32 LoaderFlags;

            [FieldOffset(92)]
            public UInt32 NumberOfRvaAndSizes;

            [FieldOffset(96)]
            public IMAGE_DATA_DIRECTORY ExportTable;

            [FieldOffset(104)]
            public IMAGE_DATA_DIRECTORY ImportTable;

            [FieldOffset(112)]
            public IMAGE_DATA_DIRECTORY ResourceTable;

            [FieldOffset(120)]
            public IMAGE_DATA_DIRECTORY ExceptionTable;

            [FieldOffset(128)]
            public IMAGE_DATA_DIRECTORY CertificateTable;

            [FieldOffset(136)]
            public IMAGE_DATA_DIRECTORY BaseRelocationTable;

            [FieldOffset(144)]
            public IMAGE_DATA_DIRECTORY Debug;

            [FieldOffset(152)]
            public IMAGE_DATA_DIRECTORY Architecture;

            [FieldOffset(160)]
            public IMAGE_DATA_DIRECTORY GlobalPtr;

            [FieldOffset(168)]
            public IMAGE_DATA_DIRECTORY TLSTable;

            [FieldOffset(176)]
            public IMAGE_DATA_DIRECTORY LoadConfigTable;

            [FieldOffset(184)]
            public IMAGE_DATA_DIRECTORY BoundImport;

            [FieldOffset(192)]
            public IMAGE_DATA_DIRECTORY IAT;

            [FieldOffset(200)]
            public IMAGE_DATA_DIRECTORY DelayImportDescriptor;

            [FieldOffset(208)]
            public IMAGE_DATA_DIRECTORY CLRRuntimeHeader;

            [FieldOffset(216)]
            public IMAGE_DATA_DIRECTORY Reserved;
        }
        [StructLayout(LayoutKind.Explicit)]
        public struct IMAGE_OPTIONAL_HEADER64
        {
            [FieldOffset(0)]
            public MagicType Magic;

            [FieldOffset(2)]
            public byte MajorLinkerVersion;

            [FieldOffset(3)]
            public byte MinorLinkerVersion;

            [FieldOffset(4)]
            public UInt32 SizeOfCode;

            [FieldOffset(8)]
            public UInt32 SizeOfInitializedData;

            [FieldOffset(12)]
            public UInt32 SizeOfUninitializedData;

            [FieldOffset(16)]
            public UInt32 AddressOfEntryPoint;

            [FieldOffset(20)]
            public UInt32 BaseOfCode;

            [FieldOffset(24)]
            public ulong ImageBase;

            [FieldOffset(32)]
            public UInt32 SectionAlignment;

            [FieldOffset(36)]
            public UInt32 FileAlignment;

            [FieldOffset(40)]
            public UInt16 MajorOperatingSystemVersion;

            [FieldOffset(42)]
            public UInt16 MinorOperatingSystemVersion;

            [FieldOffset(44)]
            public UInt16 MajorImageVersion;

            [FieldOffset(46)]
            public UInt16 MinorImageVersion;

            [FieldOffset(48)]
            public UInt16 MajorSubsystemVersion;

            [FieldOffset(50)]
            public UInt16 MinorSubsystemVersion;

            [FieldOffset(52)]
            public UInt32 Win32VersionValue;

            [FieldOffset(56)]
            public UInt32 SizeOfImage;

            [FieldOffset(60)]
            public UInt32 SizeOfHeaders;

            [FieldOffset(64)]
            public UInt32 CheckSum;

            [FieldOffset(68)]
            public SubSystemType Subsystem;

            [FieldOffset(70)]
            public DllCharacteristicsType DllCharacteristics;

            [FieldOffset(72)]
            public ulong SizeOfStackReserve;

            [FieldOffset(80)]
            public ulong SizeOfStackCommit;

            [FieldOffset(88)]
            public ulong SizeOfHeapReserve;

            [FieldOffset(96)]
            public ulong SizeOfHeapCommit;

            [FieldOffset(104)]
            public UInt32 LoaderFlags;

            [FieldOffset(108)]
            public UInt32 NumberOfRvaAndSizes;

            [FieldOffset(112)]
            public IMAGE_DATA_DIRECTORY ExportTable;

            [FieldOffset(120)]
            public IMAGE_DATA_DIRECTORY ImportTable;

            [FieldOffset(128)]
            public IMAGE_DATA_DIRECTORY ResourceTable;

            [FieldOffset(136)]
            public IMAGE_DATA_DIRECTORY ExceptionTable;

            [FieldOffset(144)]
            public IMAGE_DATA_DIRECTORY CertificateTable;

            [FieldOffset(152)]
            public IMAGE_DATA_DIRECTORY BaseRelocationTable;

            [FieldOffset(160)]
            public IMAGE_DATA_DIRECTORY Debug;

            [FieldOffset(168)]
            public IMAGE_DATA_DIRECTORY Architecture;

            [FieldOffset(176)]
            public IMAGE_DATA_DIRECTORY GlobalPtr;

            [FieldOffset(184)]
            public IMAGE_DATA_DIRECTORY TLSTable;

            [FieldOffset(192)]
            public IMAGE_DATA_DIRECTORY LoadConfigTable;

            [FieldOffset(200)]
            public IMAGE_DATA_DIRECTORY BoundImport;

            [FieldOffset(208)]
            public IMAGE_DATA_DIRECTORY IAT;

            [FieldOffset(216)]
            public IMAGE_DATA_DIRECTORY DelayImportDescriptor;

            [FieldOffset(224)]
            public IMAGE_DATA_DIRECTORY CLRRuntimeHeader;

            [FieldOffset(232)]
            public IMAGE_DATA_DIRECTORY Reserved;
        }

        [StructLayout(LayoutKind.Sequential)]
        public struct IMAGE_DATA_DIRECTORY
        {
            public UInt32 VirtualAddress;
            public UInt32 Size;
        }

        [StructLayout(LayoutKind.Sequential, Pack = 1)]
        struct IMAGE_DOS_HEADER
        {
            public IMAGE_DOS_SIGNATURE e_magic;        // Magic number
            public UInt16 e_cblp;                      // public bytes on last page of file
            public UInt16 e_cp;                        // Pages in file
            public UInt16 e_crlc;                      // Relocations
            public UInt16 e_cparhdr;                   // Size of header in paragraphs
            public UInt16 e_minalloc;                  // Minimum extra paragraphs needed
            public UInt16 e_maxalloc;                  // Maximum extra paragraphs needed
            public UInt16 e_ss;                        // Initial (relative) SS value
            public UInt16 e_sp;                        // Initial SP value
            public UInt16 e_csum;                      // Checksum
            public UInt16 e_ip;                        // Initial IP value
            public UInt16 e_cs;                        // Initial (relative) CS value
            public UInt16 e_lfarlc;                    // File address of relocation table
            public UInt16 e_ovno;                      // Overlay number
            [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 8)]
            public string e_res;                       // May contain 'Detours!'
            public UInt16 e_oemid;                     // OEM identifier (for e_oeminfo)
            public UInt16 e_oeminfo;                   // OEM information; e_oemid specific
            [MarshalAsAttribute(UnmanagedType.ByValArray, SizeConst = 10)]
            public UInt16[] e_res2;                      // Reserved public UInt16s
            public Int32 e_lfanew;                    // File address of new exe header
        }

        [StructLayout(LayoutKind.Explicit)]
        unsafe struct IMAGE_SECTION_HEADER
        {
            [FieldOffset(0)]
            public fixed byte Name[8];
            [FieldOffset(8)]
            public UInt32 PhysicalAddress;
            [FieldOffset(8)]
            public UInt32 VirtualSize;
            [FieldOffset(12)]
            public UInt32 VirtualAddress;
            [FieldOffset(16)]
            public UInt32 SizeOfRawData;
            [FieldOffset(20)]
            public UInt32 PointerToRawData;
            [FieldOffset(24)]
            public UInt32 PointerToRelocations;
            [FieldOffset(28)]
            public UInt32 PointerToLinenumbers;
            [FieldOffset(32)]
            public UInt16 NumberOfRelocations;
            [FieldOffset(34)]
            public UInt16 NumberOfLinenumbers;
            [FieldOffset(36)]
            public UInt32 Characteristics;
        }

        enum IMAGE_DOS_SIGNATURE : UInt32
        {
            DOS_SIGNATURE = 0x5A4D,      // MZ
            OS2_SIGNATURE = 0x454E,      // NE
            OS2_SIGNATURE_LE = 0x454C,      // LE
        }
        public static IntPtr Rva2Offset(UInt32 dwRva, IntPtr PEPointer)
        {
            bool is64Bit = false;
            UInt16 wIndex = 0;
            UInt16 wNumberOfSections = 0;
            IntPtr imageSectionPtr;
            IMAGE_SECTION_HEADER SectionHeader;
            int sizeOfSectionHeader = Marshal.SizeOf(typeof(IMAGE_SECTION_HEADER));

            IMAGE_DOS_HEADER dosHeader = (IMAGE_DOS_HEADER)Marshal.PtrToStructure(PEPointer, typeof(IMAGE_DOS_HEADER));

            IntPtr NtHeadersPtr = (IntPtr)((UInt64)PEPointer + (UInt64)dosHeader.e_lfanew);

            var imageNtHeaders32 = (IMAGE_NT_HEADERS32)Marshal.PtrToStructure(NtHeadersPtr, typeof(IMAGE_NT_HEADERS32));
            var imageNtHeaders64 = (IMAGE_NT_HEADERS64)Marshal.PtrToStructure(NtHeadersPtr, typeof(IMAGE_NT_HEADERS64));

            if (imageNtHeaders64.OptionalHeader.Magic == MagicType.IMAGE_NT_OPTIONAL_HDR64_MAGIC) is64Bit = true;


            if (is64Bit)
            {
                imageSectionPtr = (IntPtr)(((Int64)NtHeadersPtr + (Int64)Marshal.OffsetOf(typeof(IMAGE_NT_HEADERS64), "OptionalHeader") + (Int64)imageNtHeaders64.FileHeader.SizeOfOptionalHeader));
                SectionHeader = (IMAGE_SECTION_HEADER)Marshal.PtrToStructure(imageSectionPtr, typeof(IMAGE_SECTION_HEADER));
                wNumberOfSections = imageNtHeaders64.FileHeader.NumberOfSections;
            }
            else
            {
                imageSectionPtr = (IntPtr)(((Int64)NtHeadersPtr + (Int64)Marshal.OffsetOf(typeof(IMAGE_NT_HEADERS32), "OptionalHeader") + (Int64)imageNtHeaders32.FileHeader.SizeOfOptionalHeader));
                SectionHeader = (IMAGE_SECTION_HEADER)Marshal.PtrToStructure(imageSectionPtr, typeof(IMAGE_SECTION_HEADER));
                wNumberOfSections = imageNtHeaders32.FileHeader.NumberOfSections;
            }

            if (dwRva < SectionHeader.PointerToRawData)
                return (IntPtr)((UInt64)dwRva + (UInt64)PEPointer);

            for (wIndex = 0; wIndex < wNumberOfSections; wIndex++)
            {
                SectionHeader = (IMAGE_SECTION_HEADER)Marshal.PtrToStructure((IntPtr)((UInt32)imageSectionPtr + (UInt32)(sizeOfSectionHeader * (wIndex))), typeof(IMAGE_SECTION_HEADER));
                if (dwRva >= SectionHeader.VirtualAddress && dwRva < (SectionHeader.VirtualAddress + SectionHeader.SizeOfRawData))
                    return (IntPtr)((UInt64)(dwRva - SectionHeader.VirtualAddress + SectionHeader.PointerToRawData) + (UInt64)PEPointer);
            }

            return IntPtr.Zero;
        }

        public static unsafe bool Is64BitDLL(byte[] dllBytes)
        {
            bool is64Bit = false;

            GCHandle scHandle = GCHandle.Alloc(dllBytes, GCHandleType.Pinned);
            IntPtr scPointer = scHandle.AddrOfPinnedObject();

            Int32 headerOffset = Marshal.ReadInt32(scPointer, 60);
            UInt16 magic = (UInt16)Marshal.ReadInt16(scPointer, headerOffset + 4);

            if (magic == (UInt16)512 || magic == (UInt16)34404)
                is64Bit = true;

            scHandle.Free();

            return is64Bit;
        }

        public static unsafe IntPtr GetProcAddressR(IntPtr PEPointer, string functionName)
        {
            bool is64Bit = false;

            IMAGE_DOS_HEADER dosHeader = (IMAGE_DOS_HEADER)Marshal.PtrToStructure(PEPointer, typeof(IMAGE_DOS_HEADER));

            IntPtr NtHeadersPtr = (IntPtr)((UInt64)PEPointer + (UInt64)dosHeader.e_lfanew);

            var imageNtHeaders64 = (IMAGE_NT_HEADERS64)Marshal.PtrToStructure(NtHeadersPtr, typeof(IMAGE_NT_HEADERS64));
            var imageNtHeaders32 = (IMAGE_NT_HEADERS32)Marshal.PtrToStructure(NtHeadersPtr, typeof(IMAGE_NT_HEADERS32));

            if (!imageNtHeaders64.isValid)
                throw new ApplicationException("Invalid IMAGE_NT_HEADER signature.");

            if (imageNtHeaders64.OptionalHeader.Magic == MagicType.IMAGE_NT_OPTIONAL_HDR64_MAGIC) is64Bit = true;

            IntPtr ExportTablePtr;

            if (is64Bit)
            {
                if ((imageNtHeaders64.FileHeader.Characteristics & 0x2000) != 0x2000)
                    throw new ApplicationException("File is not a DLL, Exiting.");

                ExportTablePtr = (IntPtr)((UInt64)PEPointer + (UInt64)imageNtHeaders64.OptionalHeader.ExportTable.VirtualAddress);
            }
            else
            {
                if ((imageNtHeaders32.FileHeader.Characteristics & 0x2000) != 0x2000)
                    throw new ApplicationException("File is not a DLL, Exiting.");

                ExportTablePtr = (IntPtr)((UInt64)PEPointer + (UInt64)imageNtHeaders32.OptionalHeader.ExportTable.VirtualAddress);
            }

            IMAGE_EXPORT_DIRECTORY ExportTable = (IMAGE_EXPORT_DIRECTORY)Marshal.PtrToStructure(ExportTablePtr, typeof(IMAGE_EXPORT_DIRECTORY));

            for (int i = 0; i < ExportTable.NumberOfNames; i++)
            {
                IntPtr NameOffsetPtr = (IntPtr)((ulong)PEPointer + (ulong)ExportTable.AddressOfNames + (ulong)(i * Marshal.SizeOf(typeof(UInt32))));
                IntPtr NamePtr = (IntPtr)((ulong)PEPointer + (UInt32)Marshal.PtrToStructure(NameOffsetPtr, typeof(UInt32)));

                string Name = Marshal.PtrToStringAnsi(NamePtr);

                if (Name.Contains(functionName))
                {
                    IntPtr AddressOfFunctions = (IntPtr)((ulong)PEPointer + (ulong)ExportTable.AddressOfFunctions);
                    IntPtr OrdinalRvaPtr = (IntPtr)((ulong)PEPointer + (ulong)(ExportTable.AddressOfNameOrdinals + (i * Marshal.SizeOf(typeof(UInt16)))));
                    UInt16 FuncIndex = (UInt16)Marshal.PtrToStructure(OrdinalRvaPtr, typeof(UInt16));
                    IntPtr FuncOffsetLocation = (IntPtr)((ulong)AddressOfFunctions + (ulong)(FuncIndex * Marshal.SizeOf(typeof(UInt32))));
                    IntPtr FuncLocationInMemory = (IntPtr)((ulong)PEPointer + (UInt32)Marshal.PtrToStructure(FuncOffsetLocation, typeof(UInt32)));

                    return FuncLocationInMemory;
                }
            }
            return IntPtr.Zero;
        }
    }
}
