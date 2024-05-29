# client.py

import socket
import argparse
import threading
import os

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
        if os.path.isfile(fi):
            ct = threading.Thread(target=xfer, args=(HOST, PORT, fi))
            ct.start()
            cthreads.append(ct)
        else:
            print(f"Could not find '{fi}' in current working directory")

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