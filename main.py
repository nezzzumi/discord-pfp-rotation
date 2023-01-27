import math
from sys import argv

from PIL import Image

img = Image.open(argv[1])


[img_output_name, extension] = argv[1].rsplit('.', 1)

rotations = 1
k = 1
x0 = 0
c = 0
y0 = 0

frames = []

for x in range(-60, 61):
    x /= 2.5

    y = rotations / (1 + math.exp((-k * (x - x0))))
    diff = abs(y - y0)
    y0 = y

    new_frame = img.rotate(y * 360 * -1)
    frames.append(new_frame)


frames[0].save(img_output_name+'.gif', save_all=True,
               append_images=frames[1:], optmize=True, loop=0)
