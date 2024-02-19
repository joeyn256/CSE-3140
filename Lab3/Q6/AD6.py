import subprocess
import os
import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# get private key data
with open('d.key', 'rb') as f:
    private_key = RSA.import_key(f.read())

# use standrad iv from before
iv = b'0123456789ABCDEF'

with open(sys.argv[1], 'rb') as f:
    encrypted_data = f.read()

# split the unique ID into the aes key and respective cybertext
encrypted_aes_key = encrypted_data[:private_key.size_in_bytes()]
ciphertext = encrypted_data[private_key.size_in_bytes():]

# decrypt to get respective AES key with the private key
cipher_rsa = PKCS1_OAEP.new(private_key)
aes_key = cipher_rsa.decrypt(encrypted_aes_key)
aes_key_string = aes_key.hex() #make the binary representation a string so it can be passed as an argument in D6.py
print(f"{sys.argv[1]}'s decryption key is: {aes_key_string}")

