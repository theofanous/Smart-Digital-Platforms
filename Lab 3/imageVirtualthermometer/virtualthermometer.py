import urllib.request
import time
import random

def send_temps():
    while True:
        
        target = f'http://thermo_server:8080/store?data={str(random.sample(range(-10, 30),1)[0])}'
        
        response = urllib.request.urlopen(target)
        
        time.sleep(1)

if __name__ == "__main__":
    send_temps()
