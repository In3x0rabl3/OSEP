import random
import struct
import sys

print

decoder_stub =  '\x31\xc0\x31\xdb\x31\xc9\x31\xd2'
decoder_stub += '\xb2\x45\xeb\x1f\x5e\x8d\x3e\x8a'
decoder_stub += '\x1c\x0f\x88\xdf\x88\xd0\x30\xd8'
decoder_stub += '\x74\x16\x66\x8b\x44\x0f\x01\x66'
decoder_stub += '\x31\xd8\x66\x89\x07\x41\x8d\x7f'
decoder_stub += '\x02\xeb\xe4\xe8\xdc\xff\xff\xff'

def find_valid_xor_byte(bytes, bad_chars):
    for i in random.sample(range(1, 256), 255):
        matched_a_byte = False

        # Check if the potential XOR byte matches any of the bad chars.
        for byte in bad_chars:
            if i == int(byte.encode('hex'), 16):
                matched_a_byte = True
                break

        for byte in bytes:
            # Check that the current byte is not the same as the
            # XOR byte, otherwise null bytes will be produced.
            if i == int(byte.encode('hex'), 16):
                matched_a_byte = True
                break

            # Check if XORing using the current byte would result in any
            # bad chars ending up in the final shellcode.
            for bad_byte in bad_chars:
                if struct.pack('B', int(byte.encode('hex'), 16) ^ i) == bad_byte:
                    matched_a_byte = True
                    break

            # If a bad char would be encountered when XORing with the
            # current XOR byte, skip continuing checking the bytes and
            # try the next candidate.
            if matched_a_byte:
                break

        if not matched_a_byte:
            return i

if len(sys.argv) < 2:
    print 'Usage: python {name} [shellcode] [optional: bad_chars]'.format(name = sys.argv[0])
    exit(1)

bad_chars = '\x0a\x00\x0d'
if len(sys.argv) > 2:
    bad_chars = sys.argv[2].replace('\\x', '').decode('hex')

shellcode = sys.argv[1].replace('\\x', '').decode('hex')
encoded = []
chunk_no = 0

# Issue a warning if any of the bad chars are found within the decoder itself.
stub_has_bad_char = False

for char in bad_chars:
    for byte in decoder_stub:
        if char == byte:
            stub_has_bad_char = True
            break

    if stub_has_bad_char:
        break

if stub_has_bad_char:
    print '\033[93m[!]\033[00m One or more bad chars were found in the decoder stub\n'

# Loop through the shellcode in 2 byte chunks and find a byte to XOR them
# with, each time prepending the XOR byte to the encoded chunk.
while len(shellcode) > 0:
    chunk_no += 1
    xor_byte = 0
    chunk = shellcode[0:2]

    xor_byte = find_valid_xor_byte(chunk, bad_chars)

    if xor_byte == 0:
        print 'Failed to find a valid XOR byte to encode chunk {chunk_no}'.format(chunk_no = chunk_no)
        exit(2)

    encoded.append(struct.pack('B', xor_byte))
    for i in range(0, 2):
        if i < len(chunk):
            encoded.append(struct.pack('B', (int(chunk[i].encode('hex'), 16) ^ xor_byte)))
        else:
            encoded.append(struct.pack('B', xor_byte))

    shellcode = shellcode[2::]

# Find a byte that does not appear in the decoder stub or the encoded
# shellcode which can be used as an EOF delimiter.
xor_byte = find_valid_xor_byte(decoder_stub.join(encoded), bad_chars)

if xor_byte == 0:
    print 'Failed to find a valid XOR byte for the delimiter'
    exit(3)

decoder_stub = decoder_stub.replace('\x45', struct.pack('B', xor_byte))
encoded.append(struct.pack('B', xor_byte))

# Join the decoder and encoded payload together and output to screen.
final_shellcode = ''.join('\\x' + byte.encode('hex') for byte in decoder_stub)
final_shellcode += ''.join('\\x' + byte.encode('hex') for byte in encoded)
print final_shellcode
