import pygame, spritesheet
from debug import *
from settings import *

# player class that handles rendering, movement and actions of the player
class Player(pygame.sprite.Sprite):

    # initialise class
    def __init__(self):
        super().__init__() # derive all properties from parent class Sprite

        # rendering
        spritesheet_img = pygame.image.load("Art Assets\Sprites\Link Walking.png")
        self.spritesheet = spritesheet.SpriteSheet(spritesheet_img)

        self.current_frame = 0
        self.image = self.spritesheet.get_frame(self.current_frame, 16, 16, 4)

        self.rect = self.image.get_rect() # stores rect of player

        # movement
        self.move_speed = 5
        self.dir = DOWN

    # Detects user input for movement and moves player
    def movement(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_a] == True: # a - left
            print_debug("Moving Left")
            self.rect.move_ip(tuple(i * self.move_speed for i in LEFT)) # dirn vector * scalar speed
            self.dir = LEFT

        if key[pygame.K_d] == True: # d - right
            print_debug("Moving Right")
            self.rect.move_ip(tuple(i * self.move_speed for i in RIGHT))
            self.dir = RIGHT

        if key[pygame.K_w] == True: # w - up
            print_debug("Moving Up")
            self.rect.move_ip(tuple(i * self.move_speed for i in UP))
            self.dir = UP

        if key[pygame.K_s] == True: # s - down
            print_debug("Moving Down")
            self.rect.move_ip(tuple(i * self.move_speed for i in DOWN))
            self.dir = DOWN
    
    # changes sprite angle based on direction and cycles through animation frames
    def animate(self):

        # update sprite frame based on direction
        if self.dir == DOWN:
            self.current_frame = 0
        elif self.dir == UP:
            self.current_frame = 2
        elif self.dir == LEFT:
            self.current_frame = 4
        elif self.dir == RIGHT:
            self.current_frame = 6

        # update sprite
        self.image = self.spritesheet.get_frame(self.current_frame, 16, 16, 4)

    # updates player sprite before rendering
    def update(self):

        # animate sprite to get current frame
        self.animate()

        