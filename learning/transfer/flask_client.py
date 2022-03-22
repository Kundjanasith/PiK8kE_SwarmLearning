import requests
import sys 

ip = sys.argv[1]
filepath = sys.argv[2]

with open(filepath, 'rb') as f:
    requests.post(ip, data=f)