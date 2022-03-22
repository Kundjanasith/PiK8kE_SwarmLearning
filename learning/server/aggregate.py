import sys, configparser, glob
import model
import numpy as np

config = configparser.ConfigParser()
config.read('../config.ini')
print(config.sections())

num_of_round = sys.argv[1]

local_model = model.init()
local_model.load_weights('./client/models/round_'+str(num_of_round)+'.h5')

global_models = []
node = config['network']['node']
list_config_ip = list(config['network'])
list_config_ip.pop(0)
list_config_ip.pop(int(node)-1)
NUM_NODES = len(list_config_ip)
# NUM_NODES = 2
# NUM_NODES = NUM_NODES - 1

while True:
    if len(glob.glob('./transfer/models/*-round_'+str(num_of_round)+'.h5')) != NUM_NODES:
        print('Waiting . . .')
    else:
        break 

for i in glob.glob('./transfer/models/*-round_'+str(num_of_round)+'.h5'):
    global_model = model.init()
    global_model.load_weights(i)
    global_models.append(global_model)

def getLayerIndexByName(model, layername):
    for idx, layer in enumerate(model.layers):
        if layer.name == layername:
            return idx

for l in local_model.layers:
    l_idx = getLayerIndexByName(local_model, l.name)
    w_arr = []
    for w_idx in range(len(local_model.get_layer(index=l_idx).get_weights())):
        ww = []
        local_weights = local_model.get_layer(index=l_idx).get_weights()[w_idx]
        ww.append(local_weights)
        for g in global_models:
            g_weights = g.get_layer(index=l_idx).get_weights()[w_idx]
            ww.append(g_weights)
        ww = np.array(ww)
        ww = np.mean(ww,axis=0)
        w_arr.append(ww)
    local_model.get_layer(index=l_idx).set_weights(w_arr)

local_model.save_weights('./server/models/round_'+str(num_of_round)+'.h5')





