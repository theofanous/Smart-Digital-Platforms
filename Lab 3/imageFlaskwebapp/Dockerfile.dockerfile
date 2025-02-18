FROM ubuntu
COPY flaskwebapp.py /flaskwebapp.py
RUN apt-get update
RUN apt-get install python3 python3-flask -y
CMD ["python3", "/flaskwebapp.py"]
