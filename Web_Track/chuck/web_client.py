'''
from socket import *

mysoc  = socket(AF_INET, SOCK_STREAM)
mysoc.connect(('localhost', 9000))

cmd = 'GET http://127.0.0.1/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysoc.send(cmd)

while True:
    data = mysoc.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

mysoc.close()
'''

# even simpler version
from urllib.request import *

fhand = urlopen('http://localhost:9000/romeo.txt')
for line in fhand:
    print(line.decode().strip())
