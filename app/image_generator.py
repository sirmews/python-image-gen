import random

from PIL import Image, ImageDraw


def generate_gradient(width=500, height=500):
    """Generate a gradient image"""
    base = Image.new('RGB', (width, height), color=(0, 0, 0))
    top_color = (random.randint(0, 255), random.randint(
        0, 255), random.randint(0, 255))
    bottom_color = (random.randint(0, 255), random.randint(
        0, 255), random.randint(0, 255))
    draw = ImageDraw.Draw(base)
    for y in range(height):
        r = (top_color[0] * (height - y) + bottom_color[0] * y) / height
        g = (top_color[1] * (height - y) + bottom_color[1] * y) / height
        b = (top_color[2] * (height - y) + bottom_color[2] * y) / height
        draw.line([(0, y), (width, y)], fill=(int(r), int(g), int(b)))
    return base


def draw_triangle(draw, x, y, size, color):
    half_size = size // 2
    triangle_points = [
        (x, y - half_size),
        (x - half_size, y + half_size),
        (x + half_size, y + half_size),
    ]
    draw.polygon(triangle_points, fill=color)


def draw_square(draw, x, y, size, color):
    draw.rectangle([(x - size // 2, y - size // 2),
                    (x + size // 2, y + size // 2)], fill=color)


def draw_circle(draw, x, y, size, color):
    draw.ellipse([(x - size // 2, y - size // 2),
                 (x + size // 2, y + size // 2)], fill=color)


def draw_hexagon(draw, x, y, size, color):
    angle = 360 / 6
    hexagon = [(x + size * math.cos(math.radians(a)), y + size *
                math.sin(math.radians(a))) for a in range(0, 360, angle)]
    draw.polygon(hexagon, fill=color)


def random_dark_color():
    return (random.randint(0, 128), random.randint(0, 128), random.randint(0, 128))


def generate_patterned_shapes(width=500, height=500, shape_size=50):
    shape_functions = [draw_triangle, draw_square, draw_circle, draw_hexagon]
    shape = random.choice(shape_functions)
    color = random_dark_color()

    img = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    for x in range(0, width, shape_size):
        for y in range(0, height, shape_size):
            shape(draw, x, y, shape_size, color)

    return img
