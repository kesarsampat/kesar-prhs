'''
Student Name: Kesar 
Game title: House 
Period: 3
Features of Game: 
'''

import pygame, sys                                      #pulls in the special code functions for pygame
pygame.init()                                           #initialize game engine

w=800                                                   #Open and set window size
h=int(16/20 *w)
xu=w/20
yu=h/16

#must code graphics to auto resize based on window size
size=(w,h)
surface = pygame.display.set_mode(size)

pygame.display.set_caption("This is my house")          #set window title

#declare global variables here

BLACK    = (   0,   0,   0)                             #Color Constants 
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
BROWN     = ( 130,  64, 2)
LT_BLUE    = ( 154,  222, 241)
YELLOW     =(255,255,0)
M_BLUE    = (122,200,226)
NAVY = (60,50,168)


#other global variables (WARNING: use sparingly):





#clock = pygame.time.Clock()                            # Manage timing for screen updates
                                                        # Uncomment when timing/animation is needed


#Program helper functions:
def drawWindows(x,y):
    pygame.draw.rect(surface, YELLOW, [x,y, xu, yu])
    
    
def drawHouse():
    #base
    pygame.draw.rect(surface,M_BLUE,[7*xu,h/2,6*xu,5*yu],0)
    
    #roof
    roofPoints=[(w/2,h/4), (13*xu,8*yu ),(7*xu,h/2)]
    pygame.draw.polygon(surface,BROWN,roofPoints,0)

    #door
    pygame.draw.rect(surface,LT_BLUE,[9.5*xu,11*yu,xu,2*yu],0)
    pygame.draw.ellipse(surface,LT_BLUE,[9.5*xu,10.5*yu,xu,yu],0)

    #grass
    pygame.draw.rect(surface, GREEN, [0,13*yu,w,3*yu],0)
    
    #moon
    pygame.draw.ellipse(surface,YELLOW, [xu, yu, 3*xu, 3*yu], 0)
    pygame.draw.ellipse(surface,NAVY, [1.75*xu, yu, 3*xu, 3*yu], 0)
    
    #windows 
    
    
    
# -------- Main Program Loop -----------
def main():                                             #every program should have a main function
                                                        #other functions go above main
    
    #declare local game variables here 
    
    
    while (True):
        
        for event in pygame.event.get():                #get all events in the last 1/60 sec & process them
            
            if ( event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
                pygame.quit();                          #for ending the game & closing window
                sys.exit();
        
            # if your program has a button, mouse, or keyboard interaction, code goes at this indentation level
        
        # ongoing game logic that occurs ever 1/60 second goes @ this indentation level
        
        
      
        surface.fill(NAVY)                             #set background color
        
        #drawing code goes here
        drawHouse()
        
        
        #clock.tick(60)                                  #Change FPS - frames per sec- when animating
        pygame.display.update()                          #updates the screen- usually in main
        
        
        
            
main()                                                   #this calls the main function to run the program
