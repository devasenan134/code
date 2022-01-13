import urllib.request, urllib.parse
import json
import ssl


api_key = "AIzaSyChpRoVgR3qQ7T0yo7bT1qj18V4uQCY1Ss"

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'


# ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


while True:
    address = input("Enter location: ")
    if len(address) < 1: break


    parms = {}
    parms["address"] = address
    if api_key is not False: parms["key"] = api_key

    url = serviceurl + urllib.parse.urlencode(parms)
    print("Retrieving", url)
    fhand = urllib.request.urlopen(url, context=ctx)
    data = fhand.read().decode()
    print("Retrieved", len(data), "characters")

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or "status" not in js or js['status'] != "OK":
        print("==== Failure To Retrieve ====")
        print(data)
        break

    print(json.dumps(js, indent=4))             # pretty printing

    # lat = js["results"][0]["geometry"]["location"]["lat"]
    # lng = js["results"][0]["geometry"]["location"]["lng"]
    # print("lat", lat, "lng", lng)
    # location = js["results"][0]["formatted_address"]
    # print(location)
