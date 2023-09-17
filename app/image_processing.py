from font_loader import get_font, initialize_fonts
from PIL import ImageDraw


def add_quote_to_image(img, quote, font, padding=10):
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
    font_name = font
    font = get_font(font_name, font_size=50)

    draw = ImageDraw.Draw(img)
    
    # Calculate the bounding box of the text
    text_bbox = draw.textbbox((0, 0), quote, font=font)
    
    # Width and height of the bounding box
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]



    # Scale down the font size if the quote doesn't fit within the image

    # while text_width < img.width - (2 * padding) or text_height < img.height - (2 * padding):
    #     font_size += 5
    #     font = get_font(font_name, font_size)
    #     text_bbox = draw.textbbox((0, 0), quote, font=font)
    #     text_width = text_bbox[2] - text_bbox[0]
    #     text_height = text_bbox[3] - text_bbox[1]

    # Calculate X, Y position of the text
    x = (img.width - text_width) / 2
    y = (img.height - text_height) / 2

    draw.text((x, y), quote, (255,255,255), font=font)
    
    return img
