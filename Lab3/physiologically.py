import subprocess
import os

result = subprocess.getoutput('ls')
result = result.split('\n')
for i in result:
    hash_i = subprocess.getoutput('sha256sum -t ' + i)
    t = hash_i.split(" ")
    if t[0]  == 'a497bc8938ecb2258c557006a5f925b599381d0e5c3d98f53a88639ea5c9cb38':
        print(i)