import urllib.request
import time
import random

def send_temps():
    while True:
        temp = round(random.randint(-100.0, 100.0), 2)
        target = "http://127.0.0.1:8080/store?data=" + str(temp)
        
        response = urllib.request.urlopen(target)
        
        time.sleep(1)

if __name__ == "__main__":
    send_temps()
