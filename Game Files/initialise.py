# This script initialises all classes and things needed for main game
# It is seperate from settings because the classes being initalised required constants from settings
# Leading to circular calls?

import pygame, soundmanager, player

# soundmanager (only 1 in game)
soundManager = soundmanager.SoundManager()

# player (only 1 in game)
player_object = player.Player()
player_sprite_group = pygame.sprite.Group()
player_sprite_group.add(player_object)
