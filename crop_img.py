""" python script to crop image"""

from PIL import Image

left = int(input("Pixel from left : "))
upper = int(input("Pixel from top : "))
right = int(input("Pixel from right : "))
lower = int(input("Pixel from bottom : "))
img_path = str(input("Enter image path : "))

open_img = Image.open(img_path)
crop_image = open_img.crop((left,upper,right,lower))
crop_image.show()