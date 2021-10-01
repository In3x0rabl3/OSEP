# Marcus Botacin
# Patch PE headers
# Used to make the dropper to look like the ntdll
# Use python3

import sys  # receives argv
import lief # handles PE files

# Open the dropper file
dropper = lief.parse(sys.argv[1])
# Open the ntdll fiile
ntdll = lief.parse(sys.argv[2])

# Copy timestamps and other stuff
dropper.header.time_date_stamps = ntdll.header.time_date_stamps
dropper.optional_header.major_linker_version = ntdll.optional_header.major_linker_version
dropper.optional_header.minor_linker_version = ntdll.optional_header.minor_linker_version
dropper.optional_header.major_image_version = ntdll.optional_header.major_image_version
dropper.optional_header.minor_image_version = ntdll.optional_header.minor_image_version
dropper.optional_header.major_operating_system_version = ntdll.optional_header.major_operating_system_version
dropper.optional_header.minor_operating_system_version = ntdll.optional_header.minor_operating_system_version
dropper.optional_header.major_subsystem_version = ntdll.optional_header.major_subsystem_version
dropper.optional_header.minor_subsystem_version = ntdll.optional_header.minor_subsystem_version

# Create a new binary with the modifications
builder = lief.PE.Builder(dropper)
builder.build()
builder.write(sys.argv[1]+".patched")

