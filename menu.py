import pygame, sys
from pygame_functions import *
import random

def gameloop():
    life = 3
    #########bucket############
    bucket = makeSprite("pictures/empty-bucket.png")
    transformSprite(bucket, 0.5, 0.5)
    pos_x = 1920/2
    moveSprite(bucket, pos_x, 800)
    showSprite(bucket)
    is_moving_left = False
    is_moving_right = False
    ##########bucket###########
    ##########famille pirate###
    victor = makeSprite("pictures/famille pirate/victor.png")
    pos_x_victor = random.randint(1, 1900)
    pos_y_victor = 50
    moveSprite(victor, pos_x_victor, 50)
    showSprite(victor)
    count_famille_pirate = 0
    ########famille pirate#####
    ########american dad#######
    american_dad = makeSprite("pictures/american dad/francine_smith.png")
    pos_x_american_dad = random.randint(1, 1900)
    pos_y_american_dad = 50
    moveSprite(american_dad, pos_x_american_dad, 50)
    showSprite(american_dad)
    count_american_dad = 0
    ########american dad#######
    while True:
        pos_y_american_dad += 1
        pos_y_victor += 1
        moveSprite(american_dad, pos_x_american_dad, pos_y_american_dad)
        moveSprite(victor, pos_x_victor, pos_y_victor)
        if (is_moving_left == True):
                    pos_x -= 8
                    moveSprite(bucket, pos_x, 800)
        if (is_moving_right == True):
                    pos_x += 8
                    moveSprite(bucket, pos_x, 800)
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            if (ev.type == pygame.KEYDOWN):
                if keyPressed("left"):
                    is_moving_left = True
                if keyPressed("right"):
                    is_moving_right = True
            else:
                is_moving_left = False
                is_moving_right = False
        #############ON CATCH#############
        if (pos_y_american_dad > 700 and pos_y_victor < 900) and pos_x - pos_x_american_dad < 150 and pos_x - pos_x_american_dad > -150:
            count_american_dad += 1
            hideSprite(american_dad)
        if (pos_y_victor > 700 and pos_y_american_dad < 900) and pos_x - pos_x_victor < 150 and pos_x - pos_x_victor > -150:
            count_famille_pirate += 1
            hideSprite(victor)
        #############ON CATCH#############
        #############ON LIFE LOST#############
        if (pos_y_american_dad < 0 or pos_y_victor < 0):
            life -= 1
            pos_x_american_dad = random.randint(1, 1900)
            pos_y_american_dad = 50
            pos_x_victor = random.randint(1, 1900)
            pos_y_victor = 50
            showSprite(american_dad)
            showSprite(victor)
        updateDisplay()

def menu():
    screen = screenSize(1920, 1080)
    while True:
        setBackgroundImage(["pictures/fond.png"])
        gameloop();
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()