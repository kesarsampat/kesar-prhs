'''
Student Name: Kesar Sampat 
Game title: Ludo Board Game 
Period: 3
Features of Game: use pygame features to create the game ludo from scratch  
'''

import pygame, sys, random  ,os                             #pulls in the special code functions for pygame
pygame.init()                                           #initialize game engine

w=600                                                   #Open and set window size
h=600                                                   #must code graphics to auto resize based on window size
size=(w,h)
surface = pygame.display.set_mode(size)


pygame.display.set_caption("Ludo Game")          #set window title

#declare global variables here

BLACK    = (   0,   0,   0)                             #Color Constants 
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
GREY = (193, 193, 193)
YELLOW  = (255, 229, 0)

#other global variables (WARNING: use sparingly):





#clock = pygame.time.Clock()                            # Manage timing for screen updates
                                                        # Uncomment when timing/animation is needed


#Program helper functions:

def storeData():
    return 42


'''
-uses a random generated number (1-6) to roll the dice and returns the value to be stored in main
-player can only get out of base if 6 is rolled 
-if 6 is rolled, player gets out AND can also PLAY AGAIN
-dice value is displayed on screen 

'''
def rollDice(diceRoll):
    #loading dice images in 
    dice1 = pygame.image.load('d1.png')
    dt1 = pygame.transform.scale(dice1,(78,78))
    
    dice2 = pygame.image.load('d2.png')
    dt2 = pygame.transform.scale(dice2,(78,78))
    
    dice3= pygame.image.load('d3.png')
    dt3 = pygame.transform.scale(dice3,(78,78))
    
    dice4 = pygame.image.load('d4.png')
    dt4 = pygame.transform.scale(dice4,(78,78))
    
    dice5 = pygame.image.load('d5.png')
    dt5 = pygame.transform.scale(dice5,(78,78))
    
    dice6 = pygame.image.load('d6.png')
    dt6 = pygame.transform.scale(dice6,(78,78))
    
    diceVal = random.randint(1,7)
    

    if diceRoll == True:
        
        if diceVal == 1:
            surface.blit(dt1, [0,h-90])
        
        elif diceVal == 2:
            surface.blit(dt2, [0,h-90])    
        
        elif diceVal == 3:
            surface.blit(dt3, [0,h-90])    
    
        elif diceVal == 4:
            surface.blit(dt4, [0,h-90])
                
        elif diceVal == 5:
            surface.blit(dt5, [0,h-90])    
             
        elif diceVal == 6:
            surface.blit(dt6, [0,h-90])   
            
        return diceVal 

def showMessage(words, size, font, x, y, color, bg = None):
    text_font = pygame.font.SysFont(font, size, True, False)
    text = text_font.render(words, True, color, bg)
    textBounds = text.get_rect()
    textBounds.center = (x, y)    
    surface.blit(text,textBounds)
    
    #return bounding rectangle for click detection
    return text, textBounds


'''
displays all elements on the screen:
-background, borders, startMessage, dice implementations, whoseTurn, 
'''
def drawScreen(diceValue):
    background = pygame.image.load('background.jpg')
    #pygame.transform.scale()
    surface.blit(background, [45,26])
    
    #borders 
    pygame.draw.rect(surface, GREY, [0,0, w, w/22]) #top
    pygame.draw.rect(surface, GREY, [0,0, w/12, h]) #left
    pygame.draw.rect(surface, GREY, [w-42.3,0, w/10, h]) #right
    pygame.draw.rect(surface, GREY, [0,h-65, w, w/5]) #bottom
    
    
    ##start to play #uncomment at end 
    #showMessage("LUDO!", 100, "Consolas", w/2, h/2-10, GREY)
    #showMessage("Click To Play", 20, "Consolas", w/2, h/2+40, GREY)
    
    #dice value 
    dice1 = pygame.image.load('d1.png')
    dt1 = pygame.transform.scale(dice1,(78,78))    
    surface.blit(dt1, [0,h-90])
    
    #showMessage(str(diceValue), 50 ,"Consolas", w/2, h-50, BLACK, bg=None)
    
    #players
    
    xplay = 105
    yplay = 85    
    
    #GREEN
  
    
    pygame.draw.ellipse(surface, GREEN, [xplay, yplay, 38,38])#left
    pygame.draw.ellipse(surface, GREEN, [xplay+49, yplay, 38,38])#right
    pygame.draw.ellipse(surface, GREEN, [xplay, yplay+49, 38,38]) #BL
    pygame.draw.ellipse(surface, GREEN, [xplay+49, yplay+49, 38,38])    #BR
    
    #RED
    pygame.draw.ellipse(surface, RED, [xplay, yplay+307, 38,38])
    pygame.draw.ellipse(surface, RED, [xplay+48, yplay+307, 38,38])
    pygame.draw.ellipse(surface, RED, [xplay, yplay+356, 38,38])
    pygame.draw.ellipse(surface, RED, [xplay+48, yplay+356, 38,38])    
    
    
    #YELLOW
    pygame.draw.ellipse(surface, YELLOW, [xplay+305, yplay, 38,38])
    pygame.draw.ellipse(surface, YELLOW, [xplay+354, yplay, 38,38])
    pygame.draw.ellipse(surface, YELLOW, [xplay+305, yplay+49, 38,38])
    pygame.draw.ellipse(surface, YELLOW, [xplay+354, yplay+49, 38,38])    
    
    
    #BLUE
    pygame.draw.ellipse(surface, BLUE, [xplay+306, yplay+307, 38,38])
    pygame.draw.ellipse(surface, BLUE, [xplay+354, yplay+307, 38,38])
    pygame.draw.ellipse(surface, BLUE, [xplay+306, yplay+356, 38,38])
    pygame.draw.ellipse(surface, BLUE, [xplay+354, yplay+356, 38,38])   
    
# -------- Main Program Loop -----------
def main():                                             #every program should have a main function
                                                        #other functions go above main
    
    #declare local game variables here 
    
    diceRoll = False 
    diceValue = rollDice(diceRoll)
    
    
    while (True):
        
        for event in pygame.event.get():                #get all events in the last 1/60 sec & process them
            
            if ( event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
                pygame.quit();                          #for ending the game & closing window
                sys.exit();
        
            # if your program has a button, mouse, or keyboard interaction, code goes at this indentation level
            
        
        # ongoing game logic that occurs ever 1/60 second goes @ this indentation level
        if( event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 ):
            diceRoll = True 
                
           
            
        
      
        surface.fill(WHITE)                             #set background color
        
        drawScreen(diceValue)
        rollDice(diceRoll)
        
        
        
        
        #clock.tick(60)                                  #Change FPS - frames per sec- when animating
        pygame.display.update()                          #updates the screen- usually in main
        
        
        
            
main()                                                   #this calls the main function to run the program


'''
dice face images - https://commons.wikimedia.org/wiki/Category:Dice_faces#/media/File:Alea_6.png
'''