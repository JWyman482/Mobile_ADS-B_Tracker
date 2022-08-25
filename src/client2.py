import socket
import time

BUFFER_SIZE = 4096
HOST = "192.168.1.34"
PORT = 5001
filename = "aircraft.json"
iterations = 100
HDR_SIZE = 5

# Create the client socket
s = socket.socket()

# Connect to receiver (server)
print(f"[+] Connecting to {HOST}:{PORT}")
s.connect((HOST, PORT))
print("[+] Connected.")

for i in range(iterations):
    
    # Receive file info on client socket
    # filesize = s.recv(BUFFER_SIZE).decode()
    filesize = s.recv(HDR_SIZE).decode()
    if filesize == '':
        break
    filesize = int(filesize)
    # print(filesize)

    # Start receiving the file from the socket
    with open(filename, "wb") as f:
        while True:
            if filesize == 0:
                break
            if filesize < BUFFER_SIZE:
                bytes_read = s.recv(filesize)
            else:
                bytes_read = s.recv(BUFFER_SIZE)
            
            if not bytes_read:
                break
                
            # Trying this
            filesize -= len(bytes_read)
            # print(filesize)
            # if filesize <= 0:

            # Write the bytes just received
            f.write(bytes_read)
        f.close()
    time.sleep(1)
s.close()