'''
Student Name: Kesar Sampat 
Game title: Etch a Sketch 
Period: 3
Features of Game: use pygame features to create an etch a sketch game  
'''

import pygame, sys                                      #pulls in the special code functions for pygame
pygame.init()                                           #initialize game engine

w=800                                                   #Open and set window size
h=600                                                   #must code graphics to auto resize based on window size
size=(w,h)
surface = pygame.display.set_mode(size)



pygame.display.set_caption("Etch a Sketch ")          #set window title

#declare global variables here

BLACK    = (   0,   0,   0)                             #Color Constants 
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

#other global variables (WARNING: use sparingly):

#set rectangle bounds for each red pygame.rect --use pygame.RECT

topBorder = pygame.Rect(0, 0, w, h/8)
bottomBorder = pygame.Rect(0, h/1.3, w, h/4)
leftBorder = pygame.Rect(0, 0, w/10, h)
rightBorder = pygame.Rect(w/1.11, 0, w/10, h)




clock = pygame.time.Clock()                            # Manage timing for screen updates
                                                        # Uncomment when timing/animation is needed


#Program helper functions:

def drawScreen():
    
    surface.fill(WHITE)
    
    #top
    pygame.draw.rect(surface, RED, topBorder) 
    
    #bottom 
    pygame.draw.rect(surface, RED, bottomBorder)  
    
    #left 
    pygame.draw.rect(surface, RED, (0, 0, w/10, h))
    
    #right 
    pygame.draw.rect(surface, RED, (w/1.11, 0, w/10, h))
      
    #logo
    logo = pygame.image.load("etch.gif").convert_alpha()
    surface.blit(logo, [w/3, h/1.3])
    
    #buttons 
    pygame.draw.ellipse(surface, WHITE, (w/22, h/1.265, w/6.8, h/5.3))
    pygame.draw.ellipse(surface, WHITE, (w/1.2, h/1.265, w/6.8, h/5.3))
    
#draws brush on surface to start     
def drawBrush(brush, color):
    pygame.draw.ellipse(surface, color, (brush[0], brush[1], 4, 4))
    
#moves brush around    
def moveBrush(keys, brush):
    
    if keys[pygame.K_UP] == True:                     #top arrow key
        brush[1]-=2
        
    if keys[pygame.K_DOWN] == True:                     #bottom arrow key 
        brush[1]+=2   
        
    if keys[pygame.K_LEFT] == True:                       #left arrow key 
        brush[0]-=2   
        
    if keys[pygame.K_RIGHT] == True:                   #right arrow key 
        brush[0]+=2
#collide point  

    if topBorder.collidepoint(brush[0], brush[1]): 
        brush = [w/2,h/2]                
        drawScreen()
        drawBrush(brush, BLACK) 
        moveBrush(keys, brush)
    if bottomBorder.collidepoint(brush[0], brush[1]): 
        brush = [w/2,h/2]                
        drawScreen()
        drawBrush(brush, BLACK)
        moveBrush(keys, brush)
        
    if leftBorder.collidepoint(brush[0], brush[1]): 
        brush = [w/2,h/2]                
        drawScreen()
        drawBrush(brush, BLACK)
        moveBrush(keys, brush)
        
    if rightBorder.collidepoint(brush[0], brush[1]): 
        brush = [w/2,h/2]                
        drawScreen()
        drawBrush(brush, BLACK)
        moveBrush(keys, brush)
        
     
#gets a color to change the color of brush
def getColorChoice(key,color):
    if key == "1":
        return RED
    if key == "2":
        return BLUE
    if key == "3":
        return GREEN
    
# -------- Main Program Loop -----------
def main():                                             #every program should have a main function
    
    #declare local game variables here 
    brush = [w/2,h/2]
    drawScreen()
                                                    #other functions go above main    
    
    
    while (True):
        
        for event in pygame.event.get():                #get all events in the last 1/60 sec & process them
            
            if ( event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
                pygame.quit();                          #for ending the game & closing window
                sys.exit();
        
            # if your program has a button, mouse, or keyboard interaction, code goes at this indentation level
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                brush = [w/2,h/2]                
                drawScreen()
                drawBrush(brush, BLACK)
                           
            
        
             
        # ongoing game logic that occurs ever 1/60 second gdoes @ this indentation level
            keys = pygame.key.get_pressed() 
            key = pygame.key.get_pressed() 
                     
        
        #drawing code goes here
        
        drawBrush(brush, BLACK)
        moveBrush(keys, brush)
        getColorChoice(key, BLACK)
        
        
        clock.tick(60)                                  #Change FPS - frames per sec- when animating
        pygame.display.update()                          #updates the screen- usually in main
        
        
        
            
main()                                                   #this calls the main function to run the program
