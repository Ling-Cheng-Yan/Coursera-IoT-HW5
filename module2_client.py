import socket
import sys

try:
    ms = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print("Failed to create socket")
    sys.exit()

try:
    host = socket.gethostbyname("www.google.com")
except socket.gaierror:
    print("Failed to get host")
    sys.exit()

ms.connect((host, 80))

try:
    ms.sendall(b"Hello world!!")
except socket.error:
    print("Failed to send")
    sys.exit()

data = ms.recv(1000)
print(data)
ms.close()
