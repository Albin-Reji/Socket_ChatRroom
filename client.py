import  socket
c=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

c.connect((socket.gethostname(), 1234))
msg=c.recv(1024)
c.send(bytes(f'Succesfully Connected with {socket.gethostname()}', 'utf-8'))
print(msg.decode())







# c=socket.socket()
#
# c.connect(('192.168.43.194', 9999))
# name=input("enter your name: ")
#
# c.send(bytes(name, 'utf-8'))
#
# print(c.recv(1024).decode())