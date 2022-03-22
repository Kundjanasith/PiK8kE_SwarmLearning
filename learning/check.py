import socket
from colorama import Fore
import configparser

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


list_config_ip = list(config['network'])
list_config_ip.pop(0)


for i in list_config_ip:
   ip = config['network'][i]
   print(ip)
   if isOpen(ip,22):
      print(Fore.GREEN,ip,'is up!')
   else:
      print(Fore.RED,ip,'is down!')
