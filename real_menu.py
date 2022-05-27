from itertools import count
import pygame, sys
from pygame_functions import *
import random
import time


def real_menu():
    is_menu_opened = True
    shut_the_menu_down = False
    sound_already_played = False
    menu_background = makeSprite("pictures/menu_background.jpg")
    start_logo = makeSprite("pictures/real_menu/start_logo.png")
    moveSprite(start_logo, 900, 350)
    transformSprite(start_logo, 0.5, 2)
    settings_logo = makeSprite("pictures/real_menu/settings_logo.png")
    moveSprite(settings_logo, 900, 600)
    transformSprite(settings_logo, 0.5, 2)
    credits_logo = makeSprite("pictures/real_menu/credits_logo.png")
    moveSprite(credits_logo, 900, 850)
    transformSprite(credits_logo, 0.5, 2)
    hand_selection = makeSprite("pictures/real_menu/hand_selection.png")
    moveSprite(hand_selection, 900, (350 + 67))
    transformSprite(hand_selection, 0.2, 0.2)

    menu_music = makeSound("sound/my_family_pies_no_bass_boosted.wav")

    pos_y_hand_selection = (350 + 67)
    if sound_already_played == False:
        playSound(menu_music)
        sound_already_played = True
    while is_menu_opened == True:
        showSprite(menu_background)

        showSprite(start_logo)
        showSprite(settings_logo)
        showSprite(credits_logo)
        showSprite(hand_selection)
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            if (ev.type == pygame.KEYDOWN):
                if keyPressed("down"):
                    if (pos_y_hand_selection == (600 + 67)):
                        moveSprite(hand_selection, 900, (850 + 67))
                        pos_y_hand_selection = (850 + 67)
                    if (pos_y_hand_selection == (350 + 67)):
                        moveSprite(hand_selection, 900, (600 + 67))
                        pos_y_hand_selection = (600 + 67)
                    time.sleep(1)
                if keyPressed("up"):
                    if (pos_y_hand_selection == (600 + 67)):
                        moveSprite(hand_selection, 900, (350 + 67))
                        pos_y_hand_selection = (350 + 67)
                    if (pos_y_hand_selection == (850 + 67)):
                        moveSprite(hand_selection, 900, (600 + 67))
                        pos_y_hand_selection = (600 + 67)
                    time.sleep(1)
                if keyPressed("return"):
                    if (pos_y_hand_selection == (350 + 67)):
                        is_menu_opened = False
                        break
        # if is_menu_opened == False:
        #     break
        # for ev in pygame.event.get():
        #     if ev.type == pygame.QUIT:
    hideSprite(menu_background)
    hideSprite(settings_logo)    
    hideSprite(start_logo)    
    hideSprite(credits_logo)    
    hideSprite(hand_selection)    
    stopSound(menu_music)