import json
import os
from io import BytesIO

import requests
from PIL import ImageFont

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FONTS_JSON_PATH = os.path.join(BASE_DIR, 'fonts.json')

# Global cache for fonts
FONTS_CACHE = {}


def load_font_metadata(filename='fonts.json'):
    """
    Load font metadata from the provided JSON file.
    """
    with open(FONTS_JSON_PATH) as f:
        return json.load(f)


def fetch_and_cache_font(font_url, font_name, font_size=36):
    """
    Download a font from the given URL and cache it using font_name.
    """
    try:
        response = requests.get(font_url)
        if response.status_code == 200:
            font_file = BytesIO(response.content)
            # You can change the default size here
            font = ImageFont.truetype(font_file, font_size)
            # Cache the font using font_name and font_size as the key
            key = f"{font_name}_{font_size}"
            FONTS_CACHE[key] = font
            return font
        else:
            print(f"Error downloading {font_name} from {font_url}")
            return None
    except Exception as e:
        print(
            f"An error occurred while downloading {font_name} from {font_url}: {e}")
        return None


def get_font(font_name, font_size=36):
    """
    Get a font from the cache. If not in cache, it will try to fetch and cache it.
    """
    key = f"{font_name}_{font_size}"
    if font_name in FONTS_CACHE:
        return FONTS_CACHE[key]
    else:
        # Try fetching the font if it's not already in cache
        fonts_metadata = load_font_metadata()
        # inspiration: https://www.seeratawan.me/blog/generating-font-previews-with-python-pillow-for-enhanced-ux/
        for font in fonts_metadata:
            if font['postscript_name'] == font_name:
                return fetch_and_cache_font(font['url'], font_name, font_size)
        print(f"Font {font_name} not found in fonts.json")
        # trigger error and exit

        return None


def initialize_fonts():
    """
    Preload all fonts from the fonts.json into the cache.
    """
    fonts_metadata = load_font_metadata()
    for font in fonts_metadata:
        fetch_and_cache_font(font['url'], font['postscript_name'])


if __name__ == "__main__":
    # If you run this file, it will initialize all fonts (useful for testing)
    initialize_fonts()
    print(f"Loaded {len(FONTS_CACHE)} fonts into cache.")
