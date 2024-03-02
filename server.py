import  socket

# socket.AF_INET= ipv4
# socket.SOCK_STREAM= TCP connection
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("socket created")

s.bind((socket.gethostname(), 1234))
# 5 queue load
s.listen(5)

while True:
    clientSocket, address=s.accept()
    print(f"Connection from {address} has been established!")
    clientSocket.send(bytes("Welcome to the server", 'utf-8'))
    client_msg=clientSocket.recv(1024).decode()
    print(client_msg)

    clientSocket.close()