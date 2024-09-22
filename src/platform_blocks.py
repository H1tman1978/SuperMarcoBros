"""
platform_blocks.py
Handles platform logic for Super Marco Bros.
"""

import pygame
from settings import GREEN


class Platform(pygame.sprite.Sprite):
    """Represents a platform that the player can stand on."""

    def __init__(self, x, y, width, height, image=None):
        """
        :param x: X position of the platform.
        :param y: Y position of the platform.
        :param width: Width of the platform.
        :param height: Height of the platform.
        :param image: Optional pre-loaded image to be used for the platform sprite.
        """
        super().__init__()

        # If a pre-loaded image is provided, scale it to the platform size
        if image:
            self.image = pygame.transform.scale(image, (width, height))
        else:
            # Create a default platform surface with a solid color
            self.image = pygame.Surface((width, height))
            self.image.fill(GREEN)  # Default platform color

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, surface):
        """Draw the platform on the given surface."""
        surface.blit(self.image, self.rect)
