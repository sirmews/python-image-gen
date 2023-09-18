from image_generator import generate_gradient

from .image_generation_strategy import ImageGenerationStrategy


class GradientImageStrategy(ImageGenerationStrategy):
    def generate(self, width, height):
        return generate_gradient(width, height)
