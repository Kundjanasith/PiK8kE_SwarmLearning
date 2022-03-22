import socket, threading, os

class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print("New connection added: ", clientAddress)
    def run(self):
        print("Connection from : ", clientAddress)
        #self.csocket.send(bytes("Hi, This is from Server..",'utf-8'))
        SEPARATOR = "<SEPARATOR>"
        received = self.csocket.recv(2048).decode()
        ipx, filename, filesize = received.split(SEPARATOR)
        filename = os.path.basename(filename)
        filesize = int(filesize)
        with open('./transfer/models/'+ipx+'-'+filename, "wb") as f:
            while True:
                bytes_read = self.csocket.recv(2048)
                if not bytes_read:    
                    break
                f.write(bytes_read)
        self.csocket.close()

LOCALHOST = "0.0.0.0"
PORT = 19191
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Server started")
print("Waiting for client request..")
while True:
    server.listen(1)
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()
