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


# fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
#
# for line in fhand:
#        print(line.decode().strip())



from bs4 import BeautifulSoup

url = input(">>")
html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')

for tag in tags:
    print(tag.get('href', None))

