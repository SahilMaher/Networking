import socket
host='172.21.26.104'
port=8080

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((host,port))
msg=s.recv(1024).decode()
print(f'Received from server: {msg}')

while True:
    massage=input("Enter massage")
    s.sendall(massage.encode())
    data=s.recv(1024).decode()
     
    print('Received response:{}',format(data))
    if(data=='by'):
        break
   
print('closing connection')
s.close()