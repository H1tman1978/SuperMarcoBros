"""
enemy.py
Handles enemy logic for Super Marco Bros.
"""

import pygame
from settings import WIDTH, RED


class Enemy(pygame.sprite.Sprite):
    """Represents a basic enemy that moves left and right."""

    def __init__(self, x, y, width, height, speed):
        super().__init__()
        # Create enemy surface
        self.image = pygame.Surface((width, height))
        self.image.fill(RED)  # Default enemy color (red for now)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def update(self):
        """Move the enemy back and forth."""
        self.rect.x += self.speed

        # Reverse direction when reaching screen bounds
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speed = -self.speed
