# python 3.7.1

from pathlib import Path
from scratch.emojis_converter import emojis_converter
path = Path("emojis converter")
print(path.exists())
msg = input("message >")
print(emojis_converter(msg))
