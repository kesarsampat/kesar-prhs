'''
Student Name: Kesar Sampat 
Game title: Maze
Period: 3
Features of Game: use pygame features to create a maze 
'''

import pygame, sys                                      #pulls in the special code functions for pygame
pygame.init()                                           #initialize game engine

w=800                                                   #Open and set window size
h=600                                                   #must code graphics to auto resize based on window size
size=(w,h)
surface = pygame.display.set_mode(size)
xu = w/23
yu = h/17 


pygame.display.set_caption("Maze")          #set window title

#declare global variables here

BLACK    = (   0,   0,   0)                             #Color Constants 
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

#other global variables (WARNING: use sparingly):





#clock = pygame.time.Clock()                            # Manage timing for screen updates
                                                        # Uncomment when timing/animation is needed


#Program helper functions:


def drawBorders(): 
    #top
    pygame.draw.rect(surface, BLACK, (0, 0, w , yu)) 
    #left
    pygame.draw.rect(surface, BLACK, (0, 0+10, xu , h)) 
    #right
    pygame.draw.rect(surface, BLACK, (xu*22.1, yu , xu , h),) 
    #bottomleft
    pygame.draw.rect(surface, BLACK, (xu, yu*16.1, xu*18 , yu),) 
    #bottomright
    pygame.draw.rect(surface, BLACK, (xu*19, yu*16.1, xu*18 , yu),)     
    #end 
    pygame.draw.rect(surface, RED, (xu*18, yu*16.1, xu , yu),) #make borders around instead of overlapping 
def drawHorizontalRects():
    #h1
    pygame.draw.rect(surface, BLACK, (xu, yu*2, xu*4, yu))
    #h2
    pygame.draw.rect(surface, BLACK, (xu, yu*4, xu*6, yu))
    pygame.draw.rect(surface, BLACK, (xu, yu*5, xu*6, yu))
    #h3
    pygame.draw.rect(surface, BLACK, (xu, yu*8, xu*2, yu))
    #h4
    pygame.draw.rect(surface, BLACK, (xu*3, yu*13.5, xu*6, yu))
    pygame.draw.rect(surface, BLACK, (xu*3, yu*13, xu*6, yu))
    pygame.draw.rect(surface, BLACK, (xu*3, yu*12, xu*2, yu))
    pygame.draw.rect(surface, BLACK, (xu*3, yu*14.5, xu*2, yu))
    pygame.draw.rect(surface, BLACK, (xu*3, yu*15.2, xu*2, yu))
    pygame.draw.rect(surface, BLACK, (xu*3, yu*14.5, xu*2, yu))
    #h5
    pygame.draw.rect(surface, BLACK, (xu*10, yu*6, xu*4.5, yu))
    #h6
    pygame.draw.rect(surface, BLACK, (xu*14, yu*9, xu*2.5, yu))
    #h7
    pygame.draw.rect(surface, BLACK, (xu*15.5, yu*12, xu*7, yu))    
    #h8
    pygame.draw.rect(surface, BLACK, (xu*21.2, yu*3, xu*1.5, yu))  
    #h9
    pygame.draw.rect(surface, BLACK, (xu*12, yu*3, xu*5.5, yu))      
    #h10
    pygame.draw.rect(surface, BLACK, (xu*17, yu*2, xu*2, yu))  
    #h11
    pygame.draw.rect(surface, BLACK, (xu*2.2, yu*9, xu*4.8, yu))
    
    
    
def drawVerticalRects():
    #v1
    pygame.draw.rect(surface, BLACK, (xu*6, yu, xu, yu))    
    #v2
    pygame.draw.rect(surface, BLACK, (xu*6.5, yu*2.7, xu*1.5, yu*5))
    #v3
    pygame.draw.rect(surface, BLACK, (xu*12, yu*6.9, xu*1.5, yu*10))
    #v4
    pygame.draw.rect(surface, BLACK, (xu*16, yu*15.2, xu*1.2, yu*1.2))
    #v5
    pygame.draw.rect(surface, BLACK, (xu*18, yu*10, xu*1.2 , yu*3))       
    #v6
    pygame.draw.rect(surface, BLACK, (xu*16, yu, xu*1.5, yu*6)) 
    #v7
    pygame.draw.rect(surface, BLACK, (xu*19, yu*6.8, xu, yu*4))    
    #v8
    pygame.draw.rect(surface, BLACK, (xu*8.4, yu*15.13, xu*1.5, yu))     
def drawMaze():
    drawBorders()
    drawHorizontalRects()
    drawVerticalRects()

    
    
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
        
        
      
        surface.fill(WHITE)                             #set background color
        
        drawMaze()
        
        
        
        #clock.tick(60)                                  #Change FPS - frames per sec- when animating
        pygame.display.update()                          #updates the screen- usually in main
        
        
        
            
main()                                                   #this calls the main function to run the program
