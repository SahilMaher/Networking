import socket
host='localhost'
port=8093
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_socket.bind((host,port))
server_socket.listen(1)
print(f"Listing on {host}:{port}")
conn,address=server_socket.accept()
print(f"Connection establish with {address}")
message="welcome to the server"
conn.send(message.encode())
data=conn.recv(1024).decode()
print(f"Recived from clint:{data}")
conn.close()