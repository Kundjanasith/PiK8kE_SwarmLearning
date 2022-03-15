import configparser, os

def internet_on(ip):
    hostname = ip
    response = os.system("ping -c 1 " + hostname)   
    return response

def isOpen(ip,port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      s.connect((ip, int(port)))
      s.shutdown(2)
      return True
   except:
      return False

config = configparser.ConfigParser()
config.read('../config.ini')
print(config.sections())

node = config['network']['node']
list_config_ip = list(config['network'])
list_config_ip.pop(0)
list_config_ip.pop(int(node)-1)
for i in list_config_ip:
    ip = config['network'][i]
    response = isOpen(ip,19190)
    if response:
        print(ip,'is up!')
    else:
        print(ip,'is down!')
    
