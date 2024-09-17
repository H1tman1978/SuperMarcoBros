"""
item.py
Handles item logic (including the "bad shroom") for Super Marco Bros.
"""

import pygame
from src.settings import BLUE


class Item(pygame.sprite.Sprite):
    """Represents a collectible item, such as the 'bad shroom'."""

    def __init__(self, x, y, width, height):
        super().__init__()
        # Create item surface
        self.image = pygame.Surface((width, height))
        self.image.fill(BLUE)  # Default item color (blue for now)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def apply_effect(self, player):
        """Apply the bad shroom effect to the player."""
        # Invert controls for a set duration (this will be implemented later)
        player.reverse_controls()
