import pygame, sys
from pygame_functions import *
import random

def gameloop():
    life = 3
    speed_mult = 1
    #########bucket############
    bucket = makeSprite("pictures/empty-bucket.png")
    transformSprite(bucket, 0.5, 0.5)
    pos_x = 1920/2 + 100
    moveSprite(bucket, pos_x, 800)
    showSprite(bucket)
    is_moving_left = False
    is_moving_right = False
    bucket2 = makeSprite("pictures/empty-bucket.png")
    transformSprite(bucket2, 0.5, 0.5)
    pos_x2 = 1920/2 - 100
    moveSprite(bucket2, pos_x2, 800)
    showSprite(bucket2)
    is_moving_left2 = False
    is_moving_right2 = False
    ##########bucket###########
    ##########famille pirate###
    victor = makeSprite("pictures/famille pirate/victor.png")
    pos_x_victor = random.randint(1, 1900)
    pos_y_victor = 0 - random.randint(100, 2000)
    moveSprite(victor, pos_x_victor, pos_y_victor)
    showSprite(victor)
    count_famille_pirate = 0
    ########famille pirate#####
    ########american dad#######
    american_dad = makeSprite("pictures/american dad/Stan_smith.png")
    francine = makeSprite("pictures/american dad/francine_smith.png")
    hayley = makeSprite("pictures/american dad/Hayley_smith.png")
    roger = makeSprite("pictures/american dad/roger_smith.png")
    steve = makeSprite("pictures/american dad/steve_smith.png")
    pos_x_american_dad = random.randint(1, 1900)
    pos_y_american_dad = 0 - random.randint(100, 2000)
    pos_x_francine = random.randint(1, 1900)
    pos_y_francine = 0 - random.randint(100, 2000)
    pos_x_hayley = random.randint(1, 1900)
    pos_y_hayley = 0 - random.randint(100, 2000)
    pos_x_roger = random.randint(1, 1900)
    pos_y_roger = 0 - random.randint(100, 2000)
    pos_x_steve = random.randint(1, 1900)
    pos_y_steve = 0 - random.randint(100, 2000)
    moveSprite(american_dad, pos_x_american_dad, pos_y_american_dad)
    showSprite(american_dad)
    moveSprite(francine, pos_x_francine, pos_y_francine)
    showSprite(francine)
    moveSprite(hayley, pos_x_hayley, pos_y_hayley)
    showSprite(hayley)
    moveSprite(roger, pos_x_roger, pos_y_roger)
    showSprite(roger)
    moveSprite(steve, pos_x_steve, pos_y_steve)
    showSprite(steve)
    count_american_dad = 0
    ########american dad#######
    ########malcom#############
    dewey = makeSprite("pictures/malcom/dewey.png")
    francis = makeSprite("pictures/malcom/francis.png")
    hal = makeSprite("pictures/malcom/hal.png")
    lois = makeSprite("pictures/malcom/lois.png")
    malcom = makeSprite("pictures/malcom/malcom.png")
    rise = makeSprite("pictures/malcom/rise.png")
    pos_x_dewey = random.randint(1, 1900)
    pos_y_dewey = 0 - random.randint(100, 2000)
    pos_x_francis = random.randint(1, 1900)
    pos_y_francis = 0 - random.randint(100, 2000)
    pos_x_hal = random.randint(1, 1900)
    pos_y_hal = 0 - random.randint(100, 2000)
    pos_x_lois = random.randint(1, 1900)
    pos_y_lois = 0 - random.randint(100, 2000)
    pos_x_malcom = random.randint(1, 1900)
    pos_y_malcom = 0 - random.randint(100, 2000)
    pos_x_rise = random.randint(1, 1900)
    pos_y_rise = 0 - random.randint(100, 2000)
    moveSprite(dewey, pos_x_dewey, pos_y_dewey)
    showSprite(dewey)
    moveSprite(francis, pos_x_francis, pos_y_francis)
    showSprite(francis)
    moveSprite(hal, pos_x_hal, pos_y_hal)
    showSprite(hal)
    moveSprite(lois, pos_x_lois, pos_y_lois)
    showSprite(lois)
    moveSprite(malcom, pos_x_malcom, pos_y_malcom)
    showSprite(malcom)
    moveSprite(rise, pos_x_rise, pos_y_rise)
    showSprite(rise)
    count_dewey = 0
    ########malcom#############
    ########soda###############

    ########soda###############
    ########famille pirate#####

    ########famille pirate#####
    ########simpsons###########

    ########simpsons###########
    ########family guys########

    ########family guys########
    while True:
        pos_y_american_dad += 1 * speed_mult
        pos_y_francine += 1 * speed_mult
        pos_y_hayley += 1 * speed_mult
        pos_y_roger += 1 * speed_mult
        pos_y_steve += 1 * speed_mult
        moveSprite(american_dad, pos_x_american_dad, pos_y_american_dad)
        moveSprite(francine, pos_x_francine, pos_y_francine)
        moveSprite(hayley, pos_x_hayley, pos_y_hayley)
        moveSprite(roger, pos_x_roger, pos_y_roger)
        moveSprite(steve, pos_x_steve, pos_y_steve)
        moveSprite(victor, pos_x_victor, pos_y_victor)

        pos_y_victor += 1 * speed_mult
        speed_mult += 0.002
        if (is_moving_left == True):
                    pos_x -= 15
                    moveSprite(bucket, pos_x, 800)
        if (is_moving_right == True):
                    pos_x += 15
                    moveSprite(bucket, pos_x, 800)
        if (is_moving_left2 == True):
                    pos_x2 -= 15
                    moveSprite(bucket2, pos_x2, 800)
        if (is_moving_right2 == True):
                    pos_x2 += 15
                    moveSprite(bucket2, pos_x2, 800)
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            if (ev.type == pygame.KEYDOWN):
                if keyPressed("left"):
                    is_moving_left = True
                if keyPressed("right"):
                    is_moving_right = True
                if keyPressed("q"):
                    is_moving_left2 = True
                if keyPressed("d"):
                    is_moving_right2 = True
            else:
                is_moving_left = False
                is_moving_right = False
                is_moving_left2 = False
                is_moving_right2 = False
        #############ON CATCH#############
        if (pos_y_american_dad > 700 and pos_y_american_dad < 900 and ((pos_x - pos_x_american_dad < 150 and pos_x - pos_x_american_dad > -150) or (pos_x2 - pos_x_american_dad < 150 and pos_x2 - pos_x_american_dad > -150))):
            count_american_dad += 1
            pos_x_american_dad = random.randint(1, 1900)
            pos_y_american_dad = 0 - random.randint(50, 2000)
            moveSprite(american_dad, pos_x_american_dad, pos_y_american_dad)
        if (((pos_x - pos_x_francine < 150 and pos_x - pos_x_francine > -150) or (pos_x2 - pos_x_francine < 150 and pos_x2 - pos_x_francine > -150)) and pos_y_francine > 700 and pos_y_francine < 900):
            count_american_dad += 1
            pos_x_francine = random.randint(1, 1900)
            pos_y_francine = 0 - random.randint(50, 2000)
            moveSprite(francine, pos_x_francine, pos_y_francine)
        if ((((pos_x - pos_x_hayley < 150 and pos_x - pos_x_hayley > -150) or (pos_x2 - pos_x_hayley < 150 and pos_x2 - pos_x_hayley > -150)) and pos_y_hayley > 700 and pos_y_hayley < 900)):
            count_american_dad += 1
            pos_x_hayley = random.randint(1, 1900)
            pos_y_hayley = 0 - random.randint(50, 2000)
            moveSprite(hayley, pos_x_hayley, pos_y_hayley)
        if ((((pos_x - pos_x_roger < 150 and pos_x - pos_x_roger > -150) or (pos_x2 - pos_x_roger < 150 and pos_x2 - pos_x_roger > -150)) and pos_y_roger > 700 and pos_y_roger < 900)):
            count_american_dad += 1
            pos_x_roger = random.randint(1, 1900)
            pos_y_roger = 0 - random.randint(50, 2000)
            moveSprite(roger, pos_x_roger, pos_y_roger)
        if (((pos_x - pos_x_steve < 150 and pos_x - pos_x_steve > -150) or (pos_x2 - pos_x_steve < 150 and pos_x2 - pos_x_steve > -150)) and pos_y_steve > 700 and pos_y_steve < 900):
            count_american_dad += 1
            pos_x_steve = random.randint(1, 1900)
            pos_y_steve = 0 - random.randint(50, 2000)
            moveSprite(steve, pos_x_steve, pos_y_steve)
        if (pos_y_victor > 700 and pos_y_victor < 900 and ((pos_x - pos_x_victor < 150 and pos_x - pos_x_victor > -150) or (pos_x2 - pos_x_victor < 150 and pos_x2 - pos_x_victor > -150))):
            count_famille_pirate += 1
            pos_x_victor = random.randint(1, 1900)
            pos_y_victor = 0 - random.randint(50, 2000)
            moveSprite(victor, pos_x_victor, pos_y_victor)
        #############ON CATCH#############
        #############ON LIFE LOST#############
        if (pos_y_american_dad > 1000):
            life -= 1
            pos_x_american_dad = random.randint(1, 1900)
            pos_y_american_dad = 0 - random.randint(50, 2000)
            moveSprite(american_dad, pos_x_american_dad, pos_y_american_dad)
            showSprite(american_dad)
        if (pos_y_francine > 1000):
            life -= 1
            pos_x_francine = random.randint(1, 1900)
            pos_y_francine = 0 - random.randint(50, 2000)
            moveSprite(francine, pos_x_francine, pos_y_francine)
            showSprite(francine)
        if (pos_y_hayley > 1000):
            life -= 1
            pos_x_hayley = random.randint(1, 1900)
            pos_y_hayley = 0 - random.randint(50, 2000)
            moveSprite(hayley, pos_x_hayley, pos_y_hayley)
            showSprite(hayley)
        if (pos_y_roger > 1000):
            life -= 1
            pos_x_roger = random.randint(1, 1900)
            pos_y_roger = 0 - random.randint(50, 2000)
            moveSprite(roger, pos_x_roger, pos_y_roger)
            showSprite(roger)
        if (pos_y_steve > 1000):
            life -= 1
            pos_x_steve = random.randint(1, 1900)
            pos_y_steve = 0 - random.randint(50, 2000)
            moveSprite(steve, pos_x_steve, pos_y_steve)
            showSprite(steve)
        if (pos_y_victor > 1000):
            life -= 1
            pos_x_victor = random.randint(1, 1900)
            pos_y_victor = 0 - random.randint(50, 2000)
            moveSprite(victor, pos_x_victor, pos_y_victor)
            showSprite(victor)
        if (life <= 0):
            exit()
        updateDisplay()

def menu():
    screen = screenSize(1920, 1080)
    while True:
        setBackgroundImage(["pictures/fond.png"])
        gameloop();
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()