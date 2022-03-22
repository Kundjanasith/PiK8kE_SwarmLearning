import configparser, os, socket, time
from datetime import datetime
import subprocess

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
        active_ip = []
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
                active_ip.append(ip)
                # break
            else:
                print(ip,'is down!')
        # if res == 1:
        #     print('P2P')
        #     break
        if res == len(list_config_ip):
            print('P2P')
            break
    return active_ip

NUM_OF_ROUNDS = int(config['learning']['num_of_rounds'])

subprocess.Popen(['python3','./transfer/flask_server.py'], close_fds=True)

for i in range(NUM_OF_ROUNDS):
    os.system('rm -rf ./transfer/models/*')
    print('Communication round: #',i)
    active_ip = allConnected()
    os.system('python3 client/train.py '+str(i))
    while not os.path.exists('./client/models/round_'+str(i+1)+'.h5'):
        print('waiting local model')
        time.sleep(1)
    time.sleep(10) #Delay for storing the local model
    for ip in active_ip:
        os.system('python3 ./transfer/flask_client.py '+ip+' ./client/models/round_'+str(i+1)+'.h5')
    for j in range(1,len(active_ip)+1):
        if j == int(config['network']['node']):
            continue
        while not os.path.exists('./transfer/models/worker%02d_ip-round_%d.h5'%(j,i+1)):
            print('waiting local model from worker %02d'%(j))
            time.sleep(1)
    time.sleep(10) #Delay for storing the local model
    os.system('python3 server/aggregate.py '+str(i+1))
    time.sleep(100)
        




    
