from Crypto.PublicKey import RSA

# Generate new RSA key pair
key = RSA.generate(2048)

# Save public key to 'e.key' in PEM format
with open('e.key', 'wb') as f:
    f.write(key.publickey().export_key('PEM'))

# Save private key to 'd.key' in PEM format
with open('d.key', 'wb') as f:
    f.write(key.export_key('PEM'))