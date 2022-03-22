import requests
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


filepath = sys.argv[2]

fx = filepath.split('/')
fx = fx[len(fx)-1]
with open(filepath, 'rb') as f:
    requests.post('http://'+ip+':19191/files/'+ipx+'-'+fx, data=f)