import sys
from PIL import Image

filename = sys.argv[1]

img = Image.open(filename).convert('1')
img.load()
width, height = img.size
matrix = [[0 for _ in range(width)] for _ in range(height)]

for x in range(width):
    for y in range(height):
        rgb = img.getpixel((x, y))
        if rgb == 0:
            matrix[y][x] = 0
        else:
            matrix[y][x] = '.'

[print(*row) for row in matrix]



