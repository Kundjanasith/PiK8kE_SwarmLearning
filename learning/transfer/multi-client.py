import socket
import sys 

SERVER = sys.argv[1]
PORT = 19191
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))

node = config['network']['node']
list_config_ip = list(config['network'])
list_config_ip.pop(0)
ipx = list_config_ip[int(node)-1]

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 1024
filename = sys.argv[2]
filesize = os.path.getsize(filename)

client.send(f"{ipx}{SEPARATOR}{filename}{SEPARATOR}{filesize}".encode())
with open(filename, "rb") as f:
    while True:
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            break
        client.sendall(bytes_read)
client.close()