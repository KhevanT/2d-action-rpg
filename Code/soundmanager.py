import pygame

class SoundManager:

    def __init__(self):
        pygame.mixer.init()

        self.sounds_vol = 0.4
        self.music_vol = 0.2

        self.sounds = {
            "Player Hurt": pygame.mixer.Sound("Art Assets\Audio\SFX_Player Hurt.wav"),
            "Enemy Hurt": pygame.mixer.Sound("Art Assets\Audio\SFX_Enemy Hurt.wav"),
            "Enemy Deflect": pygame.mixer.Sound("Art Assets\Audio\SFX_Enemy Deflecting.wav")
        }

        self.music = {
            "Overworld": "Art Assets\Audio\BGM_Overworld.wav",
            "Underworld": "Art Assets\Audio\BGM_Underworld.wav"
        }
    
    # plays a sound effect file once and stops
    def play_sound(self, name):
        self.sounds[name].set_volume(self.sounds_vol)
        self.sounds[name].play()

    # plays a music file on loop until another music file is called
    def play_music(self, name):
        pygame.mixer.music.load(self.music[name])
        pygame.mixer.music.set_volume(self.music_vol)
        pygame.mixer.music.play(-1)