import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 12345 # The port used by the 
shell = 'A'

s = socket.socket()
s.connect((HOST, PORT))
print("connected...")
s.send(shell.encode())
print('sent ...')

data = s.recv(2048)
#s.close()
#print('Received', data.decode('utf-8'))