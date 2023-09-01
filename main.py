import math
import pygame
from pygame import gfxdraw
import random
import time


def paintpixel(x,y):
    x = int(x)
    y = int(y)
    gfxdraw.pixel(window, int(x), int(y), color)
    gfxdraw.pixel(window, int(x), int(y+1), color)
    gfxdraw.pixel(window, int(x+1), int(y), color)
    gfxdraw.pixel(window, int(x+1), int(y+1), color)

pygame.init()

window_size = [800,600]
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("main")
window.fill((255,255,255))

color = (255, 0, 0)





pygame.display.update()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    x = 0
    while x < 10000:
        center = [400,300]
        angle = 30
        x_new = center[0] + 50 * math.cos(angle)
        y_new = center[1] + 50 * math.sin(angle)
        paintpixel(x_new,y_new)
        x=+1

        angle=+10
        time.sleep(0.00000001)
        pygame.display.update()



    pygame.display.update()


    



    

