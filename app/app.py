import base64
from io import BytesIO

from flask import Flask, render_template, request, send_file
from font_loader import get_font, initialize_fonts
from image_generator import \
    generate_gradient  # Import the function from image_generator.py
from PIL import Image, ImageDraw, ImageFont
from social_media_images import SOCIAL_MEDIA_SIZES

app = Flask(__name__)

initialize_fonts()

@app.route('/', methods=['GET', 'POST'])
def index():
    image_data = None
    if request.method == 'POST':
        quote = request.form['quote']
        
        # Retrieve the selected size
        selected_size = request.form['platform_size']
        platform, size_name = selected_size.split('-', 1)
        width, height = SOCIAL_MEDIA_SIZES[platform][size_name]

        image = generate_gradient(width, height)

        image_with_quote = add_quote_to_image(image, quote)
        
        # Create a BytesIO buffer to hold the image data in memory
        img_io = BytesIO()
        image_with_quote.save(img_io, format='JPEG')
        img_io.seek(0)

        # Encode the image into a Data URL format
        img_base64 = base64.b64encode(img_io.getvalue()).decode('utf-8')
        image_data = f"data:image/jpeg;base64,{img_base64}"

    return render_template('index.html', image_data=image_data, SOCIAL_MEDIA_SIZES=SOCIAL_MEDIA_SIZES)

def add_quote_to_image(img, quote):
    font_name = "OpenSans-SemiBold"
    font = get_font(font_name)
    draw = ImageDraw.Draw(img)
    #font = ImageFont.load_default()

    # Calculate the bounding box of the text
    text_bbox = draw.textbbox((0, 0), quote, font=font)
    
    
    # Width and height of the bounding box
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # Calculate X, Y position of the text
    x = (img.width - text_width) / 2
    y = (img.height - text_height) / 2

    draw.text((x, y), quote, (255,255,255), font=font)
    
    return img


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
