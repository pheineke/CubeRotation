import pygame
import math
import math
import pygame
from pygame import gfxdraw
import random
import time

background = (255,255,255)

loopvar = 0

# Set up the initial angle and velocity
angle = 0
velocity = 0.1
angle_step = math.pi / 2

pointsize = 4
pointsizetup = (pointsize, pointsize)

radius = 200
rotationtime = 1


recttemp = [[0, 0] for i in range(4)]

def draw(angle):
    color = (255,0,0)


    
    

    angles = [angle_step * i for i in range(4)]

    
    pygame.draw.rect(window, background, ((recttemp[0][0], recttemp[0][1]), pointsizetup))
    pygame.draw.rect(window, background, ((recttemp[1][0], recttemp[1][1]), pointsizetup))
    pygame.draw.rect(window, background, ((recttemp[2][0], recttemp[2][1]), pointsizetup))
    pygame.draw.rect(window, background, ((recttemp[3][0], recttemp[3][1]), pointsizetup))

    # Calculate the points
    rect = [[0, 0] for i in range(4)]
    for i in range(4):
        rect[i][0] = center[0] + radius * math.cos(angle + angles[i])
        rect[i][1] = center[1] + radius * math.sin(angle + angles[i])
        recttemp[i][0] = center[0] + radius * math.cos(angle + angles[i])
        recttemp[i][1] = center[1] + radius * math.sin(angle + angles[i])

    
    pygame.draw.rect(window, color, ((rect[0][0], rect[0][1]), pointsizetup))
    pygame.draw.rect(window, color, ((rect[1][0], rect[1][1]), pointsizetup))
    pygame.draw.rect(window, color, ((rect[2][0], rect[2][1]), pointsizetup))
    pygame.draw.rect(window, color, ((rect[3][0], rect[3][1]), pointsizetup))

    pygame.display.update()



pygame.init()

window_size = (800, 600)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("main")
window.fill(background)
pygame.display.update()

# Set up the center of rotation and the radius
center = (window_size[0] // 2, window_size[1] // 2)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    while loopvar < 10000:
        draw(angle)
        
        # Update the angle
        if angle == 360:
            angle = 0
        angle += velocity

        time.sleep(rotationtime)


        print(angle)
        print(radius)
        loopvar += 1
        
    

    # Update the display
    pygame.display.update()

pygame.quit()
