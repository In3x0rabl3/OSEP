# Dropper

## Version 1.0

* Drops and launches plain executable files.

## Version 2.0

* Encodes payloads using XOR and/or Base64.
* Launches injected DLLs.
* Drops random-named files.

## Version 3.0

* Project converted to DLL.
* Dead-imports converted into dead-exports.
* Most static imports converted to dynamic imports.

## Version 4.0
* Dropping to its own memory rather than to the filesystem.
* Launch via the RunPE method.

## Version 5.0
* Dropping one payload to the disk an another in memory.
* Replacing the memory of the process launched from the disk payload.
