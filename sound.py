#import winsound
import pygame
from pygame import mixer

import os, sys



def play(track):
    print(track)
    print(os.getcwd())
    APP_FOLDER = os.getcwd()
    track = APP_FOLDER + '\\' + track

    
    print(track)
    #winsound.PlaySound(track, winsound.SND_ASYNC | winsound.SND_ALIAS )
    pygame.mixer.init()
    pygame.mixer.music.load(track)
    pygame.mixer.music.play()
def stop():
    #winsound.PlaySound(None, winsound.SND_ASYNC)
    pygame.mixer.music.stop()