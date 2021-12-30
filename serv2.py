import socket
import sys

HOST = ''  # Standard loopback interface address (localhost)
PORT = 6666 # Port to listen on (non-privileged ports are > 1023)

#player = socket.socket(AF_INET,socket.SOCK_STREAM)
#ip = socket.gethostbyname('www.google.com')


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
   # print(ip)
    #print(sys.argv[0])
    print(f"lestinening On {PORT}")
    
    conn, addr = s.accept()
   # print(conn.recv(1024))
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)