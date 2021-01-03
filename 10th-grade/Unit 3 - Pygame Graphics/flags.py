'''
Student Name: Kesar Sampat 
Game title: Flags of the World 
Period: 3 
Features of Game: making a flag to scale factor using pygame 
'''

import pygame, sys                                      #pulls in the special code functions for pygame
pygame.init()                                           #initialize game engine

w=800                                                   #Open and set window size
h=600                                                   #must code graphics to auto resize based on window size
size=(w,h)
surface = pygame.display.set_mode(size)

pygame.display.set_caption("Flag of Iceland")          #set window title

#declare global variables here

#Color Constants 

BROWN    = ( 130,  96,  29)
BLUE     = ( 0,   102, 179)
WHITE    = ( 255, 255, 255)
RED      = ( 255,   0,   0)


#other global variables (WARNING: use sparingly):





#clock = pygame.time.Clock()                            # Manage timing for screen updates
                                                        # Uncomment when timing/animation is needed


#Program helper functions:
def drawFlag(x,y,sf):
    fw= w/5*sf
    fh = 18/25 *fw
    fxu = fw/25
    fyu = fh/18    
    pygame.draw.rect(surface, BLUE, (x, y, fw, fh) , 0 )
    drawStripes(x, y , sf)
   

    
def drawStripes(x, y, sf):
    fw= w/5*sf
    fh = 18/25 *fw
    fxu = fw/25
    fyu = fh/18     
    pygame.draw.rect(surface, WHITE,(x+7*fxu, y, 4.5*fxu, fh) , 0) 
    pygame.draw.rect(surface, WHITE,(x, y+7*fyu, fw, 4*fyu) , 0) 
    
    pygame.draw.rect(surface, RED,(x+8*fxu, y, 2.7*fxu, fh) , 0) 
    pygame.draw.rect(surface, RED,(x, y+7.7*fyu, fw, 2.5*fyu) , 0)    
    
#def flagPole(x, y, sf):
    #fw= w/5*sf
    #fh = 18/25 *fw
    #fxu = fw/25
    #fyu = fh/18      
    #pygame.draw.line(surface, BROWN, [x+12*fxu, y+12*fyu], [fw, fh], 0)
    
    
def flagName(x,y):   
    font = pygame.font.SysFont("Calibri", 25, True, False,)
    text = font.render("ICELAND", True, RED)
    text_rect = text.get_rect(center=(w/2,h/6))
    surface.blit(text, text_rect)    

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
        
        
      
        surface.fill(WHITE)                         #set background color 
        
        drawFlag(w/2, h/2, 1.5)
        drawFlag(w/4, h/4, 1)
        drawFlag(w/16, h/16, 0.5)
        
        #flagPole(w/2, h/2, 1.5)
        
        flagName(w/2,h/2)
       
        
        
        
        
        #clock.tick(60)                                  #Change FPS - frames per sec- when animating
        pygame.display.update()                          #updates the screen- usually in main
        
        
        
            
main()                                                   #this calls the main function to run the program
