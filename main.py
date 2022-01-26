import sys
from PIL import Image

filename = sys.argv[1]

img = Image.open(filename).convert('L')
img.load()
width, height = img.size
matrix = [[0 for _ in range(width)] for _ in range(height)]

for x in range(width):
    for y in range(height):
        color = img.getpixel((x, y))
        if color < 25:
            matrix[y][x] = '@'
        elif color < 50:
            matrix[y][x] = '%'
        elif color < 75:
            matrix[y][x] = '#'
        elif color < 100:
            matrix[y][x] = '*'
        elif color < 125:
            matrix[y][x] = '+'
        elif color < 150:
            matrix[y][x] = '='
        elif color < 175:
            matrix[y][x] = '-'
        elif color < 200:
            matrix[y][x] = ':'
        elif color < 255:
            matrix[y][x] = '.'    
        else:
            matrix[y][x] = ' '

[print(*row, sep='') for row in matrix]



