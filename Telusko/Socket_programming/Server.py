
import socket

myserver = socket.socket()  # socket created
print("socket created")

myserver.bind(('localhost', 9999))    # bind with random port, IP=localhost & port=9999 defined

myserver.listen()   # listening to accept connection from client
print("Waiting for the connection")

# You need to start server first and then start client

myclient, addr = myserver.accept()  # Accept the connection from client
print("Connected with ", addr)

# myclient.send("Hello Avisek")
myclient.send(bytes("Hello Avisek", "utf-8"))   # Need send data in byte & need to mention format 'utf-8'


# # We can keep socket running to accept multiple client req by while loop
# while True:
#     myclient, addr = myserver.accept()  # Accept the connection from client
#     print("Connected with ", addr)
#
#     myclient.send(bytes("Hello Avisek", "utf-8"))   # Need send data in byte & need to mention format 'utf-8'









