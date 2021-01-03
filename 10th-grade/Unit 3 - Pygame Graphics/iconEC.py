'''
Student Name: Kesar Sampat 
Game title: Icon Extra Credit 
Period: 3
Features of Game: use pygame features to make an icon w/ scale factor 
'''

import pygame, sys, math                                    #pulls in the special code functions for pygame
pygame.init()                                           #initialize game engine

w=800                                                   #Open and set window size
h=600                                                   #must code graphics to auto resize based on window size
size=(w,h)
surface = pygame.display.set_mode(size)



pygame.display.set_caption("Icon")          #set window title

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
def drawIcon(x, y, sf):
    iceh = w/5*sf
    icew = 6/6*iceh
    xu = w/6
    yu = h/6  
    
    pygame.draw.rect(surface, BLACK, (xu*3, 4*yu, xu*1.5, yu*0.3))
    pygame.draw.rect(surface, BLACK, (xu*3.65, yu*3.7, xu*0.2, yu*0.5))
    
    pygame.draw.line(surface, BLACK, [xu*2.5, yu*2.2], [xu*5, yu*2.2], 10)
    
    pygame.draw.arc(surface, BLACK, (xu*2.5, yu*0.8, xu*2.5, yu*3), 5.8*math.pi/6, 12.2*math.pi/6, 10) #big arc 
    pygame.draw.arc(surface, BLACK, (xu*2.8, yu*1.67, xu, yu), math.pi/70, 6*math.pi/6,  10) #scoop1
    pygame.draw.arc(surface, BLACK, (xu*3.8, yu*1.7, xu, yu), math.pi/35, 6*math.pi/6,  10) #scoop2
    pygame.draw.arc(surface, BLACK, (xu*3.2, yu*1.4, xu, yu), math.pi/7, 5.4*math.pi/6,  10) #scoop2
  
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
        
        drawIcon(w/2, h/2,  1)
        drawIcon(w/4, h/8, 0.5)

        
        
        
        #clock.tick(60)                                  #Change FPS - frames per sec- when animating
        pygame.display.update()                          #updates the screen- usually in main
        
        
        
            
main()                                                   #this calls the main function to run the program
