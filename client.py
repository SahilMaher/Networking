import socket
host='172.21.26.105'
port=8093

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((host,port))
msg=s.recv(1024).decode()
print(f'Received from server: {msg}')
data="Hello server!"
s.send(data.encode())
s.close()
