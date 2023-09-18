import base64
from io import BytesIO

from flask import Flask, render_template, request, send_file
from font_loader import get_font, initialize_fonts
from image_generator import \
    generate_gradient  # Import the function from image_generator.py
from image_processing import add_quote_to_image
from PIL import Image, ImageDraw, ImageFont
from social_media_images import SOCIAL_MEDIA_SIZES
from strategies.gradient_image_strategy import GradientImageStrategy
from strategies.patterned_shapes_image_strategy import \
    PatternedShapesImageStrategy

app = Flask(__name__)

initialize_fonts()

IMAGE_STRATEGIES = {
    'gradient': GradientImageStrategy(),
    'patterned_shapes': PatternedShapesImageStrategy()
}


@app.route('/', methods=['GET', 'POST'])
def index():
    image_data = None
    if request.method == 'POST':
        quote = request.form['quote']
        font_name = "OpenSans-SemiBold"

        # Retrieve the selected size
        selected_size = request.form['platform_size']
        platform, size_name = selected_size.split('-', 1)
        width, height = SOCIAL_MEDIA_SIZES[platform][size_name]

        # Choose image generation strategy based on user input
        image_type = request.form.get('image_type', 'patterned_shapes')
        strategy = IMAGE_STRATEGIES.get(image_type)
        image = strategy.generate(width, height)

        image_with_quote = add_quote_to_image(image, quote, font_name)

        # Create a BytesIO buffer to hold the image data in memory
        img_io = BytesIO()
        image_with_quote.save(img_io, format='JPEG')
        img_io.seek(0)

        # Encode the image into a Data URL format
        img_base64 = base64.b64encode(img_io.getvalue()).decode('utf-8')
        image_data = f"data:image/jpeg;base64,{img_base64}"

    return render_template('index.html', image_data=image_data, SOCIAL_MEDIA_SIZES=SOCIAL_MEDIA_SIZES)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
