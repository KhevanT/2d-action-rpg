import pygame, logging, os
from settings import *
pygame.init()

font = pygame.font.Font(None, 30) # default font size 30

# check for log text file and clear file from previous run of code
# NOT WORKING
if os.path.exists('gamelog.txt'):
    os.remove('gamelog.txt')

# prints debug info on screen at given pos in real-time
def print_debug(info, x = 10, y = 10):

    display_surface = pygame.display.get_surface() # get active screen

    # set font, font colour and pos info
    debug_surface = font.render(str(info), True, COLOUR_WHITE)
    debug_rect = debug_surface.get_rect(topleft = (x, y))

    # set rect, bgcolour and display on screen
    pygame.draw.rect(display_surface, COLOUR_BLACK, debug_rect)
    display_surface.blit(debug_surface, debug_rect)


# display messages in log screen and adds them to text file
# only use in conditions, otherwise it keeps printing
def log_debug(a: str, newline = 0):
    level = logging.INFO
    format_ = '%(message)s'
    handlers = [logging.FileHandler('gamelog.txt'), logging.StreamHandler()]
    logging.basicConfig(level=level, format=format_, handlers=handlers)
    logging.info(a)
    if newline == 1:  # default new line is 0
        logging.info(" ")

    