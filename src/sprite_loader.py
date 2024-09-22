import xml.etree.ElementTree as ET
import pygame


def load_sprites_from_xml(xml_file, spritesheet_image):
    """Load the sprite information from the XML file and cut images from the sprite sheet."""
    tree = ET.parse(xml_file)
    root = tree.getroot()

    sprites = {}

    # Loop through each 'SubTexture' tag in the XML and extract its attributes
    for subtexture in root.findall('SubTexture'):
        name = subtexture.attrib['name']
        x = int(subtexture.attrib['x'])
        y = int(subtexture.attrib['y'])
        width = int(subtexture.attrib['width'])
        height = int(subtexture.attrib['height'])

        # Extract the subimage from the sprite sheet
        sprite_image = spritesheet_image.subsurface(pygame.Rect(x, y, width, height))

        # Store the sprite image in the dictionary with its name as the key
        sprites[name] = sprite_image

    return sprites
