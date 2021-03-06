import socket
import tqdm
import os
import sys 
import configparser

config = configparser.ConfigParser()
config.read('../config.ini')
print(config.sections())

ip = sys.argv[1]
node = config['network']['node']
list_config_ip = list(config['network'])
list_config_ip.pop(0)
ipx = list_config_ip[int(node)-1]

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 # send 4096 bytes each time step

# the ip address or hostname of the server, the receiver
host = ip
# the port, let's use 5001
port = 19191
# the name of file we want to send, make sure it exists
filename = sys.argv[2]
# get the file size
filesize = os.path.getsize(filename)

# create the client socket
s = socket.socket()

print(f"[+] Connecting from {ipx} to {host}:{port}")
s.connect((host, port))
print("[+] Connected.")

# send the filename and filesize
s.send(f"{ipx}{SEPARATOR}{filename}{SEPARATOR}{filesize}".encode())

# start sending the file
progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "rb") as f:
    while True:
        # read the bytes from the file
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            # file transmitting is done
            break
        # we use sendall to assure transimission in 
        # busy networks
        s.sendall(bytes_read)
        # update the progress bar
        progress.update(len(bytes_read))
# close the socket
s.close()