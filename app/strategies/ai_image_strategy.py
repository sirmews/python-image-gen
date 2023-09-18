from image_generator import generate_ai_background

from .image_generation_strategy import ImageGenerationStrategy


class AIImageStrategy(ImageGenerationStrategy):
    def generate(self, width, height):
        return generate_ai_background(width, height)
