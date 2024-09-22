"""
item.py
Handles item logic (including the "bad shroom") for Super Marco Bros.
"""

import pygame
from settings import BLUE


class Item(pygame.sprite.Sprite):
    """Base class for items in the game that can be animated."""

    def __init__(self, frames, x, y, frame_duration=200):
        """
        :param frames: List of images representing the item's animation frames.
        :param x: Initial x position.
        :param y: Initial y position.
        :param frame_duration: Time in milliseconds for each frame.
        """
        super().__init__()
        self.frames = frames  # List of frames (sprite images)
        self.image = self.frames['idle'][0]  # Set the initial image to the first frame
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.frame_duration = frame_duration  # Time to display each frame (milliseconds)
        self.current_frame = 0  # Index of the current frame
        self.last_updated = pygame.time.get_ticks()  # Time when the last frame was updated

        self.is_animating = False  # Whether the item is animating
        self.loop_animation = False  # Whether the animation loops

    def animate(self, loop=False):
        """Start animating the item."""
        self.is_animating = True
        self.loop_animation = loop  # Set whether the animation should loop

    def stop_animation(self):
        """Stop the animation and reset to the first frame."""
        self.is_animating = False
        self.current_frame = 0
        self.image = self.frames[self.current_frame]  # Reset to the first frame

    def update(self):
        """Update the item's animation state if animating."""
        if self.is_animating:
            now = pygame.time.get_ticks()

            # If enough time has passed, update to the next frame
            if now - self.last_updated >= self.frame_duration:
                self.last_updated = now  # Update the last update time
                self.current_frame += 1  # Move to the next frame

                # If we reached the end of the frame list
                if self.current_frame >= len(self.frames):
                    if self.loop_animation:
                        self.current_frame = 0  # Loop back to the first frame
                    else:
                        self.stop_animation()  # Stop if not looping

                # Update the image to the current frame
                self.image = self.frames[self.current_frame]
