from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

# Generating an asymmetric key pair
key = RSA.generate(2048)
private_key = key.export_key()
file_out = open("private.pem", "wb")
file_out.write(private_key)
file_out.close()

public_key = key.publickey().export_key()
file_out = open("public.pem", "wb")
file_out.write(public_key)
file_out.close()


# Encrypting data using RSA
with open('text.txt', 'rb') as fo:
    message = fo.read()
file_out = open("encrypted_data.bin", "wb")

recipient_key = RSA.import_key(open("public.pem").read())
session_key = get_random_bytes(16)

# Encrypt the key with the public RSA key
cipher_rsa = PKCS1_OAEP.new(recipient_key)
enc_session_key = cipher_rsa.encrypt(session_key)

# Encrypt the data with the AES key
cipher_aes = AES.new(session_key, AES.MODE_EAX)
ciphertext, tag = cipher_aes.encrypt_and_digest(message)
[file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext)]
file_out.close()


# Decrypting data using RSA
file_in = open("encrypted_data.bin", "rb")

private_key = RSA.import_key(open("private.pem").read())

enc_session_key, nonce, tag, ciphertext = \
   [file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1)]

# Decrypt the key with the private RSA key
cipher_rsa = PKCS1_OAEP.new(private_key)
session_key = cipher_rsa.decrypt(enc_session_key)

# Decrypt the data with the AES key
cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
data = cipher_aes.decrypt_and_verify(ciphertext, tag)
print(data.decode("utf-8"))