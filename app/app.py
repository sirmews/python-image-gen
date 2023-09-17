from io import BytesIO

import requests
from flask import Flask, render_template, request, send_file
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)

UNSPLASH_URL = "https://api.unsplash.com/photos/random?client_id=YOUR_UNSPLASH_ACCESS_KEY"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        quote = request.form['quote']
        image = get_random_image_from_unsplash()
        image_with_quote = add_quote_to_image(image, quote)
        image_with_quote.save("static/generated_image.jpg")
        return render_template('index.html', image_path="static/generated_image.jpg")
    return render_template('index.html', image_path=None)

def get_random_image_from_unsplash():
    response = requests.get(UNSPLASH_URL)
    img_url = response.json()['urls']['full']
    img_response = requests.get(img_url)
    return Image.open(BytesIO(img_response.content))

def add_quote_to_image(img, quote):
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("path_to_font.ttf", 20) # Change this to path of any TTF font file you have
    draw.text((10,10), quote, (255,255,255), font=font)
    return img

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
