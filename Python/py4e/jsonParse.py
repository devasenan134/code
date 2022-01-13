import urllib.request, urllib.error
import json

url = input(">>")
fhand = urllib.request.urlopen(url)         # urlopen will ignore headers
headers = dict(fhand.getheaders())          # to get the headers


data = """"""
tot = 0

for line in fhand:
#    print(line.decode().strip())
    data += line.decode()

info = json.loads(data)
print("User count:", len(info["comments"]))

userList = info["comments"]

for user in userList:
    tot += user["count"]

print("Sum:", tot)
