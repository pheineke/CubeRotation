import pygame
import math
import math
import pygame
from pygame import gfxdraw
import random
import time

backgroundcolor = (255,255,255)
color = (255,0,0)
color0 = (255, 0, 0)    # Rot
color1 = (0, 255, 0)    # Grün
color2 = (0, 0, 255)    # Blau
color3 = (255, 255, 0)  # Gelb
color4 = (255, 0, 255)  # Magenta
color5 = (0, 255, 255)  # Cyan

loopvar = 0

# Set up the initial angle and velocity
angle = 0
velocity = 0.1
angle_step = math.pi / 2

pointsize = 4
pointsizetup = (pointsize, pointsize)

radius = 200
a = 100  # horizontaler Halbparameter des Ovals
b = 50  # vertikaler Halbparameter des Ovals
rotationtime = 1


recttemp = [[0, 0] for i in range(4)]
recttemp1 = [[0, 0] for i in range(4)]
# Calculate the points
rect = [[0, 0] for i in range(4)]
rect1 = [[0, 0] for i in range(4)]

def draw(angle):
    


    angles = [angle_step * i for i in range(4)]

    #Erase old rectangle:

    '''
    pygame.draw.rect(window, background, ((recttemp[0][0], recttemp[0][1]), pointsizetup))
    pygame.draw.rect(window, background, ((recttemp[1][0], recttemp[1][1]), pointsizetup))
    pygame.draw.rect(window, background, ((recttemp[2][0], recttemp[2][1]), pointsizetup))
    pygame.draw.rect(window, background, ((recttemp[3][0], recttemp[3][1]), pointsizetup))
    '''
    #>
    for i in range(0,4):
        pygame.draw.rect(window, backgroundcolor, ((recttemp[i][0], recttemp[i][1]), pointsizetup))

    for i in range(0,4):
        pygame.draw.rect(window, backgroundcolor, ((recttemp1[i][0], recttemp1[i][1]), pointsizetup))

    
    for i in range(0,4):
        for j in range(0,4):
            pygame.draw.line(window, backgroundcolor, (rect[i][0], rect[i][1]), (rect[j][0], rect[j][1]), 1)

    '''
    pygame.draw.rect(window, background, ((recttemp1[0][0], recttemp1[0][1]), pointsizetup))
    pygame.draw.rect(window, background, ((recttemp1[1][0], recttemp1[1][1]), pointsizetup))
    pygame.draw.rect(window, background, ((recttemp1[2][0], recttemp1[2][1]), pointsizetup))
    pygame.draw.rect(window, background, ((recttemp1[3][0], recttemp1[3][1]), pointsizetup))
    '''
    #>
    
    ####

    

    for i in range(4):
    # Berechnung der x- und y-Koordinaten
        x = center[0] + a * math.cos(angle + angles[i]) 
        y = center[1] + b * math.sin(angle + angles[i])
        
        # Aktualisierung der Positionen
        rect[i][0] = int(x)
        rect[i][1] = int(y)
        recttemp[i][0] = int(x)
        recttemp[i][1] = int(y)

    for i in range(4):
    # Berechnung der x- und y-Koordinaten
        x = center[0] + a * math.cos(angle + angles[i]) 
        y = center[1] + b * math.sin(angle + angles[i]) - 100
        
        # Aktualisierung der Positionen
        rect1[i][0] = int(x)
        rect1[i][1] = int(y)
        recttemp1[i][0] = int(x)
        recttemp1[i][1] = int(y)


    #Draw New Rectangle:

    '''
    pygame.draw.rect(window, color, ((rect[0][0], rect[0][1]), pointsizetup))
    pygame.draw.rect(window, color, ((rect[1][0], rect[1][1]), pointsizetup))
    pygame.draw.rect(window, color, ((rect[2][0], rect[2][1]), pointsizetup))
    pygame.draw.rect(window, color, ((rect[3][0], rect[3][1]), pointsizetup))
    '''
    #>
    for i in range(0,4):
        pygame.draw.rect(window, color, ((rect[i][0], rect[i][1]), pointsizetup))

    '''
    pygame.draw.rect(window, color, ((rect1[0][0], rect1[0][1]), pointsizetup))
    pygame.draw.rect(window, color, ((rect1[1][0], rect1[1][1]), pointsizetup))
    pygame.draw.rect(window, color, ((rect1[2][0], rect1[2][1]), pointsizetup))
    pygame.draw.rect(window, color, ((rect1[3][0], rect1[3][1]), pointsizetup))
    '''
    #>
    for i in range(0,4):
        pygame.draw.rect(window, color, ((rect1[i][0], rect1[i][1]), pointsizetup))


    ####

    pygame.display.update()



pygame.init()

window_size = (800, 600)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("main")
window.fill(backgroundcolor)
pygame.display.update()

# Set up the center of rotation and the radius
center = (window_size[0] // 2, window_size[1] // 2)


running = True
while running:
    x = pygame.event.get()
    for event in x:
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
