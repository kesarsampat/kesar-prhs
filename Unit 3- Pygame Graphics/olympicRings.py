'''
Student Name: Kesar Sampat 
Game title: Olympic Rings
Period: 3
Features of Game: making the olympic rings using pygame features 
'''

import pygame, sys, math                                      #pulls in the special code functions for pygame
pygame.init()                                           #initialize game engine

w=800                                                   #Open and set window size
h=int(16/20*w)                                                   #must code graphics to auto resize based on window size
size=(w,h)
surface = pygame.display.set_mode(size)
xu= w/20
yu= h/16





pygame.display.set_caption("Olympic Rings")          #set window title

#declare global variables here

BLACK    = (   0,   0,   0)
WHITE  =   (255,255,255   )                                              #Color Constants 
YELLOW   = (242, 203, 50)
GREEN    = (24, 163, 79)
RED      = ( 255,   0,   0)
BLUE     = (15, 113, 188)

#other global variables (WARNING: use sparingly):





#clock = pygame.time.Clock()                            # Manage timing for screen updates
                                                        # Uncomment when timing/animation is needed


#Program helper functions:
def drawRing(surface, color, coords, thickness):
    pygame.draw.ellipse(surface, color, coords, thickness)
    
def drawArc(surface, color, coord, a1, a2, thickness):
    pygame.draw.arc(surface, color, coord, a1, a2, thickness)
    
def showMessage():
    font = pygame.font.SysFont("Calibri", 25, True, False,)
    text = font.render("2020 Summer Olympics - Tokyo, Japan", True, BLACK)
    text_rect = text.get_rect(center=(300, 20))
    #textBounds = text.get_rect()
    #textBounds.center(w/2, yu)
    surface.blit(text, text_rect)
    

# -------- Main Program Loop -----------
def main():       
    #every program should have a main function
                                                        #other functions go above main
    #declare local game variables here 
    print(xu,yu)
    
    while (True):
        
        for event in pygame.event.get():                #get all events in the last 1/60 sec & process them
            
            if ( event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
                pygame.quit();                          #for ending the game & closing window
                sys.exit();
        
            # if your program has a button, mouse, or keyboard interaction, code goes at this indentation level
        
        # ongoing game logic that occurs ever 1/60 second goes @ this indentation level
        
        
      
        surface.fill(WHITE)                             #set background color

        drawRing(surface, BLUE, [xu, yu, 4*xu, 4*yu],20)
        drawRing(surface, BLACK, [5.5*xu, yu, 4*xu, 4*yu],20)
        drawRing(surface, RED, [9.75*xu, yu, 4*xu, 4*yu],20)
        drawRing(surface, YELLOW, [3*xu, 2.8*yu, 4*xu, 4*yu],20)
        drawRing(surface, GREEN, [7.5*xu, 2.8*yu, 4*xu, 4*yu],20)
        
        drawArc(surface, BLUE, (xu, yu,4*xu,4*yu), 5*math.pi/3, math.pi/6, 10)
        drawArc(surface, BLACK, (5.5*xu, yu, 4*xu, 4*yu), 4*math.pi/3, 5*math.pi/3, 10)
        drawArc(surface, GREEN, (7.5*xu, 2.8*yu, 4*xu, 4*yu), 5*math.pi/6, 7*math.pi/6, 10)
        drawArc(surface, BLACK, (5.5*xu, yu, 4*xu, 4*yu), 15*math.pi/8, math.pi/6, 10)
        drawArc(surface, RED, (9.75*xu, yu, 4*xu, 4*yu), 7*math.pi/5, 8*math.pi/5, 10)
        
        showMessage()
        
        
        
        
        
        #clock.tick(60)                                  #Change FPS - frames per sec- when animating
        pygame.display.update()                          #updates the screen- usually in main
        
        
        
            
main()                                                   #this calls the main function to run the program
