'''
Student Name: Kesar Sampat 
Game title: Vehicles 
Period: 3
Features of Game: create at least 2 kind of veicles with color using pygame features 
'''

import pygame, sys                                      #pulls in the special code functions for pygame
pygame.init()                                           #initialize game engine

w=800                                                   #Open and set window size
h=600                                                   #must code graphics to auto resize based on window size
size=(w,h)
surface = pygame.display.set_mode(size)

pygame.display.set_caption("Vehicles")          #set window title

#declare global variables here

BLACK    = (   0,   0,   0)                             #Color Constants 
WHITE    = ( 255, 255, 255)
GREEN    = (162, 204, 138)
RED      = ( 255,   0,   0)
BLUE     = (16, 129, 242)

#other global variables (WARNING: use sparingly):





#clock = pygame.time.Clock()                            # Manage timing for screen updates
                                                        # Uncomment when timing/animation is needed


#Program helper functions:
   
    

def drawCar(x, y, sf):
    cw= w/5*sf
    ch = 3/6 *cw
    xu = cw/6
    yu = ch/3       

    pygame.draw.rect(surface, WHITE, (x, y+yu, xu*6, yu))
    
    trapPoints = ((x+xu, y+yu),(x+xu*2, y), (x+xu*4,y), (x+xu*5, y+yu))
    pygame.draw.polygon(surface, WHITE, trapPoints)
    
    pygame.draw.ellipse(surface, WHITE, (x+xu, y+yu*1.9, xu, yu))
    pygame.draw.ellipse(surface, WHITE, (x+xu*4, y+yu*1.9, xu, yu))
    
def drawTruck(x, y, sf):
    tw= w/5*sf
    th = 4/6 *tw
    xu = tw/6
    yu = th/4  
    
  
    pygame.draw.rect(surface, BLUE, (x, y+yu, xu*4.5, yu)) #horizontal
    pygame.draw.rect(surface, BLUE, (x+xu*2.53, y, yu*2, yu))  
    
    pygame.draw.ellipse(surface, WHITE, (x+xu*3, y+yu*1.5, xu, yu)) #right wheel
    pygame.draw.ellipse(surface, WHITE, (x, y+yu*1.5, xu, yu))
   
          



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
        
        
      
        surface.fill(GREEN)                             #set background color
        

        pygame.draw.rect(surface, BLACK, (0,200,800,200))
        drawCar(w/2, h/2, 1) #right
        drawCar(w/8, h/2, 0.5)
        drawTruck(w/4, h/2, 1)
        drawTruck(650, h/2, 0.5)
        
 
        
        
        #clock.tick(60)                                  #Change FPS - frames per sec- when animating
        pygame.display.update()                          #updates the screen- usually in main
        
        
        
            
main()                                                   #this calls the main function to run the program
