from os import walk
import secrets
import threading
import requests

class HTTPPusher:
    def __init__(self, clientIP):
        self.clientID = clientIP
        try:
            r = requests.get('http://'+clientIP+'/deploy', timeout=2)
            print(r.content)
        except:
            print("Exception on client " + clientIP)


for client in secrets.clients:
    print("Connecting to " + client, flush=True)
    f = HTTPPusher(client)
