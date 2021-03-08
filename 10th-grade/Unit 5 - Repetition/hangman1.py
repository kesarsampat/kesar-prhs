'''
Student Name: Kesar Sampat 
Game title: Hangman Pygame 
Period: 3
Features of Game: use pygame features to create a hangman game w/ user 
'''

import pygame, sys, random                                      #pulls in the special code functions for pygame
pygame.init()                                           #initialize game engine

w=800                                                   #Open and set window size
h=600                                                   #must code graphics to auto resize based on window size
size=(w,h)
surface = pygame.display.set_mode(size)
xu = w/9
yu = h/14  


pygame.display.set_caption("Hangman")          #set window title

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
def drawGallows():
    pygame.draw.rect(surface, BLACK, (xu*2, yu*10, w/2, h/4))
    pygame.draw.line(surface, BLACK, (xu*4.3, yu*10), (xu*4.3, yu), 8)
    pygame.draw.line(surface, BLACK, (xu*4.3, yu), (xu*5.5, yu),  8)
    pygame.draw.line(surface, BLACK, (xu*5.5, yu), (xu*5.5, yu*3), 8)
def head():
    pygame.draw.ellipse(surface, BLACK,(xu*5, yu*3 , xu, yu*2), 6)
def body():
    pygame.draw.line(surface, BLACK, [xu*5.5, yu*5], [xu*5.5, yu*7.5], 4)
def armR():
    pygame.draw.line(surface, BLACK, [xu*5.5,yu*6.5], [xu*5,yu*5.5], 5)    
def armL():
    pygame.draw.line(surface, BLACK, [xu*5.5,yu*6.5], [xu*6,yu*5.5], 5)
def legR():
    pygame.draw.line(surface, BLACK, [xu*5.5, yu*7.5], [xu*5.1, yu*9], 5)
def legL():
    pygame.draw.line(surface, BLACK, [xu*5.5, yu*7.5], [xu*5.8, yu*9], 5)
    
#draws the hangman    
def drawHangman():
    drawGallows()
    head()
    body()
    armR()
    armL()
    legR()
    legL()
    
#returns a random word to play hangman with
def getGameWord():
    words = ["computer", "concatenation", "binary", "function", "abstraction","programming", "python", "statement"]
    
    return random.choice(words)

#function to show message 
def showMessage(words, size, x, y, color, bg=None):
    font = pygame.font.SysFont("Calibri", 25, True, False,)
    text = font.render(words,True, color, bg)
    textBounds = text.get_rect()
    textBounds.center=(x,y)
    return text, textBounds



# -------- Main Program Loop -----------
def main():                                             #every program should have a main function
                                                        #other functions go above main
    
    #declare local game variables here
    gameWord = getGameWord()    
    
    while (True):
        
        for event in pygame.event.get():                #get all events in the last 1/60 sec & process them
            
            if ( event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
                pygame.quit();                          #for ending the game & closing window
                sys.exit();
        
            # if your program has a button, mouse, or keyboard interaction, code goes at this indentation level
        
        # ongoing game logic that occurs ever 1/60 second goes @ this indentation level
        
        
      
        surface.fill(WHITE)                             #set background color
        
        drawHangman()
        
        
        
        #clock.tick(60)                                  #Change FPS - frames per sec- when animating
        pygame.display.update()                          #updates the screen- usually in main
        
        
        
            
main()                                                   #this calls the main function to run the program
