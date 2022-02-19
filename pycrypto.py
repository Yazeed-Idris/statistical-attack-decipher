from secrets import token_bytes
from Crypto.Cipher import AES

# AES Algorithm
key = token_bytes(16)
message = ''

with open('text.txt', 'rb') as fo:
    message = fo.read().decode('utf-8')

# Encrypting the message
cipher = AES.new(key, AES.MODE_EAX)
nonce = cipher.nonce
cipher_text, tag = cipher.encrypt_and_digest(message.encode('ascii'))

with open('enc.txt.aes', 'wb') as fo:
    fo.write(cipher_text)
    fo.close()

with open('enc.txt.aes', 'rb') as fo:
    file_text = fo.read()

# Decrypting the message
cipher = AES. new(key, AES.MODE_EAX, nonce=nonce)
plain_text = cipher.decrypt(file_text)

try:
    cipher.verify(tag)
    print('plain text:', plain_text.decode('ascii'))
except ValueError:
    print('Key incorrect or message corrupted')

