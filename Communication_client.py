
import socket
host='localhost'
port=8092
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((host,port))
print('connected to {}:{}'.format(host,port))
while True:
    massage=input("Enter massage")
    client_socket.sendall(massage.encode())
    data=client_socket.recv(1024).decode()
    print('Received response:{}',format(data))
print('closing connection')
client_socket.close()