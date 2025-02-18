FROM ubuntu
COPY virtualthermometer.py /virtualthermometer.py
RUN apt-get update
RUN apt-get install python3 -y
CMD ["python3", "/virtualthermometer.py"]
