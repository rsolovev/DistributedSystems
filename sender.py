import socket
import sys
import os

filename = sys.argv[1]
host_ip = sys.argv[2]
host_port = sys.argv[3]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
f = open(filename, 'rb')
l = f.read(1024)
s.connect((host_ip, int(host_port)))
s.send(bytes(filename, 'utf-8'))
resp = s.recv(1024)
if resp == b'ok':
    i = 1
    while l:
        s.send(l)
        print(f"Progress: {100 * (i * 1024 / os.path.getsize(filename))}%", flush=True)
        i += 1
        l = f.read(1024)
