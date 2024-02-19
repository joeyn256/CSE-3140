import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Hash import MD5

BLOCKSIZE = 256
h = MD5.new()
count = 0

with open( 'R5.py' , 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        count = count + 1
        h.update(buf)
        buf = afile.read(BLOCKSIZE)
hf = h.digest()
key = hf


input_file = 'Encrypted5'
output_file = 'Q5a'

with open(input_file, 'rb') as f:
    iv = f.read(16)
    encrypted_data = f.read()

# Create an instance of the AES cipher with the bird key and IV
cipher = AES.new(key, AES.MODE_CBC, iv)

# Decrypt the data
decrypted_data = cipher.decrypt(encrypted_data)
decrypted_data = decrypted_data.decode()
print(decrypted_data)

# Write the decrypted data to a new file
with open('Decrypted5', 'w') as f:
    f.write(decrypted_data)