from PIL import Image, ImageFilter

before = Image.open("../assets/miniMe.jpg")
after = before.filter(ImageFilter.BoxBlur(1))
# after = before.filter(ImageFilter.FIND_EDGES)
after.save("out.jpg")

