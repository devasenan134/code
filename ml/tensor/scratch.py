# import socket
#
#
# mysoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysoc.connect(("data.pr4e.org", 80))
#
# cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
# mysoc.send(cmd)
#
# while True:
#     data = mysoc.recv(512)
#     if len(data) < 1:
#         break
#     print(data.decode())
#
# mysoc.close()


import urllib.request, urllib.parse, urllib.error
import json

url = input(">>")
fhand = urllib.request.urlopen(url)
data = """"""
tot = 0

for line in fhand:
    # print(line.decode().strip())
    data += line.decode()

info = json.loads(data)
print('User count:', len(info["comments"]))

userList = info["comments"]

for user in userList:
    tot += user["count"]

print("Sum:", tot)
