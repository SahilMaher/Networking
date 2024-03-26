import socket
host=''
port=8092
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server_socket.bind((host,port))
server_socket.listen(5)
print('server listen on {}:{}'.format(host,port))
client_socket,client_address=server_socket.accept()
print('accept connection from{}:{}'.format(client_address[0],client_address[1]))
while True:
    data=client_socket.recv(1024).decode()
    if not data:
        break
    print('Received Message:{}'.format(data))
    response=input('Enter Response')
    client_socket.sendall(response.encode())
print('closing connection')
client_socket.close()