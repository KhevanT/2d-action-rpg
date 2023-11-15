import pygame, sys
from settings import *
from debug import *
from initialise import *

# Game Class
class Game:

    def __init__(self): # initialises basic pygame requirements

        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("2D Action RPG")
        self.clock = pygame.time.Clock()
    
    def run(self): # main pygame loop
        while True:

            self.screen.fill((COLOUR_WHITE))
            
            # Debug functions test
            # test screen print debug message
            # print_debug(pygame.mouse.get_pos())

            # Event Handler (Rough)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # system quit
                    pygame.quit()
                    sys.exit()
                
                '''
                # Tests
                elif event.type == pygame.KEYDOWN: # key pressed down
            
                    # Debug log message test
                    if event.key == pygame.K_q:
                        log_debug("TEST LOG MESSAGE. Q was pressed")

                    # Audio functions test
                    if event.key == pygame.K_s: # play sfx on S keypress
                        log_debug("S was pressed. SFX played")
                        soundManager.play_sound("Enemy Deflect")
                    elif event.key == pygame.K_w: # start bgm on W keypress
                        log_debug("W was pressed. BGM started playing")
                        soundManager.play_music("Overworld")
                    
                '''
            # Check for player input
            player_object.movement() 
            player_object.update()  

            # render player
            player_sprite_group.draw(self.screen)

            # update display and fps
            pygame.display.update()
            self.clock.tick(FPS)



# run main function if file is opened
if __name__ == "__main__":
    game = Game()
    game.run()

