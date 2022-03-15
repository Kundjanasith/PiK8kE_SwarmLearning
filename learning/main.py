import configparser, os, socket, time
from datetime import datetime

config = configparser.ConfigParser()
config.read('../config.ini')
print(config.sections())

def isOpen(ip,port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      s.connect((ip, int(port)))
      s.shutdown(2)
      return True
   except:
      return False

def allConnected():
    node = config['network']['node']
    list_config_ip = list(config['network'])
    list_config_ip.pop(0)
    list_config_ip.pop(int(node)-1)
    
    while True:
        time.sleep(10)
        dateTimeObj = datetime.now()
        print(dateTimeObj,'Retry . . .')
        res = 0
        for i in list_config_ip:
            ip = config['network'][i]
            response = isOpen(ip,19190)
            if response:
                print(ip,'is up!')
                res = res + 1
            else:
                print(ip,'is down!')
        if res == len(list_config_ip):
            break

NUM_OF_ROUNDS = int(config['learning']['num_of_rounds'])

for i in range(NUM_OF_ROUNDS):
    allConnected()
    break
        




    
