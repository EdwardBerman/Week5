# LEAST SIGNIFICANT BIT (LSB) EMBEDDING

import numpy as np
from PIL import Image

# Put Map File into testEmbed.bmp
img = Image.open("testEmbed.bmp", 'r')
width, height = img.size
array = np.array(list(img.getdata()))
total_pixels = array.size//3

binary_key = "1011010101*"
message = ''.join([format(ord(i), "08b") for i in binary_key])

index=0
for p in range(total_pixels):
    for q in range(0, 3):
     if index < len(message): array[p][q] = int( bin(array[p][q]) [2:9] + message[index], 2)
     index += 1

array = array.reshape(height, width, 3)
enc_img = Image.fromarray(array.astype('uint8'), img.mode)

# What file to save Map into
enc_img.save("embeddedImage.bmp")
print("Image Encoded Successfully")
