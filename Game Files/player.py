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

        self.frame_count = 8
        self.sprite_list = self.spritesheet.get_all_frames(self.frame_count, 16, 16, 4)

        self.current_frame = 0
        self.image = self.sprite_list[self.current_frame]

        self.rect = self.image.get_rect() # stores rect of player

        # movement
        self.moving = False # NOT IMPLEMENTED YET, BUT REQUIRED FOR ANIM
        self.move_speed = 5
        self.dir = DOWN


    # Detects user input for movement and moves player
    def movement(self):

        key = pygame.key.get_pressed()
        wasd_input = [key[pygame.K_a], key[pygame.K_d], key[pygame.K_w], key[pygame.K_s]]

        prev_dir = self.dir

        # test for moving bool (required for anim and prob later too)
        if any(wasd_input) == True:
            self.moving = True
        else:
            self.moving = False

        if wasd_input[0]: # a - left
            # print_debug("Moving Left")
            self.rect.move_ip(tuple(i * self.move_speed for i in LEFT)) # dirn vector * scalar speed
            self.dir = LEFT

        if wasd_input[1]: # d - right
            # print_debug("Moving Right")
            self.rect.move_ip(tuple(i * self.move_speed for i in RIGHT))
            self.dir = RIGHT

        if wasd_input[2]: # w - up
            # print_debug("Moving Up")
            self.rect.move_ip(tuple(i * self.move_speed for i in UP))
            self.dir = UP

        if wasd_input[3]: # s - down
            # print_debug("Moving Down")
            self.rect.move_ip(tuple(i * self.move_speed for i in DOWN))
            self.dir = DOWN
        
        # change sprite direction, but only if there is an actual change in direction
        # helps avoid resetting walking animation cycle
        if prev_dir != self.dir:
            self.change_dir()
            
    
    # changes sprite angle based on direction 
    def change_dir(self):

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
        self.image = self.sprite_list[self.current_frame]

    # cycles through animation frames
    def walking_anim(self):
        pass


        # TO IMPLEMENT:
        # time.Clock based animation cycle change
        # its more annoying but better to learn

        '''
        # increment next frame only by a bit to time anim better
        self.current_frame += 0.1

        if self.current_frame >= len(self.sprite_list):
            self.current_frame = 0

        self.image = self.sprite_list[int(self.current_frame)]
        '''

        '''
        anim_cycle_len = 1
        anim_cycle_starts = [0, 2, 4, 6]
        anim_cycle_ends = [1, 3, 5, 7]

        self.current_frame += 0.1
        for i in range(3):
            if self.current_frame == anim_cycle_ends[i]:
                self.current_frame = anim_cycle_starts[i]

        self.image = self.sprite_list[int(self.current_frame)]
        '''

        

    # updates player sprite before rendering
    def update(self):

        '''
        # movement based sprite changes
        if self.moving == True:

            # cycle through walking animation
            self.walking_anim()
            log_debug(self.current_frame)
        '''
        

        

        
        


        