import pygame, sys
from pygame_functions import *

pygame.init()

res = (1920, 1080)

screen = pygame.display.set_mode(res)

width = screen.get_width()
height = screen.get_height()


def main_menu():
    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()

main_menu()