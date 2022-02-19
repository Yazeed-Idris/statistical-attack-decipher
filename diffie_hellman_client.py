import diffie_hellman
import socket                   # Import socket module

# Alice will choose the private key 4
private_key = 4
x = diffie_hellman.compute_key(private_key)

# client.py
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)             # Create a socket object
s.connect((socket.gethostname(), 1234))
print('Connected to server')
print(f'Sending generated key {x}')
s.send(str(x).encode('utf-8'))

while True:
    message = s.recv(1024)
    if len(message) <= 0:
        break
    y = int(message.decode('utf-8'))
    print(f'Received data y={y}')

shared_key = diffie_hellman.compute_shared_key(y, private_key)
print(f'The shared key is {shared_key}')
