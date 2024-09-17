"""
platform.py
Handles platform logic for Super Marco Bros.
"""

import pygame
from src.settings import WIDTH, HEIGHT, GREEN


class Platform(pygame.sprite.Sprite):
    """Represents a platform that the player can stand on."""

    def __init__(self, x, y, width, height):
        super().__init__()
        # Create platform surface
        self.image = pygame.Surface((width, height))
        self.image.fill(GREEN)  # Default platform color (green for now)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, surface):
        """Draw the platform on the given surface."""
        surface.blit(self.image, self.rect)
