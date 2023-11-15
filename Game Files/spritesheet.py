import pygame
from settings import *

# This class handles the sprite import settings and frame changes
class SpriteSheet:

    def __init__(self, sheet):
        self.sheet = sheet

    # this function takes img data and returns specified frame
    def get_frame(self, frame, width, height, scale):
        
        image = pygame.Surface((width, height))

        # this tricky line of code extracts the specified frames data starting from (0,0)
        # and offset by fram * width across the horizontal length of the image
        image.blit(self.sheet, dest = (0, 0), area = ((frame * width), 0, width, height))

        # scale image
        image = pygame.transform.scale(image, (width * scale, height * scale))

        # converts given colour pixels to transparent
        image.set_colorkey(COLOUR_BLACK)

        return image

    # returns a list of all frames from spritesheet
    # CAUSING ERROR : the returned list for some reason is not comprised of the right data type
    # this is leading to errors with image.get_rect() calls
    '''
    def get_all_frames(self, count, width, height, scale):

        sprite_list = []
        for i in range(count):
            x = self.get_frame(i, width, height, scale)
            sprite_list.append(x)
            
        return sprite_list
    '''
    
        


