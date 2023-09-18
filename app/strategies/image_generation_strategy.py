from abc import ABC, abstractmethod


class ImageGenerationStrategy(ABC):

    @abstractmethod
    def generate(self, width, height):
        pass
