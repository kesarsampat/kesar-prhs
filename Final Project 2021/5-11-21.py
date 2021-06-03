'''
Student Name: Kesar Sampat 
Game title: Ludo Board Game 
Period: 3
Features of Game: use pygame features to create the game ludo from scratch  
'''

import pygame, sys, random , time                             #pulls in the special code functions for pygame
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
GREY     = (193, 193, 193)
YELLOW   = (255, 229, 0)

#other global variables (WARNING: use sparingly):
   
xplay = w/5.7       
yplay = w/7  

#boxes/spaces
box = w/25

#borders 
borders = [pygame.Rect(0,0, w, w/22), pygame.Rect(0,0, w/12, h), pygame.Rect(w-42.3,0, w/10, h), pygame.Rect(0,h-65, w, w/5)]

#pygame rect players 
greenPlayers = [pygame.Rect(xplay, yplay, 38,38), pygame.Rect(xplay+49, yplay, 38,38), pygame.Rect(xplay, yplay+49, 38,38), pygame.Rect(xplay+49, yplay+49, 38,38) ]

redPlayers = [pygame.Rect(xplay, yplay+307, 38,38), pygame.Rect(xplay+48, yplay+307, 38,38), pygame.Rect(xplay, yplay+356, 38,38), pygame.Rect(xplay+48, yplay+356, 38,38)]

yellowPlayers = [pygame.Rect(xplay+305, yplay, 38,38), pygame.Rect(xplay+354, yplay, 38,38), pygame.Rect(xplay+305, yplay+49, 38,38), pygame.Rect(xplay+354, yplay+49, 38,38)  ]

bluePlayers  = [pygame.Rect(xplay+306, yplay+307, 38,38), pygame.Rect(xplay+354, yplay+307, 38,38), pygame.Rect(xplay+306, yplay+356, 38,38), pygame.Rect(xplay+354, yplay+356, 38,38)]

    

diceRect = pygame.Rect(0,h-90, 78,78)
#clock = pygame.time.Clock()                            # Manage timing for screen updates
                                                        # Uncomment when timing/animation is needed


#Program helper functions:

'''
the beginning screen before playing with the title and 'click to play'
-uses mouse clicks 
'''
def startScreen(gameInPlay, color):
    for wall in borders:
        pygame.draw.rect(surface, GREY, wall)
   
    showMessage("LUDO!", 120, "Consolas", w/2-10, h/2-10, GREY)
    showMessage("Click To Play", 30, "Consolas", w/2-15, h/2+60, WHITE, GREY)    
    
    if color == True:
        surface.fill(WHITE)
        chooseColor()
        gameInPlay = True

'''
asks the user to clip which color and then that color goes down into main with the variable 'whoseTurn' 
'''
def chooseColor():
    for wall in borders:
        pygame.draw.rect(surface, GREY, wall) 
    
    #message rects for collison 
        
    showMessage("CHOOSE A COLOR", 40, "Consolas", w/2, 200, GREY, BLACK)
    greenText, greenBounds = showMessage("GREEN", 40, "Consolas", w/2, 260, WHITE, GREEN)
    yellowText, yellowBounds = showMessage("YELLOW", 40, "Consolas", w/2, 320, WHITE, YELLOW)
    blueText, blueBounds  = showMessage("BLUE", 40, "Consolas", w/2, 390, WHITE, BLUE)
    redText, redBounds = showMessage("RED", 40, "Consolas", w/2, 450, WHITE, RED)

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
    
    
    pygame.draw.rect(surface, RED, diceRect, 10)
    
    
    #randomly generating a number
    diceVal = random.randint(1,6)    
    
    for x in range(10):
                

    if diceRoll == True:    #diceRoll is a local variable in main 
        
        
        #print(diceVal)
        
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
        
        #updating screen and timing    
        pygame.display.update()
        time.sleep(0.2)
        print(diceVal)
            
        return diceVal #will  be stored in a variable in main

'''
displays a str message on screen when called 
'''
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
def drawScreen(diceValue, whoseTurn):
    #background
    background = pygame.image.load('background.jpg')
    surface.blit(background, [45,26])
    
    #displaying grey borders all 4 sides 
    for wall in borders:
        pygame.draw.rect(surface, GREY, wall)
    
    #dice value 
    dice1 = pygame.image.load('d1.png')
    dt1 = pygame.transform.scale(dice1,(78,78))    
    surface.blit(dt1, [0,h-90])    
    
    #displaying players in each home using pygame.Rect objects 
    for player in greenPlayers:
        pygame.draw.ellipse(surface, GREEN, player)
        
    for player in yellowPlayers:
        pygame.draw.ellipse(surface, YELLOW, player)
            
    for player in bluePlayers:
        pygame.draw.ellipse(surface, BLUE, player)
                
    for player in redPlayers:
        pygame.draw.ellipse(surface, RED, player)                
        
    #whoseTurn
    showMessage(whoseTurn, 30, "Consolas", w/2, h-50, BLACK)
''' 
switches the players when needed 
'''
def switchPlayer(whoseTurn):
    return 42
    
'''
gets the dice value from rollDice and moves the player 
-needs to know whose turn it is 
-when mouse is clicked on player, it directly goes to the first colored space out (it is safe there)
-player can only move if 6 is rolled 
'''    
def movePlayer(rollDice, whoseTurn):
    print(rollDice)
    
    if rollDice != 6:
        whoseTurn =  "RED'S TURN"
    else:
        #clicks on chosen player and player moves out 
        rollDice()
        movePlayer(rollDice)
        
    
# -------- Main Program Loop -----------
def main():                                             #every program should have a main function
                                                        #other functions go above main
    
    #declare local game variables here 
    gameInPlay = False 
   
    diceRoll = True 
    diceValue = rollDice(diceRoll)
    whoseTurn = "GREEN"
    mouse = False 
    color = False
    
    greenText, greenBounds = showMessage("GREEN", 40, "Consolas", w/2, 260, WHITE, GREEN)
    yellowText, yellowBounds = showMessage("YELLOW", 40, "Consolas", w/2, 320, WHITE, YELLOW)
    blueText, blueBounds  = showMessage("BLUE", 40, "Consolas", w/2, 390, WHITE, BLUE)
    redText, redBounds = showMessage("RED", 40, "Consolas", w/2, 450, WHITE, RED)
    
    
    
    while (True):
        
        for event in pygame.event.get():                #get all events in the last 1/60 sec & process them
            
            if ( event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
                pygame.quit();                          #for ending the game & closing window
                sys.exit();
        
            # if your program has a button, mouse, or keyboard interaction, code goes at this indentation level
            
        
        # ongoing game logic that occurs ever 1/60 second goes @ this indentation level
        
        
        #if( event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 ):
            #mouse = True 
            
            #color = True 
            #if greenBounds.collidepoint(pygame.mouse.get_pos()):
                #drawScreen(diceValue, whoseTurn)
        
                ##clicks down to roll the dice 
                #if( event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 ):
                    #diceRoll = True 
                    #rollDice(diceRoll)
                    
                    #print("check")
                    
            ##stopping the dice

            #if diceRect.collidepoint(pygame.mouse.get_pos()):
                #diceRoll = rollDice(diceRoll) 
                #if diceRect.collidepoint(pygame.mouse.get_pos()):
                    #diceRoll = True
                    #diceRoll()
          
          
          
          
          
        surface.fill(WHITE)  #set background color
        
        #startScreen(gameInPlay,color)
        drawScreen(diceValue, whoseTurn)
        rollDice(diceRoll)
        
        #clock.tick(60)                                  #Change FPS - frames per sec- when animating
        pygame.display.update()                          #updates the screen- usually in main
        
        
        
            
main()                                                   #this calls the main function to run the program


'''
dice face images - https://commons.wikimedia.org/wiki/Category:Dice_faces#/media/File:Alea_6.png


add in dice stopping and time link 
'''