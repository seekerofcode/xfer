""" 
client.py


sources used:
https://realpython.com/python-sockets/
https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client
https://www.tutorialspoint.com/python/python_command_line_arguments.htm
https://stackoverflow.com/questions/15753701/how-can-i-pass-a-list-as-a-command-line-argument-with-argparse
"""

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
Use 'if not data: ' to determine if client has closed the socket

"""

def client():
    parser = argparse.ArgumentParser()

    parser.add_argument("host")
    parser.add_argument("port", nargs='?', default=9999)
    parser.add_argument("files", nargs='+')

    args = parser.parse_args()
    HOST = args.host
    PORT = args.port
    files = args.files

    csocket = socket.socket()
    csocket.connect((HOST, PORT))

    for f in files:
        csocket.sendall(bytes(f,'utf-8'))
        csocket.sendall(b" \n")
    data = csocket.recv(1024)

    print("Received: " + str(data))

    csocket.close()

if __name__ == '__main__':
  client()