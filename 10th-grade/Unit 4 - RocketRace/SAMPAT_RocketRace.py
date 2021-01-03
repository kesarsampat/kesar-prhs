'''
Student Name: Kesar Sampat 
Game title: Rocket Race 
Period: 3
Features of Game: use pygame features to create a rocket race 
'''

import pygame, sys, random                              #pulls in the special code functions for pygame
pygame.init()                                           #initialize game engine

w=500 #Open and set window size
h=600                                                   #must code graphics to auto resize based on window size
size=(w,h)
surface = pygame.display.set_mode(size)


pygame.display.set_caption("Rocket Race")          #set window title

#declare global variables here

BLACK    = (   0,   0,   0)                             #Color Constants 
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
YELLOW   = (239, 239, 14  )

#other global variables (WARNING: use sparingly):

redRocket = pygame.image.load("rocket_red.gif").convert_alpha()
blueRocket = pygame.image.load("rocket_blue.gif").convert_alpha()
redRect = redRocket.get_rect()
blueRect = blueRocket.get_rect()



clock = pygame.time.Clock()                            # Manage timing for screen updates
                                                        # Uncomment when timing/animation is needed


#Program helper functions:

def drawScreen(gameInPlay,rocketChoice):
    bg = pygame.image.load("background4.jpg")
    surface.blit(bg,[0,0])
    surface.blit(redRocket, redRect)
    surface.blit(blueRocket, blueRect)
    
    if gameInPlay == False:
        winner = getWinner(rocketChoice)
        winnerText, winnerBounds = showMessage(winner, 40 , w/2, h/2, YELLOW, bg=WHITE)
        surface.blit(winnerText, winnerBounds)
        
    if gameInPlay == False:
        chooseText, chooseBounds = showMessage("Choose a Rocket", 30, w/2, w/2, YELLOW, bg=None)
        surface.blit(chooseText, chooseBounds)
        
    if gameInPlay == False:
        redButtonText, redButtonBounds = showMessage("Choose Red Rocket", 15, w/4, h/1.5, RED, bg=WHITE)
        blueButtonText, blueButtonBounds = showMessage("Choose Blue Rocket", 15, w/4*3, h/1.5, BLUE, bg=WHITE)    
        surface.blit(redButtonText, redButtonBounds)
        surface.blit(blueButtonText, blueButtonBounds)

        
       
def initRockets():
    redRect.centerx = w/4
    redRect.bottom = h-69
    blueRect.centerx = w/2+100
    blueRect.bottom = h-69
    
def showMessage(words, size, x, y, color, bg=None):
    font = pygame.font.SysFont("Calibri", 25, True, False,)
    text = font.render(words,True, color, bg)
    textBounds = text.get_rect()
    textBounds.center=(x,y)
    return text, textBounds

def getWinner(rocketChoice):
    
    if rocketChoice == None:
        return ""
    if rocketChoice == blueRocket and blueRect.top < redRect.top: #check this after need to look at showMessage 
        return "You Win!"
    if rocketChoice == redRocket and redRect.top < blueRect.top:
        return "You Win!"
    if rocketChoice == redRocket and redRect.top ==  blueRect.top:
        return "Tie!"
    if rocketChoice == blueRocket and redRect.top == blueRect.top:
        return "Tie!"
    else:
        return "You Lose!"
    
    if redRocket < blueRocket:
        return "Red Wins!"
    elif redRocket > blueRocket:
        return "Blue Wins!"
    else:
        return "Tie!"
    

# -------- Main Program Loop -----------
def main():                                             #every program should have a main function
                                                        #other functions go above main
    initRockets()
    #declare local game variables here 
    gameInPlay = False
    rocketChoice = None
    
    redButtonText, redButtonBounds = showMessage("Choose Red Rocket", 15, w/4, h/1.5, RED, bg=None)
    blueButtonText, blueButtonBounds = showMessage("Choose Blue Rocket", 15, w/4*3, h/1.5, BLUE, bg=None)
    
    while (True):
        
        for event in pygame.event.get():                #get all events in the last 1/60 sec & process them
            
            if ( event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
                pygame.quit();                          #for ending the game & closing window
                sys.exit();
        
            # if your program has a button, mouse, or keyboard interaction, code goes at this indentation level
            mousePos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if redButtonBounds.collidepoint(mousePos) == True:
                    print("leftClick")
                    gameInPlay = True
                if blueButtonBounds.collidepoint(mousePos) == True:
                    print("rightClick")
                    gameInPlay = True
    
        # ongoing game logic that occurs ever 1/60 second goes @ this indentation level
        if gameInPlay:
            values = [1,2,3,4,5]
            redRect.top -= random.choice(values)
            blueRect.top -= random.choice(values) 
            
        #stop rockets
        if redRect.top <= 0:
            gameInPlay = False
        elif blueRect.top <= 0:
            gameInPlay = False
            
        surface.fill(WHITE)                             #set background color
        
        #drawing code goes here
        
        drawScreen(gameInPlay, rocketChoice)
        
        clock.tick(60)                                  #Change FPS - frames per sec- when animating
        pygame.display.update()                          #updates the screen- usually in main
        
        
        
            
main()                                                   #this calls the main function to run the program
