from Crypto.Cipher import AES

input_file = 'Encrypted4'
output_file = 'Encrypted4_Decrypted.txt'

with open(input_file, 'rb') as f:
    iv = f.read(16)
    ciphertext = f.read()

key = b'c\x83a\xb1\xdc\x15\xffE\xe0{\x06u\xc31\x82@'
cipher = AES.new(key, AES.MODE_CBC, iv=iv)

with open(output_file, 'wb') as f:
    plaintext = cipher.decrypt(ciphertext)
    f.write(plaintext)

#pleasurableness18$