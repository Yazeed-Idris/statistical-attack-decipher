import diffie_hellman
import socket  # Import socket module

# Bob will choose the private key 3
private_key = 3
y = diffie_hellman.compute_key(private_key)

# server.py
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

print('Server listening on port: 1234')
while True:
    clientsocket, address = s.accept()
    print(f'Connection from {address} has been established!')
    print(f'Receiving data...')
    x = int(clientsocket.recv(1024).decode('utf-8'))
    print(f'Received x= {x}')
    print(f'Sending generated key {y}')
    clientsocket.send(str(y).encode('utf-8'))
    clientsocket.close()
    break
shared_key = diffie_hellman.compute_shared_key(x, private_key)
print(f'The shared key is {shared_key}')

