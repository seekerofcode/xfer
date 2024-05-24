# server.py

import socket
import argparse
import os

"""
states: INIT, SENT_OK
INIT      thread is waiting to get XFER from client
          data:   XFER <fname> <flen> string
SENT_OK   data    bytes of the file
if error: break out of loop, which closes sock

Put \n after every sendall() string sent, except when sending file bytes
Use os.stat() to get file size

"""

def server():
    print("Server IP: " + socket.gethostbyname(socket.gethostname()))
    HOST = socket.gethostname()
    
    parser = argparse.ArgumentParser()
    parser.add_argument("port", nargs='?', default=9999)
    args = parser.parse_args()
    PORT = args.port
    
    ssocket = socket.socket()
    ssocket.bind((HOST, PORT))
    ssocket.listen() # specify number of connections allowed?
    sock, addr = ssocket.accept()
    print("Connected to: " + str(addr))
 

    # def handle_client(sock, addr):
    with sock:
        # state = "INIT"
        while True:
            data = sock.recv(1024)
            print("Received from client: " + str(data) + "\n")
            if not data: # break & close socket if client closes connection
                print("Closing connection.")
                break
            sock.sendall(data) # echo received data
            sock.sendall(b"\n")
    
    # sock.close()

if __name__ == '__main__':
  server()
