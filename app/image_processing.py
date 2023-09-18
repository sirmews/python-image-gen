from font_loader import get_font, initialize_fonts
from PIL import ImageDraw


def add_quote_to_image(img, quote, font_name, padding=10):
    """
    Adds a quote to the provided image, ensuring the quote doesn't exceed the image's boundaries.

    Args:
        img (PIL.Image): The image to add the quote to.
        quote (str): The quote text to be added.
        font_name (str): The name of the font to use.
        padding (int, optional): Padding from the edges of the image. Defaults to 30.

    Returns:
        PIL.Image: Image with the quote added.
    """
    max_font_size = 100  # set a reasonable max font size
    draw = ImageDraw.Draw(img)
    optimal_font_size = get_optimal_font_size(
        draw, quote, font_name, max_font_size, padding, img.width, img.height)
    optimal_font = get_font(font_name, font_size=optimal_font_size)
    draw_centered_text(img, quote, optimal_font)
    return img


def calculate_text_bbox(draw, quote, font):
    """Return the bounding box of the text for the given quote and font."""
    return draw.textbbox((0, 0), quote, font=font)


def draw_centered_text(img, quote, font):
    """
    Draw the given text centered on the image.

    Args:
    - img (PIL.Image): The image to draw the text on.
    - quote (str): The text to be drawn.
    - font (PIL.ImageFont.FreeTypeFont): The font object to use.

    Returns:
    - None: The function directly modifies the given image.
    """
    draw = ImageDraw.Draw(img)
    text_bbox = calculate_text_bbox(draw, quote, font)

    # Compute X and Y coordinates for centered placement of the text
    x = (img.width - text_bbox[2]) / 2
    y = (img.height - text_bbox[3]) / 2

    draw.text((x, y), quote, (255, 255, 255), font=font)


def get_optimal_font_size(draw, quote, font_name, max_size, padding, image_width, image_height):
    """
    Find the optimal font size for the given quote within the specified image dimensions.

    Args:
    - draw (ImageDraw.Draw): A drawing context for the image.
    - quote (str): The text we want to draw.
    - font_name (str): The font's name.
    - max_size (int): Maximum permissible font size.
    - padding (int): The padding from the image's borders.
    - image_width (int): Width of the image.
    - image_height (int): Height of the image.

    Returns:
    - int: The optimal font size for the quote to fit in the image.
    """
    base_font_size = 20  # Start with a reasonably small size to increment from

    while base_font_size < max_size:
        font = get_font(font_name, font_size=base_font_size)

        # Calculate the bounding box of the text for this font size
        text_bbox = calculate_text_bbox(draw, quote, font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]

        # If the quote width or height exceeds the image dimensions minus padding,
        # return the previous font size that fit
        if text_width > image_width - (2 * padding) or text_height > image_height - (2 * padding):
            return base_font_size - 10

        # Increment the font size for the next iteration
        base_font_size += 5

    return base_font_size
