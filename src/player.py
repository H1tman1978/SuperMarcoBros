"""
player.py
Handles player character logic (Marco and Luca) in Super Marco Bros.
"""

import pygame
from settings import PLAYER_SPEED, JUMP_HEIGHT, GRAVITY, WIDTH, HEIGHT


class Player(pygame.sprite.Sprite):
    """Represents the player character with animation support."""

    def __init__(self, frames, x, y, frame_duration=200):
        """
        :param frames: Dictionary of lists for different animation frames (e.g., 'walk_left', 'walk_right', etc.).
        :param x: Initial x position.
        :param y: Initial y position.
        :param frame_duration: Time in milliseconds for each frame.
        """
        super().__init__()

        # Animation frames (e.g., walk_left, walk_right, idle, jump)
        self.frames = frames
        self.image = self.frames['idle'][0]
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

        # Animation attributes
        self.frame_duration = frame_duration  # Time per frame
        self.current_frame = 0
        self.last_updated = pygame.time.get_ticks()
        self.current_animation = 'idle_right'  # Default animation

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
            self.current_animation = 'walk_left'
        elif keys[right_key] or keys[pygame.K_d]:
            self.velocity_x = 5
            self.current_animation = 'walk_right'
        else:
            self.velocity_x = 0
            self.current_animation = 'idle'

        # Jumping (Space or W key)
        if (keys[pygame.K_SPACE] or keys[pygame.K_w]) and not self.is_jumping:
            self.velocity_y = -10
            self.is_jumping = True
            self.current_animation = 'jump'

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

    def animate(self):
        """Animate the player character based on the current action (walking, jumping, idle)."""
        now = pygame.time.get_ticks()

        if now - self.last_updated >= self.frame_duration:
            self.last_updated = now
            self.current_frame += 1

            # Get the current animation frame list
            current_frames = self.frames[self.current_animation]

            if self.current_frame >= len(current_frames):
                self.current_frame = 0  # Loop back to the first frame

            self.image = current_frames[self.current_frame]

    def update(self):
        """Update the player's position, animation, and movement logic."""
        self.handle_input()  # Process user input
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y
        self.apply_gravity()  # Apply gravity to the player
        self.animate()  # Animate based on the player's current state

        # Ensure the player doesn't move out of bounds
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
