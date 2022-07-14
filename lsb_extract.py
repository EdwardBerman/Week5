import numpy as np
from PIL import Image

img = Image.open("embeddedImage.bmp", 'r')
array = np.array(list(img.getdata()))
total_pixels = array.size//3

hidden_bits = ""
for p in range(total_pixels):
    for q in range(0, 3):
        hidden_bits += (bin(array[p][q])[2:][-1])
hidden_bits = [hidden_bits[i:i+8]for i in range(0, len(hidden_bits), 8)]
message = ""

for i in range(len(hidden_bits)):
    if message[-1:] == "!":
        break
    else:
        message += chr(int(hidden_bits[i], 2))
print("Hidden Message:", message)
