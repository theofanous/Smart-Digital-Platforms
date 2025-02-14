import os
from flask import Flask
from flask import request

from datetime import datetime

username = os.getenv("USER", "default_user")
app = Flask(__name__)

@app.route(f'/now_{username}')
def hello() :
	now = datetime.now()
	time = now.strftime("%H:%M:%S")
	return "it is "+time

if __name__ =='__main__':
   app.run(host='0.0.0.0', port=8080)
