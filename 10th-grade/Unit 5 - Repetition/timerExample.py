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
pygame.time.set_timer(pygame.USEREVENT, 1000) 


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
places a spiral on surface rotated to degrees 
places countdown timer of seconds remaining 
when timer expires, spiral doubles in size 

'''
def drawScreen(sec, degrees):
    
    spiralPic = pygame.image.load("spiral.png").convert_alpha()
    if sec > 0 :
        spiralPic = pygame.image.transform.rotate(spiralPic, degrees)
        timeText, timeBounds = showMessage(str(sec), 60, "Consolas", w/2, h/2, RED)
        
    else: #no more seconds left on timer 
        spiralPic = pygame.transform.scale2x(spiralPic)
        timeText, timeBounds = showMessage(str("Boom!", 100, "Consolas", w/2, h/2, RED))

    #center the rotated image 
    spiralBounds = spiralPic.get_rect()
    spiralBounds.centerx = w/2 
    spiralBounds.centery = h/2 
    
    #blit
    surface.blit(spiralPic, spiralBounds)
    surface.blit(timeText, timeBounds)        

    return 42
    
    
#----------Main Program Loop ----------
def main():
    
    #set up the model variables
    seconds = 10 
    degrees = 0 

    
    #main program loop
    while(True):
        for event in pygame.event.get():
            if( event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                pygame.quit()
                sys.exit()
            
            # game logic goes here
            
        
   
        degrees += .5 
        
        # set background fill
        surface.fill(WHITE)
        
        # drawing code goes here
        
        drawScreen(seconds,degrees)
       
        pygame.display.update()
main()