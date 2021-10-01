#!/usr/bin/env python

import encoder
import preamble
import sys

if len(sys.argv) != 3:
    print 'Usage: main.py <shellcode file> <pointer to shellcode>'
    print "Pointer to shellcode should be an expression that is the address of the start of the shellcode in the victim's address space"
    print 'Example: main.py shellcode.bin rcx'
    print 'Example: main.py shellcode.bin [rsp+-8]'
    print 'Example: main.py shellcode.bin 0x0123456789abcdef'
    print 'Example: main.py shellcode.bin rbp+5'
    sys.exit(1)

payload = open(sys.argv[1], 'rb').read()
encoded_payload = encoder.encode(payload)

shellcode_ptr = sys.argv[2]
print
print 'Encoding preamble for rdx <- %s' % (shellcode_ptr)
preamble = preamble.load_rdx(shellcode_ptr)
print preamble

print 
print 'Original length: %d' % (len(payload),)
print 'Encoded length:  %d' % (len(encoded_payload),)
print 'Preamble length: %d' % (len(preamble))
print 'Total length:    %d' % (len(preamble) + len(encoded_payload))
print
print preamble + encoded_payload
