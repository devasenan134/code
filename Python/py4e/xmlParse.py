import urllib.request
import xml.etree.ElementTree as ET

data = """
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Deva</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Jonesy</name>
        </user>
    </users>
</stuff>
"""

url = input(">>")
fhand = urllib.request.urlopen(url)

data = """"""
tot = 0

for line in fhand:
    data += line.decode()


commentinfo = ET.fromstring(data)

lst = commentinfo.findall("comments/comment")

print("User count:", len(lst))

for item in lst:
    print("Name:", item.find("name").text)
    print("Count:", item.find("count").text)
#    print("Attribute:", item.get("X"))
    tot += int(item.find("count").text)

print("Sum:", tot)

