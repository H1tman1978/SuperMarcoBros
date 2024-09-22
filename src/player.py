"""
player.py
Handles player character logic (Marco and Luca) in Super Marco Bros.
"""

import pygame
from settings import PLAYER_SPEED, JUMP_HEIGHT, GRAVITY, WIDTH, HEIGHT


class Player(pygame.sprite.Sprite):
    """Represents the player character in the game."""

    def __init__(self, sprite_image, x, y):
        super().__init__()
        self.image = sprite_image  # Assign the sprite image
        self.rect = self.image.get_rect()

        # Set player's starting position
        self.rect.x = x
        self.rect.y = y

        # Player movement attributes
        self.velocity_x = 0
        self.velocity_y = 0
        self.is_jumping = False

        # Reverse control attributes
        self.controls_reversed = False
        self.reverse_timer = 0

    def reverse_controls(self):
        """Reverse player controls for 5 seconds when eating a bad shroom."""
        self.controls_reversed = True
        self.reverse_timer = pygame.time.get_ticks() + 5000  # Reverse for 5 seconds

    def handle_input(self):
        """Handle player input for movement and jumping."""
        keys = pygame.key.get_pressed()

        # Reverse controls if the effect is active
        left_key = pygame.K_RIGHT if self.controls_reversed else pygame.K_LEFT
        right_key = pygame.K_LEFT if self.controls_reversed else pygame.K_RIGHT

        # Horizontal movement (Arrow keys and WSAD)
        if keys[left_key] or keys[pygame.K_a]:
            self.velocity_x = -5
        elif keys[right_key] or keys[pygame.K_d]:
            self.velocity_x = 5
        else:
            self.velocity_x = 0

        # Jumping (Space or W key)
        if (keys[pygame.K_SPACE] or keys[pygame.K_w]) and not self.is_jumping:
            self.velocity_y = -10
            self.is_jumping = True

        # Reset controls after 5 seconds
        if self.controls_reversed and pygame.time.get_ticks() > self.reverse_timer:
            self.controls_reversed = False

    def apply_gravity(self):
        """Apply gravity to the player."""
        self.velocity_y += 1
        if self.rect.bottom >= HEIGHT - 50:
            self.rect.bottom = HEIGHT - 50
            self.velocity_y = 0
            self.is_jumping = False

    def update(self):
        """Update the player's position and apply movement logic."""
        self.handle_input()
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y
        self.apply_gravity()
