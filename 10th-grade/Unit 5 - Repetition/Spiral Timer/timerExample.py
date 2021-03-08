#YOUR NAME Here
#HCP
#Assignment: Timer Example with Rotation
#Description:Program to rotate a spiral while counting down from 10

import pygame, sys, math,random

#initialize game engine
pygame.init()

#Set up drawing surface
w = 400
h = 400
size=(w,h)
surface = pygame.display.set_mode(size)

#set window title bar
pygame.display.set_caption("Count down")

#set up game timer
#every 1000 seconds, a userevent will be added to the event queue


#Color constants
BLACK = (  0,  0,  0)
WHITE = (255,255,255)
RED =   (255,  0,  0)
GREEN = (  0,255,  0)
BLUE =  (  0,  0,255)



def showMessage(words, size, font, x, y, color, bg = None):
    text_font = pygame.font.SysFont(font, size, True, False)
    text = text_font.render(words, True, color, bg)
    textBounds = text.get_rect()
    textBounds.center = (x, y)    
    
    #return bounding rectangle for click detection
    return text, textBounds

'''


'''
def drawScreen(sec, degrees):
    
    return 42
    
    
#----------Main Program Loop ----------
def main():
    
    #set up the model variables

    
    #main program loop
    while(True):
        for event in pygame.event.get():
            if( event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                pygame.quit()
                sys.exit()
            
            # game logic goes here
        
            
                
            
          

        # set background fill
        surface.fill(WHITE)
        
        # drawing code goes here
        
        drawScreen(seconds,degrees)
       
        pygame.display.update()
main()