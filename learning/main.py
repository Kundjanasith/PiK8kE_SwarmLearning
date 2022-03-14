import configparser, os

def internet_on(ip):
    hostname = ip
    response = os.system("ping -c 1 " + hostname)   
    return response

config = configparser.ConfigParser()
config.read('../config.ini')
print(config.sections())

node = config['network']['node']
list_config_ip = list(config['network'])
list_config_ip.pop(0)
list_config_ip.pop(int(node)-1)
for i in list_config_ip:
    ip = config['network'][i]
    response = internet_on(ip)
    if response == 0:
        print(ip,'is up!')
    else:
        print(ip,'is down!')
    
