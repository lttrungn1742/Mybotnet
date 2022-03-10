FROM python:latest
RUN apt update && apt install tcpdump -y
RUN pip install flask
COPY app.py /server.py

CMD ["python3","/server.py"]