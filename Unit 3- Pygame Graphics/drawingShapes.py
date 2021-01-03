'''
Student Name: Kesar Sampat 
Game title: practice with drawing commands 
Period: 3 
Features of Game: drawing functions 
'''

import pygame, sys, math                                #pulls in the special code functions for pygame
pygame.init()                                           #initialize game engine

w=640                                                   #Open and set window size
h=640                                                   #must code graphics to auto resize based on window size
size=(w,h)
surface = pygame.display.set_mode(size)

pygame.display.set_caption("Drawing Practice")          #set window title

#declare global variables here

BLACK    = (   0,   0,   0)                             #Color Constants 
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
LIGHT    = (150, 213, 245 )
GRAY     = (200,200, 200  )

#other global variables (WARNING: use sparingly):





#clock = pygame.time.Clock()                            # Manage timing for screen updates
                                                        # Uncomment when timing/animation is needed


#Program helper functions:
def drawShapes():
    pygame.draw.line(surface, RED, [0,0], [w,h], 10)
    pygame.draw.line(surface, RED, [0,h], [w,0], 10)
    
    pygame.draw.rect(surface, GREEN , (0,0,w,h), 15)

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
        
        
      
        surface.fill(LIGHT)                             #set background color
       
        #drawing code goes here
        drawShapes()
        pygame.draw.line(surface, RED, [0,0], [w,h], 10)
        pygame.draw.line(surface, RED, [0,h], [w,0], 10)
                
        pygame.draw.rect(surface, GREEN, (0,0,w,h), 20)
                
        pygame.draw.rect(surface, BLUE, (0,h/2,w/2,h/2), 0)
        
        #2 ways of drawing circles
        pygame.draw.ellipse(surface, GRAY,(0,h/2,w/2,h/2), 0) 
        
        pygame.draw.circle(surface, BLACK, int(w/4), int(3/4*h), int(w/8), 0 ) 
        
        #polygon
        polyPoints = [(w/2,0), (w, 2/5*h), (3/4*w,h), (w/4,h),(0,h*2/5)]
        
        pygame.draw.polygon(suface, WHITE, polyPoints, 5)
        
        #arc
        pygame.draw.arc(surface, BLACK, (2/5*w,h/6, w/5, w/5), math.pi,math.pi*3/2.5)
                
                
        
        
        
        #clock.tick(60)                                  #Change FPS - frames per sec- when animating
        pygame.display.update()                          #updates the screen- usually in main
        
        
        
            
main()                                                   #this calls the main function to run the program
