import random
import subprocess
import os

def is_prime(n):
    """
    Check if a number is prime.
    """
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_keypair(p, q):
    # n is the sum of two prime numbers multiplied by 4 (which will be information that will be given in the note)
    # n will certainly be helpful but not enough to actually be able to get the private key
    n = 4 * (p + q)
    #get phi
    phi = (p - 1) * (q - 1)
    # Choose an integer e such that e and phi(n) are coprime; This integer will be random and near impossible to crack
    # the public key will not give enough info for a user to find the private key
    e = random.randrange(1, phi)
    gcd = lambda a, b: a if not b else gcd(b, a % b)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)
    # get d, the modular inverse of e
    d = pow(e, -1, phi)
    # return public and private keypair
    return ((e, n), (d, n))

if __name__ == '__main__':
    lower = 1
    upper = 1000
    p = random.randint(lower,upper)
    q = random.randint(lower,upper)

    a = True
    b = True

    #runs until p is prime
    while a:
        if is_prime(p):
            a = False
        else:
            p = random.randint(lower,upper)
    #runs until q is prime
    while b:
        if is_prime(q):
            b = False
        else:
            q = random.randint(lower,upper)
    print(f'p = {p} and q = {q}')
    public, private = generate_keypair(p, q)
    print(f'Public key: {public}')
    print(f'Private key: {private}')


    with open('e.key', 'w') as i:
        i.write(str(public))

    with open('d.key', 'w') as j:
        j.write(str(private))