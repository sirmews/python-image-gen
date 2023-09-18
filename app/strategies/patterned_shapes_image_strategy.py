from image_generator import generate_patterned_shapes

from .image_generation_strategy import ImageGenerationStrategy


class PatternedShapesImageStrategy(ImageGenerationStrategy):
    def generate(self, width, height):
        return generate_patterned_shapes(width, height)
