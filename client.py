""" 
client.py


sources used:
https://realpython.com/python-sockets/
https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client
https://www.tutorialspoint.com/python/python_command_line_arguments.htm
https://stackoverflow.com/questions/15753701/how-can-i-pass-a-list-as-a-command-line-argument-with-argparse
https://www.geeksforgeeks.org/python-convert-string-to-bytes/
https://www.tutorialspoint.com/python/os_stat.htm
https://docs.python.org/3/library/socket.html#functions
https://www.geeksforgeeks.org/multithreading-python-set-1/
https://stackoverflow.com/questions/68425239/how-to-handle-multithreading-with-sockets-in-python
https://stackoverflow.com/questions/7174927/when-does-socket-recvrecv-size-return
"""

import socket
import argparse
import threading
import os

"""
states: INIT, SENT_OK
INIT      thread is waiting to get XFER from client
          data:   XFER <fname> <flen> string
SENT_OK   data    bytes of the file
if error: break out of loop, which closes sock

Put \n after every sendall() string sent, except when sending file bytes

"""

def client():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("host")
        parser.add_argument("port")
        parser.add_argument("files", nargs='+') # '+' 1 or more args
        args = parser.parse_args()
    except:
        print("The following arguments are required: host, port, file(s).\nTry again")
        return 0

    HOST = args.host
    PORT = int(args.port)
    files = args.files

    cthreads = []
    for fi in files:
        ct = threading.Thread(target=xfer, args=(HOST, PORT, fi))
        ct.start()
        cthreads.append(ct)
    
    for ct in cthreads:
        ct.join()

def xfer(HOST, PORT, fi):
    csocket = socket.socket()
    csocket.connect((HOST, PORT))

    # Send initial message, XFER <filename> <file-length>
    size = os.stat(fi).st_size
    print(f"Sending {fi}: length {size}")
    msg = str("XFER {} {}".format(fi, size))
    csocket.send(msg.encode())
    # Wait for server confirmation
    reply = csocket.recv(1024).decode()
    if reply != "OK":
        print(reply)
        csocket.close()
        return 0
    print(f"Got OK from server-- now sending {fi}")

    # Send file as bytes
    try:
        f = open(fi, 'rb')
        data = f.read()
        csocket.sendall(data)
        f.close()
    except:
        print(f"Failed to send {fi}")
        f.close()
        csocket.close()
    
    # Wait for server to finish writing
    print(f"Finished sending {fi}. Waiting for server to finish copying")
    reply = csocket.recv(1024).decode()
    if reply != "SUCCESS":
        print(reply)
    else:
        print(f"Successfully transfered {fi}")
    csocket.close()

if __name__ == '__main__':
  client()