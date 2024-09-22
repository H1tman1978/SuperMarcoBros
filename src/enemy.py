"""
enemy.py
Handles enemy logic for Super Marco Bros.
"""

import pygame
from settings import WIDTH


class Enemy(pygame.sprite.Sprite):
    """Represents a basic enemy that moves left and right with animation."""

    def __init__(self, frames, x, y, speed, frame_duration=200, platforms=None):
        """
        :param frames: List of images representing the enemy's animation frames.
        :param x: Initial x position.
        :param y: Initial y position.
        :param speed: Speed of enemy movement.
        :param frame_duration: Time in milliseconds for each frame.
        :param platforms: List of platform objects to check edge collisions.
        """
        super().__init__()
        self.frames = frames  # List of animation frames
        self.image = self.frames['idle'][0]  # Set the initial image to the first frame
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

        self.frame_duration = frame_duration  # Time per frame
        self.current_frame = 0
        self.last_updated = pygame.time.get_ticks()
        self.is_animating = True

        self.platforms = platforms  # List of platforms to detect edge collisions

    def animate(self):
        """Handle enemy animation by switching between frames."""
        now = pygame.time.get_ticks()

        if now - self.last_updated >= self.frame_duration:
            self.last_updated = now
            self.current_frame += 1

            if self.speed > 0:  # check if speed is greater than 0
                animation_key = 'walk_right'
            elif self.speed < 0:  # check if speed is lesser than 0
                animation_key = 'walk_left'
            else:
                animation_key = 'idle'

            if self.current_frame >= len(self.frames[animation_key]):
                self.current_frame = 0  # Loop back to the first frame

            self.image = self.frames[animation_key][self.current_frame]  # Update to the current frame

    def check_platform_edges(self):
        """Reverse direction if the enemy reaches the edge of a platform."""
        # Get the bottom left and bottom right of the enemy's rect
        bottom_left = self.rect.bottomleft
        bottom_right = self.rect.bottomright

        # Define a small buffer to ensure the enemy doesn't reverse prematurely on small gaps
        buffer = 2

        # Assume the enemy is not on a platform until checked
        on_platform = False

        # Expand the area of the check slightly to catch small platform gaps or edges
        bottom_left_with_buffer = (bottom_left[0] - buffer, bottom_left[1])
        bottom_right_with_buffer = (bottom_right[0] + buffer, bottom_right[1])

        # Check if either the left or right bottom part of the enemy is on a platform
        for platform in self.platforms:
            if platform.rect.collidepoint(bottom_left_with_buffer) or platform.rect.collidepoint(
                    bottom_right_with_buffer):
                on_platform = True
                break

        # If the enemy is not on a platform, reverse direction
        if not on_platform:
            self.speed = -self.speed

    def update(self):
        """Move the enemy back and forth, animate, and handle edge detection."""
        # Move the enemy left or right
        self.rect.x += self.speed

        # Reverse direction if hitting screen bounds
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speed = -self.speed

        # Check for platform edges
        if self.platforms:
            self.check_platform_edges()

        # Animate the enemy
        if self.is_animating:
            self.animate()
