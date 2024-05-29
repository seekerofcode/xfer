# server.py

import socket
import argparse
import threading

"""
states: INIT, SENT_OK
INIT      thread is waiting to get XFER from client
          data:   XFER <fname> <flen> string
SENT_OK   data    bytes of the file
if error: break out of loop, which closes sock

Put \n after every sendall() string sent, except when sending file bytes

"""

def server():
    print("Server IP: " + socket.gethostbyname(socket.gethostname()))
    HOST = socket.gethostname()
    
    parser = argparse.ArgumentParser()
    parser.add_argument("port", nargs='?', default=9999) # '?' 0 or 1 args
    args = parser.parse_args()
    PORT = args.port
    
    ssocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssocket.bind((HOST, PORT))
    ssocket.listen()

    sthreads = []
    try:
        while True:
            sock, addr = ssocket.accept()
            print("Client connected from " + str(addr))
            st = threading.Thread(target=handle_client, args=(sock, addr))
            st.start()
            sthreads.append(st)
    finally:
        for st in sthreads:
            st.join()

def handle_client(sock, addr):
    with sock:
        # Get initial message, XFER <filename> <file-length>
        state = "INIT"
        data = sock.recv(1024).decode().split(" ")
        if len(data) != 3 or data[0] != "XFER":
            sock.sendall(b"badly formatted message")
            sock.close()
        print(f"Got XFER command from client: {data}")

        # Open file for writing
        file = data[1]
        size = int(data[2])
        try:
            filename = "copy_of_" + file
            ope = open(filename, "wb")
        except Exception as error:
            msg = "error when opening file '{}': {}".format(file, error)
            sock.sendall(msg.encode())
            sock.close()
        # Send back success message
        sock.sendall(b"OK")
        state = "SENT_OK"
        print(f"Ready to copy {file}-- sent OK to client")

        # Write transferred bytes into new file
        while True:
            data = sock.recv(1024)
            chunksize = len(data)
            print(f"Writing {chunksize} bytes to the file '{file}'") #: " + data)
            ope.write(data)
            
            size -= chunksize
            if size <= 0: # break & close socket if we run out of data
                break
        ope.close()
        print(f"Transfer of '{file}' complete.")
        sock.send(b"SUCCESS")
        sock.close()

if __name__ == '__main__':
  server()
