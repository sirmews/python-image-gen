from io import BytesIO

from flask import Flask, render_template, request, send_file
from font_loader import get_font, initialize_fonts
from image_generator import \
    generate_gradient  # Import the function from image_generator.py
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)

initialize_fonts()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        quote = request.form['quote']
        image = generate_gradient()
        image_with_quote = add_quote_to_image(image, quote)
        
        # Create a BytesIO buffer to hold the image data in memory
        img_io = BytesIO()
        image_with_quote.save(img_io, format='JPEG')
        img_io.seek(0)

        #return render_template('index.html', image_path="static/generated_image.jpg")
        # Return the image data directly as the response with the appropriate content type
        return send_file(img_io, mimetype='image/jpeg', as_attachment=False)
    return render_template('index.html', image_path=None)

def add_quote_to_image(img, quote):
    font_name = "OpenSans-Light"
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
