import os
import qrcode

url = input("Enter a url: ")
img = qrcode.make(url)
img.save("qr.png", "PNG")
os.system("qr.png")

