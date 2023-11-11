import pygame, sys
from settings import *
from debug import *

# Game Class
class Game:

    def __init__(self): # initialises basic pygame requirements

        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
    
    def run(self): # main pygame loop
        while True:

            # check for game quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.screen.fill((COLOUR_WHITE))

            '''
            # test screen print debug message
            print_debug(pygame.mouse.get_pos())

            # test log file debug message
            # check for user input and move player 
            key = pygame.key.get_pressed()
            if key[pygame.K_q] == True:
                log_debug("TEST LOG MESSAGE. Q was pressed")
            '''
            

            # update display and fps
            pygame.display.update()
            self.clock.tick(FPS)



# run main function if file is opened
if __name__ == "__main__":
    game = Game()
    game.run()