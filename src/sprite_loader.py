import xml.etree.ElementTree as ET
import pygame

from src.settings import HEIGHT, SPRITESHEETS_LIST, WIDTH

pygame.init()
pygame.display.set_mode((WIDTH, HEIGHT))


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


# Load spritesheet images
sprites = {}
for sheet in SPRITESHEETS_LIST:
    image_path = sheet['image']
    xml_path = sheet['xml']

    # Load the sprite sheet image
    spritesheet_image = pygame.image.load(image_path).convert_alpha()

    # Load sprites from the corresponding XML file
    sprite_data = load_sprites_from_xml(xml_path, spritesheet_image)

    # Store the loaded sprite data in the main sprites dictionary
    sprites.update(sprite_data)