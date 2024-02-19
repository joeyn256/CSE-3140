import Crypto
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15 as pk
from Crypto.Hash import SHA256 as sh
import os


f = open('Q3pk.pem', 'r')
key = RSA.import_key(f.read())

files = os.listdir('/home/cse/Lab3/Q3files')
exe_list = []
for i in files:
    if i[-3::] == 'exe':
        exe_list.append(i)
    else:
        pass

while exe_list:
    exe = exe_list.pop()
    signer = pk.new(key)
    hasher = sh.new()
    f = open(exe, 'rb')
    hasher.update(f.read())
    f = open(exe + '.sign', 'rb')
    try:
        signer.verify(hasher, f.read())
        print(exe)
    except ValueError:
        pass


#lorgnette.exe