import pygame
import numpy as np

#USER INPUTS FOR DIFFERNT RENDER
RES = WIDTH, HEIGHT = 1600, 900
FPS = 1

#USER INPUTS FOR TREE
ITERATIONS = 10

#Pygame setup acording to res
pygame.init()
screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
running = True

def branch(X, Y, CURRENT):
    if (CURRENT >= ITERATIONS):
        return    
    NEW_HEIGHT = Y - (10 * CURRENT)
    NEW_X1 = X-10*CURRENT
    NEW_X2 = X+10*CURRENT
    
    pygame.draw.line(screen, (255/CURRENT, 255/(ITERATIONS-CURRENT), 0), (X, Y), (NEW_X1, NEW_HEIGHT), width = 5)
    pygame.draw.line(screen, (255/CURRENT, 255/(ITERATIONS-CURRENT), 0), (X, Y), (NEW_X2, NEW_HEIGHT), width = 5)

    CURRENT = CURRENT + 1

    branch(NEW_X1, NEW_HEIGHT, CURRENT)
    branch(NEW_X2, NEW_HEIGHT, CURRENT)


    
            
    
    




#Polls for new ingame events (our case is the exit button)
#pygame.quit() means the user clicked the X in the window
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

 
    screen.fill("white")
    branch(WIDTH/2,HEIGHT, 1)
    


    

    #Displays the game with flip()
    pygame.display.flip()

    #FrameRate
    clock.tick(FPS)

pygame.quit()



