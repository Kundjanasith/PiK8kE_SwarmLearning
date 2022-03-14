import requests
import configparser

def internet_on(ip):
    url = 'http://'+ip+':19191'
    timeout = 5
    result = None
    try:
        request = requests.get(url, timeout=timeout)
        result = 'Connected'
    except (requests.ConnectionError, requests.Timeout) as exception:
        result = 'Not Connected'
    return result

config = configparser.ConfigParser()
config.read('../config.ini')
print(config.sections())

node = config['network']['node']
list_config_ip = list(config['network'])
list_config_ip.pop(0)
list_config_ip.pop(int(node)-1)
for i in list_config_ip:
    ip = config['network'][i]
    print(ip,internet_on(ip))
    
