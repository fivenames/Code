import sys
from PIL import Image
import os
from PIL import ImageOps

n = len(sys.argv)

if n < 3:
    sys.exit("Too few command-line arguments")
elif n > 3:
    sys.exit("Too many command-line arguments")
else:
    try:
        root1, ext1 = os.path.splitext(sys.argv[1])
        root2, ext2 = os.path.splitext(sys.argv[2])
        ext1 = ext1.lower()
        ext2 = ext2.lower()
        if ext1 == '.png' or ext1 == '.jpg' or ext1 == 'jpeg':
            if ext2 == '.png' or ext2 == '.jpg' or ext2 == 'jpeg':
                shirt = Image.open("shirt.png", mode='r', formats=None)
                image = Image.open(sys.argv[1], mode='r', formats=None)
            else:
                sys.exit("File type not supported")
        else:
            sys.exit("File type not supported")
    except FileNotFoundError:
        sys.exit("File not found")

size = shirt.size
image = ImageOps.fit(image, size)

# Base image is output when the value of the mask image is 0 (black), pasted image is output when the mask image is 255 (white).
# For other values, the two images are blended according to the value.
# For this case, the mask image use is shirt itself, the background of the image is black, the output is the base image,
# the shirt itself, has a value much greater than 0, hence the output will be the paste image.
image.paste(shirt, mask=shirt)

image.save(sys.argv[2])