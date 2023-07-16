import pygame
import numpy as np

#USER INPUTS FOR DIFFERNT RENDER
RES = WIDTH, HEIGHT = 1600, 900
FPS = 10

#Pygame setup acording to res
pygame.init()
screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
running = True


#Polls for new ingame events (our case is the exit button)
#pygame.quit() means the user clicked the X in the window
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill("black")




    #Displays the game with flip()
    pygame.display.flip()

    #FrameRate
    clock.tick(FPS)

pygame.quit()



