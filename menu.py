from itertools import count
import pygame, sys
from pygame_functions import *
import random
import time

from real_menu import *

def gameloop():
    life = 3
    fin = 0
    speed_mult = 1
    scoritos = 0
    #########fin###############
    sprite_fin1 = makeSprite("pictures/american dad/tree.jpg")
    sprite_fin2 = makeSprite("pictures/famille pirate/tree (1).jpg")
    moveSprite(sprite_fin2, 640, 0)
    sprite_fin3 = makeSprite("pictures/family guys/tree (2).jpg")
    moveSprite(sprite_fin3, 1280, 0)
    sprite_fin4 = makeSprite("pictures/malcom/tree (3).jpg")
    moveSprite(sprite_fin4, 0, 600)
    sprite_fin5 = makeSprite("pictures/simpsons/tree (5).jpg")
    moveSprite(sprite_fin5, 640, 600)
    sprite_fin6 = makeSprite("pictures/soda/New Project (1).jpg")
    moveSprite(sprite_fin6, 1280, 600)
    
    #########fin###############
    #########life##############
    sprite_life1 = makeSprite("pictures/life.png")
    sprite_life2 = makeSprite("pictures/life.png")
    sprite_life3 = makeSprite("pictures/life.png")
    moveSprite(sprite_life2, 75, 0)
    moveSprite(sprite_life3, 150, 0)
    #########life##############
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
    ########american dad#######
    american_dad = makeSprite("pictures/american dad/Stan_smith.png")
    francine = makeSprite("pictures/american dad/francine_smith.png")
    hayley = makeSprite("pictures/american dad/Hayley_smith.png")
    roger = makeSprite("pictures/american dad/roger_smith.png")
    steve = makeSprite("pictures/american dad/steve_smith.png")
    pos_x_american_dad = random.randint(1, 1900)
    pos_y_american_dad = 0 - random.randint(100, 15000)
    pos_x_francine = random.randint(1, 1900)
    pos_y_francine = 0 - random.randint(100, 15000)
    pos_x_hayley = random.randint(1, 1900)
    pos_y_hayley = 0 - random.randint(100, 15000)
    pos_x_roger = random.randint(1, 1900)
    pos_y_roger = 0 - random.randint(100, 15000)
    pos_x_steve = random.randint(1, 1900)
    pos_y_steve = 0 - random.randint(100, 15000)
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
    pos_y_dewey = 0 - random.randint(100, 15000)
    pos_x_francis = random.randint(1, 1900)
    pos_y_francis = 0 - random.randint(100, 15000)
    pos_x_hal = random.randint(1, 1900)
    pos_y_hal = 0 - random.randint(100, 15000)
    pos_x_lois = random.randint(1, 1900)
    pos_y_lois = 0 - random.randint(100, 15000)
    pos_x_malcom = random.randint(1, 1900)
    pos_y_malcom = 0 - random.randint(100, 15000)
    pos_x_rise = random.randint(1, 1900)
    pos_y_rise = 0 - random.randint(100, 15000)
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
    adam = makeSprite("pictures/soda/SODA_Adam01.png")
    babeth = makeSprite("pictures/soda/SODA_Babeth.png")
    eve = makeSprite("pictures/soda/SODA_Eve.png")
    gisele = makeSprite("pictures/soda/SODA_Gisele.png")
    michel = makeSprite("pictures/soda/SODA_Michel.png")
    slimane = makeSprite("pictures/soda/SODA_Slimane.png")
    pos_x_adam = random.randint(1, 1900)
    pos_y_adam = 0 - random.randint(100, 15000)
    pos_x_babeth = random.randint(1, 1900)
    pos_y_babeth = 0 - random.randint(100, 15000)
    pos_x_eve = random.randint(1, 1900)
    pos_y_eve = 0 - random.randint(100, 15000)
    pos_x_gisele = random.randint(1, 1900)
    pos_y_gisele = 0 - random.randint(100, 15000)
    pos_x_michel = random.randint(1, 1900)
    pos_y_michel = 0 - random.randint(100, 15000)
    pos_x_slimane = random.randint(1, 1900)
    pos_y_slimane = 0 - random.randint(100, 15000)
    moveSprite(adam, pos_x_adam, pos_y_adam)
    showSprite(adam)
    moveSprite(babeth, pos_x_babeth, pos_y_babeth)
    showSprite(babeth)
    moveSprite(eve, pos_x_eve, pos_y_eve)
    showSprite(eve)
    moveSprite(gisele, pos_x_gisele, pos_y_gisele)
    showSprite(gisele)
    moveSprite(michel, pos_x_michel, pos_y_michel)
    showSprite(michel)
    moveSprite(slimane, pos_x_slimane, pos_y_slimane)
    showSprite(slimane)
    count_adam = 0
    ########soda###############
    ########famille pirate#####
    bigorneau = makeSprite("pictures/famille pirate/bigorneau.png")
    mac = makeSprite("pictures/famille pirate/mac.png")
    scampi = makeSprite("pictures/famille pirate/scampi.png")
    victor = makeSprite("pictures/famille pirate/victor.png")
    pos_x_bigorneau = random.randint(1, 1900)
    pos_y_bigorneau = 0 - random.randint(100, 15000)
    pos_x_mac = random.randint(1, 1900)
    pos_y_mac = 0 - random.randint(100, 15000)
    pos_x_scampi = random.randint(1, 1900)
    pos_y_scampi = 0 - random.randint(100, 15000)
    pos_x_victor = random.randint(1, 1900)
    pos_y_victor = 0 - random.randint(100, 15000)
    moveSprite(bigorneau, pos_x_bigorneau, pos_y_bigorneau)
    showSprite(bigorneau)
    moveSprite(mac, pos_x_mac, pos_y_mac)
    showSprite(mac)
    moveSprite(scampi, pos_x_scampi, pos_y_scampi)
    showSprite(scampi)
    moveSprite(victor, pos_x_victor, pos_y_victor)
    showSprite(victor)
    count_bigorneau = 0
    ########famille pirate#####
    ########simpsons###########
    bart = makeSprite("pictures/simpsons/bart.png")
    homer = makeSprite("pictures/simpsons/homer.png")
    lisa = makeSprite("pictures/simpsons/lisa.png")
    maggie = makeSprite("pictures/simpsons/maggie.png")
    marge = makeSprite("pictures/simpsons/Marge.png")
    pos_x_bart = random.randint(1, 1900)
    pos_y_bart = 0 - random.randint(100, 15000)
    pos_x_homer = random.randint(1, 1900)
    pos_y_homer = 0 - random.randint(100, 15000)
    pos_x_lisa = random.randint(1, 1900)
    pos_y_lisa = 0 - random.randint(100, 15000)
    pos_x_maggie = random.randint(1, 1900)
    pos_y_maggie = 0 - random.randint(100, 15000)
    pos_x_marge = random.randint(1, 1900)
    pos_y_marge = 0 - random.randint(100, 15000)
    moveSprite(bart, pos_x_bart, pos_y_bart)
    showSprite(bart)
    moveSprite(homer, pos_x_homer, pos_y_homer)
    showSprite(homer)
    moveSprite(lisa, pos_x_lisa, pos_y_lisa)
    showSprite(lisa)
    moveSprite(maggie, pos_x_maggie, pos_y_maggie)
    showSprite(maggie)
    moveSprite(marge, pos_x_marge, pos_y_marge)
    showSprite(marge)
    count_bart = 0
    ########simpsons###########
    ########family guys########
    chris_griffin = makeSprite("pictures/family guys/chris_griffin.png")
    Lois_griffin = makeSprite("pictures/family guys/Lois_griffin.png")
    meg_griffin = makeSprite("pictures/family guys/meg_griffin.png")
    peter_griffin = makeSprite("pictures/family guys/peter_griffin.png")
    ryan_griffin = makeSprite("pictures/family guys/ryan_griffin.png")
    stewie_griffin = makeSprite("pictures/family guys/stewie_griffin.png")
    pos_x_chris_griffin = random.randint(1, 1900)
    pos_y_chris_griffin = 0 - random.randint(100, 15000)
    pos_x_Lois_griffin = random.randint(1, 1900)
    pos_y_Lois_griffin = 0 - random.randint(100, 15000)
    pos_x_meg_griffin = random.randint(1, 1900)
    pos_y_meg_griffin = 0 - random.randint(100, 15000)
    pos_x_peter_griffin = random.randint(1, 1900)
    pos_y_peter_griffin = 0 - random.randint(100, 15000)
    pos_x_ryan_griffin = random.randint(1, 1900)
    pos_y_ryan_griffin = 0 - random.randint(100, 15000)
    pos_x_stewie_griffin = random.randint(1, 1900)
    pos_y_stewie_griffin = 0 - random.randint(100, 15000)
    moveSprite(chris_griffin, pos_x_chris_griffin, pos_y_chris_griffin)
    showSprite(chris_griffin)
    moveSprite(Lois_griffin, pos_x_Lois_griffin, pos_y_Lois_griffin)
    showSprite(Lois_griffin)
    moveSprite(meg_griffin, pos_x_meg_griffin, pos_y_meg_griffin)
    showSprite(meg_griffin)
    moveSprite(peter_griffin, pos_x_peter_griffin, pos_y_peter_griffin)
    showSprite(peter_griffin)
    moveSprite(ryan_griffin, pos_x_ryan_griffin, pos_y_ryan_griffin)
    showSprite(ryan_griffin)
    moveSprite(stewie_griffin, pos_x_stewie_griffin, pos_y_stewie_griffin)
    showSprite(stewie_griffin)
    count_chris_griffin = 0
    ########family guys########
    while True:
        score = makeLabel(str(scoritos), 40, 1850, 0, (0, 0, 0), "Agency FB", "white")
        showLabel(score)
        pos_y_american_dad += 3 * speed_mult
        pos_y_francine += 3 * speed_mult
        pos_y_hayley += 3 * speed_mult
        pos_y_roger += 3 * speed_mult
        pos_y_steve += 3 * speed_mult
        pos_y_dewey += 3 * speed_mult
        pos_y_malcom += 3 * speed_mult
        pos_y_francis += 3 * speed_mult
        pos_y_hal += 3 * speed_mult
        pos_y_lois += 3 * speed_mult
        pos_y_rise += 3 * speed_mult
        pos_y_adam += 3 * speed_mult
        pos_y_babeth += 3 * speed_mult
        pos_y_eve += 3 * speed_mult
        pos_y_gisele += 3 * speed_mult
        pos_y_michel += 3 * speed_mult
        pos_y_slimane += 3 * speed_mult
        pos_y_bigorneau += 3 * speed_mult
        pos_y_mac += 3 * speed_mult
        pos_y_scampi += 3 * speed_mult
        pos_y_victor += 3 * speed_mult
        pos_y_bart += 3 * speed_mult
        pos_y_homer += 3 * speed_mult
        pos_y_lisa += 3 * speed_mult
        pos_y_maggie += 3 * speed_mult
        pos_y_marge += 3 * speed_mult
        pos_y_chris_griffin += 3 * speed_mult
        pos_y_Lois_griffin += 3 * speed_mult
        pos_y_meg_griffin += 3 * speed_mult
        pos_y_peter_griffin += 3 * speed_mult
        pos_y_ryan_griffin += 3 * speed_mult
        pos_y_stewie_griffin += 3 * speed_mult
        moveSprite(american_dad, pos_x_american_dad, pos_y_american_dad)
        moveSprite(francine, pos_x_francine, pos_y_francine)
        moveSprite(hayley, pos_x_hayley, pos_y_hayley)
        moveSprite(roger, pos_x_roger, pos_y_roger)
        moveSprite(steve, pos_x_steve, pos_y_steve)
        moveSprite(victor, pos_x_victor, pos_y_victor)
        moveSprite(dewey, pos_x_dewey, pos_y_dewey)
        moveSprite(malcom, pos_x_malcom, pos_y_malcom)
        moveSprite(francis, pos_x_francis, pos_y_francis)
        moveSprite(hal, pos_x_hal, pos_y_hal)
        moveSprite(lois, pos_x_lois, pos_y_lois)
        moveSprite(rise, pos_x_rise, pos_y_rise)
        moveSprite(adam, pos_x_adam, pos_y_adam)
        moveSprite(babeth, pos_x_babeth, pos_y_babeth)
        moveSprite(eve, pos_x_eve, pos_y_eve)
        moveSprite(gisele, pos_x_gisele, pos_y_gisele)
        moveSprite(michel, pos_x_michel, pos_y_michel)
        moveSprite(slimane, pos_x_slimane, pos_y_slimane)
        moveSprite(bigorneau, pos_x_bigorneau, pos_y_bigorneau)
        moveSprite(mac, pos_x_mac, pos_y_mac)
        moveSprite(scampi, pos_x_scampi, pos_y_scampi)
        moveSprite(victor, pos_x_victor, pos_y_victor)
        moveSprite(bart, pos_x_bart, pos_y_bart)
        moveSprite(homer, pos_x_homer, pos_y_homer)
        moveSprite(lisa, pos_x_lisa, pos_y_lisa)
        moveSprite(maggie, pos_x_maggie, pos_y_maggie)
        moveSprite(marge, pos_x_marge, pos_y_marge)
        moveSprite(chris_griffin, pos_x_chris_griffin, pos_y_chris_griffin)
        moveSprite(Lois_griffin, pos_x_Lois_griffin, pos_y_Lois_griffin)
        moveSprite(meg_griffin, pos_x_meg_griffin, pos_y_meg_griffin)
        moveSprite(peter_griffin, pos_x_peter_griffin, pos_y_peter_griffin)
        moveSprite(ryan_griffin, pos_x_ryan_griffin, pos_y_ryan_griffin)
        moveSprite(stewie_griffin, pos_x_stewie_griffin, pos_y_stewie_griffin)
        if life == 3:
            showSprite(sprite_life1)
            showSprite(sprite_life2)
            showSprite(sprite_life3)
        if life == 2:
            showSprite(sprite_life1)
            showSprite(sprite_life2)
            hideSprite(sprite_life3)
        if life == 1:
            showSprite(sprite_life1)
            hideSprite(sprite_life2)
            hideSprite(sprite_life3)
        if life == 0:
            hideSprite(sprite_life1)
            hideSprite(sprite_life2)
            hideSprite(sprite_life3)
        pos_y_victor += 3 * speed_mult
        speed_mult += 0.01
        if (is_moving_left == True):
                    pos_x -= 30
                    moveSprite(bucket, pos_x, 800)
        if (is_moving_right == True):
                    pos_x += 30
                    moveSprite(bucket, pos_x, 800)
        if (is_moving_left2 == True):
                    pos_x2 -= 30
                    moveSprite(bucket2, pos_x2, 800)
        if (is_moving_right2 == True):
                    pos_x2 += 30
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
                if keyPressed("space"):
                    life -= 1
            elif (is_moving_left == True or is_moving_right == True):
                is_moving_left = False
                is_moving_right = False
            elif (is_moving_left2 == True or is_moving_right2 == True):
                is_moving_left2 = False
                is_moving_right2 = False
        #############ON CATCH#############
        if (pos_y_american_dad > 700 and pos_y_american_dad < 900 and ((pos_x - pos_x_american_dad < 150 and pos_x - pos_x_american_dad > -150) or (pos_x2 - pos_x_american_dad < 150 and pos_x2 - pos_x_american_dad > -150))):
            count_american_dad += 1
            pos_x_american_dad = random.randint(1, 1900)
            pos_y_american_dad = 0 - random.randint(50, 15000)
            moveSprite(american_dad, pos_x_american_dad, pos_y_american_dad)
            hideSprite(american_dad)
            scoritos += 1
        if (((pos_x - pos_x_francine < 150 and pos_x - pos_x_francine > -150) or (pos_x2 - pos_x_francine < 150 and pos_x2 - pos_x_francine > -150)) and pos_y_francine > 700 and pos_y_francine < 900):
            count_american_dad += 1
            pos_x_francine = random.randint(1, 1900)
            pos_y_francine = 0 - random.randint(50, 15000)
            moveSprite(francine, pos_x_francine, pos_y_francine)
            hideSprite(francine)
            scoritos += 1
        if ((((pos_x - pos_x_hayley < 150 and pos_x - pos_x_hayley > -150) or (pos_x2 - pos_x_hayley < 150 and pos_x2 - pos_x_hayley > -150)) and pos_y_hayley > 700 and pos_y_hayley < 900)):
            count_american_dad += 1
            pos_x_hayley = random.randint(1, 1900)
            pos_y_hayley = 0 - random.randint(50, 15000)
            moveSprite(hayley, pos_x_hayley, pos_y_hayley)
            hideSprite(hayley)
            scoritos += 1
        if ((((pos_x - pos_x_roger < 150 and pos_x - pos_x_roger > -150) or (pos_x2 - pos_x_roger < 150 and pos_x2 - pos_x_roger > -150)) and pos_y_roger > 700 and pos_y_roger < 900)):
            count_american_dad += 1
            pos_x_roger = random.randint(1, 1900)
            pos_y_roger = 0 - random.randint(50, 15000)
            moveSprite(roger, pos_x_roger, pos_y_roger)
            hideSprite(roger)
            scoritos += 1
        if (((pos_x - pos_x_steve < 150 and pos_x - pos_x_steve > -150) or (pos_x2 - pos_x_steve < 150 and pos_x2 - pos_x_steve > -150)) and pos_y_steve > 700 and pos_y_steve < 900):
            count_american_dad += 1
            pos_x_steve = random.randint(1, 1900)
            pos_y_steve = 0 - random.randint(50, 15000)
            moveSprite(steve, pos_x_steve, pos_y_steve)
            hideSprite(steve)
            scoritos += 1
        #############"PIRATE"#############
        if (pos_y_bigorneau > 700 and pos_y_bigorneau < 900 and ((pos_x - pos_x_bigorneau < 150 and pos_x - pos_x_bigorneau > -150) or (pos_x2 - pos_x_bigorneau < 150 and pos_x2 - pos_x_bigorneau > -150))):
            count_bigorneau += 1
            pos_x_bigorneau = random.randint(1, 1900)
            pos_y_bigorneau = 0 - random.randint(50, 15000)
            moveSprite(bigorneau, pos_x_bigorneau, pos_y_bigorneau)
            hideSprite(bigorneau)
            scoritos += 1
        if (((pos_x - pos_x_mac < 150 and pos_x - pos_x_mac > -150) or (pos_x2 - pos_x_mac < 150 and pos_x2 - pos_x_mac > -150)) and pos_y_mac > 700 and pos_y_mac < 900):
            count_american_dad += 1
            pos_x_mac = random.randint(1, 1900)
            pos_y_mac = 0 - random.randint(50, 15000)
            moveSprite(mac, pos_x_mac, pos_y_mac)
            hideSprite(mac)
            scoritos += 1
        if ((((pos_x - pos_x_scampi < 150 and pos_x - pos_x_scampi > -150) or (pos_x2 - pos_x_scampi < 150 and pos_x2 - pos_x_scampi > -150)) and pos_y_scampi > 700 and pos_y_scampi < 900)):
            count_bigorneau += 1
            pos_x_scampi = random.randint(1, 1900)
            pos_y_scampi = 0 - random.randint(50, 15000)
            moveSprite(scampi, pos_x_scampi, pos_y_scampi)
            hideSprite(scampi)
            scoritos += 1
        if ((((pos_x - pos_x_victor < 150 and pos_x - pos_x_victor > -150) or (pos_x2 - pos_x_victor < 150 and pos_x2 - pos_x_victor > -150)) and pos_y_victor > 700 and pos_y_victor < 900)):
            count_bigorneau += 1
            pos_x_victor = random.randint(1, 1900)
            pos_y_victor = 0 - random.randint(50, 15000)
            moveSprite(victor, pos_x_victor, pos_y_victor)
            hideSprite(victor)
            scoritos += 1
        #############"PIRATE"#############
        if (pos_y_dewey > 700 and pos_y_dewey < 900 and ((pos_x - pos_x_dewey < 150 and pos_x - pos_x_dewey > -150) or (pos_x2 - pos_x_dewey < 150 and pos_x2 - pos_x_dewey > -150))):
            count_dewey += 1
            pos_x_dewey = random.randint(1, 1900)
            pos_y_dewey = 0 - random.randint(50, 15000)
            moveSprite(dewey, pos_x_dewey, pos_y_dewey)
            hideSprite(dewey)
            scoritos += 1
        if (((pos_x - pos_x_francis < 150 and pos_x - pos_x_francis > -150) or (pos_x2 - pos_x_francis < 150 and pos_x2 - pos_x_francis > -150)) and pos_y_francis > 700 and pos_y_francis < 900):
            count_dewey += 1
            pos_x_francis = random.randint(1, 1900)
            pos_y_francis = 0 - random.randint(50, 15000)
            moveSprite(francis, pos_x_francis, pos_y_francis)
            hideSprite(francis)
            scoritos += 1
        if ((((pos_x - pos_x_hal < 150 and pos_x - pos_x_hal > -150) or (pos_x2 - pos_x_hal < 150 and pos_x2 - pos_x_hal > -150)) and pos_y_hal > 700 and pos_y_hal < 900)):
            count_dewey += 1
            pos_x_hal = random.randint(1, 1900)
            pos_y_hal = 0 - random.randint(50, 15000)
            moveSprite(hal, pos_x_hal, pos_y_hal)
            hideSprite(hal)
            scoritos += 1
        if ((((pos_x - pos_x_lois < 150 and pos_x - pos_x_lois > -150) or (pos_x2 - pos_x_lois < 150 and pos_x2 - pos_x_lois > -150)) and pos_y_lois > 700 and pos_y_lois < 900)):
            count_dewey += 1
            pos_x_lois = random.randint(1, 1900)
            pos_y_lois = 0 - random.randint(50, 15000)
            moveSprite(lois, pos_x_lois, pos_y_lois)
            hideSprite(lois)
            scoritos += 1
        if ((((pos_x - pos_x_malcom < 150 and pos_x - pos_x_malcom > -150) or (pos_x2 - pos_x_malcom < 150 and pos_x2 - pos_x_malcom > -150)) and pos_y_malcom > 700 and pos_y_malcom < 900)):
            count_dewey += 1
            pos_x_malcom = random.randint(1, 1900)
            pos_y_malcom = 0 - random.randint(50, 15000)
            moveSprite(malcom, pos_x_malcom, pos_y_malcom)
            hideSprite(malcom)
            scoritos += 1
        if ((((pos_x - pos_x_rise < 150 and pos_x - pos_x_rise > -150) or (pos_x2 - pos_x_rise < 150 and pos_x2 - pos_x_rise > -150)) and pos_y_rise > 700 and pos_y_rise < 900)):
            count_dewey += 1
            pos_x_rise = random.randint(1, 1900)
            pos_y_rise = 0 - random.randint(50, 15000)
            moveSprite(rise, pos_x_rise, pos_y_rise)
            hideSprite(rise)
            scoritos += 1
        ############################""
        if (pos_y_bart > 700 and pos_y_bart < 900 and ((pos_x - pos_x_bart < 150 and pos_x - pos_x_bart > -150) or (pos_x2 - pos_x_bart < 150 and pos_x2 - pos_x_bart > -150))):
            count_bart += 1
            pos_x_bart = random.randint(1, 1900)
            pos_y_bart = 0 - random.randint(50, 15000)
            moveSprite(bart, pos_x_bart, pos_y_bart)
            hideSprite(bart)
            scoritos += 1
        if (((pos_x - pos_x_homer < 150 and pos_x - pos_x_homer > -150) or (pos_x2 - pos_x_homer < 150 and pos_x2 - pos_x_homer > -150)) and pos_y_homer > 700 and pos_y_homer < 900):
            count_bart += 1
            pos_x_homer = random.randint(1, 1900)
            pos_y_homer = 0 - random.randint(50, 15000)
            moveSprite(homer, pos_x_homer, pos_y_homer)
            hideSprite(homer)
            scoritos += 1
        if ((((pos_x - pos_x_marge < 150 and pos_x - pos_x_marge > -150) or (pos_x2 - pos_x_marge < 150 and pos_x2 - pos_x_marge > -150)) and pos_y_marge > 700 and pos_y_marge < 900)):
            count_bart += 1
            pos_x_marge = random.randint(1, 1900)
            pos_y_marge = 0 - random.randint(50, 15000)
            moveSprite(marge, pos_x_marge, pos_y_marge)
            hideSprite(marge)
            scoritos += 1
        if ((((pos_x - pos_x_maggie < 150 and pos_x - pos_x_maggie > -150) or (pos_x2 - pos_x_maggie < 150 and pos_x2 - pos_x_maggie > -150)) and pos_y_maggie > 700 and pos_y_maggie < 900)):
            count_bart += 1
            pos_x_maggie = random.randint(1, 1900)
            pos_y_maggie = 0 - random.randint(50, 15000)
            moveSprite(maggie, pos_x_maggie, pos_y_maggie)
            hideSprite(maggie)
            scoritos += 1
        if ((((pos_x - pos_x_lisa < 150 and pos_x - pos_x_lisa > -150) or (pos_x2 - pos_x_lisa < 150 and pos_x2 - pos_x_lisa > -150)) and pos_y_lisa > 700 and pos_y_lisa < 900)):
            count_bart += 1
            pos_x_lisa = random.randint(1, 1900)
            pos_y_lisa = 0 - random.randint(50, 15000)
            moveSprite(lisa, pos_x_lisa, pos_y_lisa)
            hideSprite(lisa)
            scoritos += 1
        ############################""
        if (pos_y_chris_griffin > 700 and pos_y_chris_griffin < 900 and ((pos_x - pos_x_chris_griffin < 150 and pos_x - pos_x_chris_griffin > -150) or (pos_x2 - pos_x_chris_griffin < 150 and pos_x2 - pos_x_chris_griffin > -150))):
            count_chris_griffin += 1
            pos_x_chris_griffin = random.randint(1, 1900)
            pos_y_chris_griffin = 0 - random.randint(50, 15000)
            moveSprite(chris_griffin, pos_x_chris_griffin, pos_y_chris_griffin)
            hideSprite(chris_griffin)
            scoritos += 1
        if (((pos_x - pos_x_Lois_griffin < 150 and pos_x - pos_x_Lois_griffin > -150) or (pos_x2 - pos_x_Lois_griffin < 150 and pos_x2 - pos_x_Lois_griffin > -150)) and pos_y_Lois_griffin > 700 and pos_y_Lois_griffin < 900):
            count_chris_griffin += 1
            pos_x_Lois_griffin = random.randint(1, 1900)
            pos_y_Lois_griffin = 0 - random.randint(50, 15000)
            moveSprite(Lois_griffin, pos_x_Lois_griffin, pos_y_Lois_griffin)
            hideSprite(Lois_griffin)
            scoritos += 1
        if ((((pos_x - pos_x_meg_griffin < 150 and pos_x - pos_x_meg_griffin > -150) or (pos_x2 - pos_x_meg_griffin < 150 and pos_x2 - pos_x_meg_griffin > -150)) and pos_y_meg_griffin > 700 and pos_y_meg_griffin < 900)):
            count_chris_griffin += 1
            pos_x_meg_griffin = random.randint(1, 1900)
            pos_y_meg_griffin = 0 - random.randint(50, 15000)
            moveSprite(meg_griffin, pos_x_meg_griffin, pos_y_meg_griffin)
            hideSprite(meg_griffin)
            scoritos += 1
        if ((((pos_x - pos_x_peter_griffin < 150 and pos_x - pos_x_peter_griffin > -150) or (pos_x2 - pos_x_peter_griffin < 150 and pos_x2 - pos_x_peter_griffin > -150)) and pos_y_peter_griffin > 700 and pos_y_peter_griffin < 900)):
            count_chris_griffin += 1
            pos_x_peter_griffin = random.randint(1, 1900)
            pos_y_peter_griffin = 0 - random.randint(50, 15000)
            moveSprite(peter_griffin, pos_x_peter_griffin, pos_y_peter_griffin)
            hideSprite(peter_griffin)
            scoritos += 1
        if ((((pos_x - pos_x_ryan_griffin < 150 and pos_x - pos_x_ryan_griffin > -150) or (pos_x2 - pos_x_ryan_griffin < 150 and pos_x2 - pos_x_ryan_griffin > -150)) and pos_y_ryan_griffin > 700 and pos_y_ryan_griffin < 900)):
            count_chris_griffin += 1
            pos_x_ryan_griffin = random.randint(1, 1900)
            pos_y_ryan_griffin = 0 - random.randint(50, 15000)
            moveSprite(ryan_griffin, pos_x_ryan_griffin, pos_y_ryan_griffin)
            hideSprite(ryan_griffin)
            scoritos += 1
        ##############################
        if (pos_y_adam > 700 and pos_y_adam < 900 and ((pos_x - pos_x_adam < 150 and pos_x - pos_x_adam > -150) or (pos_x2 - pos_x_adam < 150 and pos_x2 - pos_x_adam > -150))):
            count_adam += 1
            pos_x_adam = random.randint(1, 1900)
            pos_y_adam = 0 - random.randint(50, 15000)
            moveSprite(adam, pos_x_adam, pos_y_adam)
            hideSprite(adam)
            scoritos += 1
        if (((pos_x - pos_x_babeth < 150 and pos_x - pos_x_babeth > -150) or (pos_x2 - pos_x_babeth < 150 and pos_x2 - pos_x_babeth > -150)) and pos_y_babeth > 700 and pos_y_babeth < 900):
            count_adam += 1
            pos_x_babeth = random.randint(1, 1900)
            pos_y_babeth = 0 - random.randint(50, 15000)
            moveSprite(babeth, pos_x_babeth, pos_y_babeth)
            hideSprite(babeth)
            scoritos += 1
        if ((((pos_x - pos_x_eve < 150 and pos_x - pos_x_eve > -150) or (pos_x2 - pos_x_eve < 150 and pos_x2 - pos_x_eve > -150)) and pos_y_eve > 700 and pos_y_eve < 900)):
            count_adam += 1
            pos_x_eve = random.randint(1, 1900)
            pos_y_eve = 0 - random.randint(50, 15000)
            moveSprite(eve, pos_x_eve, pos_y_eve)
            hideSprite(eve)
            scoritos += 1
        if ((((pos_x - pos_x_gisele < 150 and pos_x - pos_x_gisele > -150) or (pos_x2 - pos_x_gisele < 150 and pos_x2 - pos_x_gisele > -150)) and pos_y_gisele > 700 and pos_y_gisele < 900)):
            count_adam += 1
            pos_x_gisele = random.randint(1, 1900)
            pos_y_gisele = 0 - random.randint(50, 15000)
            moveSprite(gisele, pos_x_gisele, pos_y_gisele)
            hideSprite(gisele)
            scoritos += 1
        if ((((pos_x - pos_x_michel < 150 and pos_x - pos_x_michel > -150) or (pos_x2 - pos_x_michel < 150 and pos_x2 - pos_x_michel > -150)) and pos_y_michel > 700 and pos_y_michel < 900)):
            count_adam += 1
            pos_x_michel = random.randint(1, 1900)
            pos_y_michel = 0 - random.randint(50, 15000)
            moveSprite(michel, pos_x_michel, pos_y_michel)
            hideSprite(michel)
            scoritos += 1
        if ((((pos_x - pos_x_slimane < 150 and pos_x - pos_x_slimane > -150) or (pos_x2 - pos_x_slimane < 150 and pos_x2 - pos_x_slimane > -150)) and pos_y_slimane > 700 and pos_y_slimane < 900)):
            count_adam += 1
            pos_x_slimane = random.randint(1, 1900)
            pos_y_slimane = 0 - random.randint(50, 15000)
            moveSprite(slimane, pos_x_slimane, pos_y_slimane)
            hideSprite(slimane)
            scoritos += 1
        #############ON CATCH#############
        #############ON LIFE LOST#############
        if (pos_y_american_dad > 1000):
            life -= 1
            pos_x_american_dad = random.randint(1, 1900)
            pos_y_american_dad = 0 - random.randint(50, 15000)
            moveSprite(american_dad, pos_x_american_dad, pos_y_american_dad)
            # showSprite(american_dad)
        if (pos_y_francine > 1000):
            life -= 1
            pos_x_francine = random.randint(1, 1900)
            pos_y_francine = 0 - random.randint(50, 15000)
            moveSprite(francine, pos_x_francine, pos_y_francine)
            # showSprite(francine)
        if (pos_y_hayley > 1000):
            life -= 1
            pos_x_hayley = random.randint(1, 1900)
            pos_y_hayley = 0 - random.randint(50, 15000)
            moveSprite(hayley, pos_x_hayley, pos_y_hayley)
            # showSprite(hayley)
        if (pos_y_roger > 1000):
            life -= 1
            pos_x_roger = random.randint(1, 1900)
            pos_y_roger = 0 - random.randint(50, 15000)
            moveSprite(roger, pos_x_roger, pos_y_roger)
            # showSprite(roger)
        if (pos_y_steve > 1000):
            life -= 1
            pos_x_steve = random.randint(1, 1900)
            pos_y_steve = 0 - random.randint(50, 15000)
            moveSprite(steve, pos_x_steve, pos_y_steve)
            # showSprite(steve)
        #########"pirate"#############
        if (pos_y_bigorneau > 1000):
            life -= 1
            pos_x_bigorneau = random.randint(1, 1900)
            pos_y_bigorneau = 0 - random.randint(50, 15000)
            moveSprite(bigorneau, pos_x_bigorneau, pos_y_bigorneau)
            # showSprite(bigorneau)
        if (pos_y_victor > 1000):
            life -= 1
            pos_x_victor = random.randint(1, 1900)
            pos_y_victor = 0 - random.randint(50, 15000)
            moveSprite(victor, pos_x_victor, pos_y_victor)
            # showSprite(victor)
        if (pos_y_mac > 1000):
            life -= 1
            pos_x_mac = random.randint(1, 1900)
            pos_y_mac = 0 - random.randint(50, 15000)
            moveSprite(mac, pos_x_mac, pos_y_mac)
            # showSprite(mac)
        #########"fin"################
        if (count_adam >= 4 and count_american_dad >= 4 and count_bart >= 4 and count_bigorneau >= 4 and count_chris_griffin >= 4 and count_dewey >= 4 or keyPressed("p")):
            showSprite(sprite_fin1)
            showSprite(sprite_fin2)
            showSprite(sprite_fin3)
            showSprite(sprite_fin4)
            showSprite(sprite_fin5)
            showSprite(sprite_fin6)
            time.sleep(10)
            exit()
        #########"pirate"#############
        if (life <= 0):
            exit()
        updateDisplay()

def menu():
    screen = screenSize(1920, 1080)
    while True:
        real_menu();
        setBackgroundImage(["pictures/fond.png"])
        gameloop();
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()