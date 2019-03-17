import socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = input("Enter Server IP Address")
port = 12345
x = input("Enter file name : ")
server_socket.connect((host,port))
name = server_socket.recv(1024).decode()
name = name.split('.')[-1]
name = x+'.'+name

f = open(name,'wb')
while True :
    c_msg = server_socket.recv(1024)
    if c_msg == 'EOF'.encode() : 
        f.close()
        server_socket.close()
        break
    f.write(c_msg)


