import socket

myclient = socket.socket()  # socket created

myclient.connect(('localhost', 9999))  # Need to define IP & Port number of server

# print(myclient.recv(1024))  # output = b'Hello Avisek' which is in byte format
print(myclient.recv(1024).decode())  # to print in str format need to add decode()
