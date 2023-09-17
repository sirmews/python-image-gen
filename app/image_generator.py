import random

from PIL import Image, ImageDraw


def generate_gradient(width=500, height=500):
    base = Image.new('RGB', (width, height), color=(0, 0, 0))
    top_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    bottom_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    draw = ImageDraw.Draw(base)
    for y in range(height):
        r = (top_color[0] * (height - y) + bottom_color[0] * y) / height
        g = (top_color[1] * (height - y) + bottom_color[1] * y) / height
        b = (top_color[2] * (height - y) + bottom_color[2] * y) / height
        draw.line([(0, y), (width, y)], fill=(int(r), int(g), int(b)))
    return base
