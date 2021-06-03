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


#board = [ [bg,bg,bg,bg,bg,bg,w,w,w,by,by,by,by,by,by]
          #[bg,bg,bg,bg,bg,bg,w,y,y,by,by,by,by,by,by]
          #[bg,bg,bg,bg,bg,bg,w,y,w,by,by,by,by,by,by]
          #[bg,bg,bg,bg,bg,bg,w,y,w,by,by,by,by,by,by]
          #[bg,bg,bg,bg,bg,bg,w,y,w,by,by,by,by,by,by]
          #[bg,bg,bg,bg,bg,bg,w,y,w,by,by,by,by,by,by]
          #[w,g,w,w,w,w, gy, y, yb, w,w,w,w,w,w ]
          #[w,g,g,g,g,g,w,w,w,b,b,b,b,b,w]
          #[rb,rb,rb,rb,rb,rb,w,r,w,bb,bb,bb,bb,bb,bb]
          #[rb,rb,rb,rb,rb,rb,w,r,w,bb,bb,bb,bb,bb,bb]
          #[rb,rb,rb,rb,rb,rb,w,r,w,bb,bb,bb,bb,bb,bb]
          #[rb,rb,rb,rb,rb,rb,w,r,w,bb,bb,bb,bb,bb,bb]
          #[rb,rb,rb,rb,rb,rb,w,r,w,bb,bb,bb,bb,bb,bb]
          #[rb,rb,rb,rb,rb,rb,w,w,w,bb,bb,bb,bb,bb,bb]
          

#]

pygame.display.set_caption("Ludo Game")          #set window title

#declare global variables here

BLACK    = (   0,   0,   0)                             #Color Constants 
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
GREY     = (193, 193, 193)
YELLOW   = (255, 229, 0)
DKGREY   = (132, 131, 131)

#other global variables (WARNING: use sparingly):
   
xplay = w/5.7       
yplay = w/7  

#boxes/spaces
box = w/25

#borders 
borders = [pygame.Rect(0,0, w, w/22), pygame.Rect(0,0, w/12, h), pygame.Rect(w-42.3,0, w/10, h), pygame.Rect(0,h-65, w, w/5)]

#pygame rect players 

#GREEN
greenPlayers = [pygame.Rect(xplay, yplay, 38,38), pygame.Rect(xplay+49, yplay, 38,38), pygame.Rect(xplay, yplay+49, 38,38), pygame.Rect(xplay+49, yplay+49, 38,38) ]

green1 = pygame.Rect(xplay, yplay, 38,38)
green2 = pygame.Rect(xplay+49, yplay, 38,38)
green3 = pygame.Rect(xplay, yplay+49, 38,38)
green4 = pygame.Rect(xplay+49, yplay+49, 38,38)

#RED
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
def startScreen(gameInPlay, pickPlayer, diceValue, diceRoll, startDScreen):
    for wall in borders:
        pygame.draw.rect(surface, GREY, wall)
   
    showMessage("LUDO!", 120, "Consolas", w/2-10, h/2-10, GREY)
    showMessage("Click To Play", 30, "Consolas", w/2-15, h/2+60, WHITE, GREY)    
    
    if pickPlayer == True:
        
        surface.fill(WHITE)
        gameInPlay == True
        drawScreen(diceValue, diceRoll, startDScreen)

    return gameInPlay
        

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
    
    if diceRoll == False:
        surface.blit(dt1, [0,h-90])

    if diceRoll == True:    #diceRoll is a local variable in main 
        #dice value for click/collision thing 
        startDScreen = False 
        
     
        #randomly generating a number
        diceVal = random.randint(1,6)    
      
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
        time.sleep(0.5)
        
        print(diceVal)
        
        if diceRoll == False:
            #need to add something in here for when it is false?
            print("stop")        
      
        return diceVal, startDScreen #will  be stored in a variable in main

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
def drawScreen(diceValue,diceRoll, startDScreen):
    #background
    background = pygame.image.load('background.jpg')
    surface.blit(background, [45,26])
    
    
    
    #displaying grey borders all 4 sides 
    for wall in borders:
        pygame.draw.rect(surface, GREY, wall)
       
    #dice start message
    showMessage("Click dice to start.", 15, "Consolas", w/2, h-20, BLACK)
    
    #displaying players in each home using pygame.Rect objects 
    for player in greenPlayers:
        pygame.draw.ellipse(surface, GREEN, player)
        
    for player in yellowPlayers:
        pygame.draw.ellipse(surface, YELLOW, player)
            
    for player in bluePlayers:
        pygame.draw.ellipse(surface, BLUE, player)
                
    for player in redPlayers:
        pygame.draw.ellipse(surface, RED, player)   
        
    if startDScreen == True:
        #dice value 
        dice1 = pygame.image.load('d1.png')
        dt1 = pygame.transform.scale(dice1,(78,78))    
        surface.blit(dt1, [0,h-90])    
          
        
''' 
switches the players when needed and displays the turn of the player when needed 
'''
def switchPlayer(greenTurn, yellowTurn, redTurn, blueTurn):
    
    #SWITCHING PLAYERS 
    if greenTurn == True:
        greenTurn == False
        yellowTurn = True

    elif yellowTurn == True:
        yellowTurn == False  
        redTurn = True
        
    elif redTurn == True:
        redTurn = False 
        blueTurn = True 
        
    elif blueTurn == True:
        blueTurn = False
        greenTurn = True
        
        
    #DISPLAYING TURNS 
    if greenTurn == True:
        showMessage("GREEN'S TURN", 40, "Consolas", w/2, h-45, DKGREY)
        showMessage("GREEN'S TURN", 40, "Consolas", (w/2)-5, h-43,GREEN )   #casts a shadow effect 
        
    elif redTurn == True:
        showMessage("RED'S TURN", 40, "Consolas", w/2, h-45, DKGREY)
        showMessage("RED'S TURN", 40, "Consolas", (w/2)-5, h-43, RED)   #casts a shadow effect 
           
    elif yellowTurn == True:
        showMessage("YELLOW'S TURN", 40, "Consolas", w/2, h-45, DKGREY)
        showMessage("YELLOW'S TURN", 40, "Consolas", (w/2)-5, h-43, YELLOW)   #casts a shadow effect 
           
    elif blueTurn == True:
        showMessage("BLUE'S TURN", 40, "Consolas", w/2, h-45, DKGREY)  
        showMessage("BLUE'S TURN", 40, "Consolas", (w/2)-5, h-43, BLUE)   #casts a shadow effect 
        
    return greenTurn, yellowTurn, redTurn, blueTurn
       
 
    
'''
gets the dice value from rollDice and moves the player 
-needs to know whose turn it is 
-when mouse is clicked on player, it directly goes to the first colored space out (it is safe there)
-player can only move if 6 is rolled 
'''    
def movePlayer(diceValue, playerMove, greenTurn, redTurn, yellowTurn, blueTurn):
    
    if diceValue != 6:   #move on to next player 
        switchPlayer(greenTurn, redTurn, yellowTurn, blueTurn)
    
    #first play to get out
    elif diceValue == 6 and playerMove == False: #if playerMove == False, it is still in its home (first play)
        #need to do it seperatly for all players???
        if greenTurn == True:
            green1.bottom+=box
  
     
    else:
        
        if playerMove == True:
            greenTurn = True
            
        
        if playerMove == True:      #playerMove = True when the mouse clicks on the sprite 
            print('check')
            green1.left+=box           #box is a global variable of change --- it is the length of each individual square on the board 
            
            
            
            #move the player....+spaceW*rollDice     #moving the player but then multiply by the return value in roll dice to move the right number of squares 
            
        
            #if diceValue == 6:
                ##roll again
                #rollDice()
                #movePlayer(rollDice)
                
    
# -------- Main Program Loop -----------
def main():                                             #every program should have a main function
                                                        #other functions go above main
    
    #declare local game variables here 
    gameInPlay = True
    diceRoll = True #only goes when clicked 
    diceValue, startDScreen = rollDice(diceRoll)  #return value (int) from rollDice() function
    gameBoard = False      #turns true only on the start screen when the mouse is clicked, otherwise is false
    playerMove = False   
    
    
    greenTurn = False #game always starts with green 
    redTurn = True 
    yellowTurn = False 
    blueTurn = False 
    
    greenTurn, yellowTurn, redTurn, blueTurn = switchPlayer(greenTurn, yellowTurn, redTurn, blueTurn) #color turns for switches and stuff      

        
        
            
    while (True):
        
        for event in pygame.event.get():                #get all events in the last 1/60 sec & process them
            
            if ( event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
                pygame.quit();                          #for ending the game & closing window
                sys.exit();
        
            # if your program has a button, mouse, or keyboard interaction, code goes at this indentation level
            
            if gameInPlay == False:
                startScreen(gameInPlay, gameBoard, diceValue, diceRoll)

     
            if gameInPlay == True:      #switching from home screen to gamescreen
                
                if( event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 ):
                        
                    gameBoard = True
                    
                    movePlayer(rollDice, playerMove, greenTurn, yellowTurn, redTurn, blueTurn)    
                    
                #if any of the players are cliked, call the function- the function will work accordingly
                
                if green1.collidepoint(pygame.mouse.get_pos()):
                    if( event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 ):  
                        print("greencollide1")
                    

                        movePlayer(rollDice, playerMove, greenTurn, redTurn, yellowTurn, blueTurn)
                    
                #if redPlayers.collidepoint(pygame.mouse.get_pos()):
                
                    #movePlayer(rollDice, whoseTurn, playerMove, greenTurn, redTurn, yellowTurn, blueTurn)
 
                
                #if yellowPlayers.collidepoint(pygame.mouse.get_pos()):
                
                    #movePlayer(rollDice, whoseTurn, playerMove, greenTurn, redTurn, yellowTurn, blueTurn)
                                                            
                #if bluePlayers.collidepoint(pygame.mouse.get_pos()):
                
                    #movePlayer(rollDice, whoseTurn, playerMove, greenTurn, redTurn, yellowTurn, blueTurn)  
                    
 
                #stopping the dice 
                if diceRect.collidepoint(pygame.mouse.get_pos()):
                    if( event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 ):        
                        
                        
                        #so it works only when mouse collides with dice and NOT the gameboard 
                        diceRoll = True 
                        rollDice(diceRoll)   
                      
                    
                        diceRoll = False
                        rollDice(diceRoll)
                    
                    
                    
                    ##to roll dice again after clicking - only happens when a 6 is rolled 
                    #if diceRect.collidepoint(pygame.mouse.get_pos()):
                        #diceRoll = True
                        #rollDice(diceRoll)
              
        
        # ongoing game logic that occurs ever 1/60 second goes @ this indentation level
        
     
        
        
        surface.fill(WHITE)  #set background color
        
        startScreen(gameInPlay,gameBoard, diceValue, diceRoll, startDScreen)
        
        
        #clock.tick(60)                                  #Change FPS - frames per sec- when animating
        pygame.display.update()                          #updates the screen- usually in main
        
        
        
            
main()                                                   #this calls the main function to run the program


'''
dice face images - https://commons.wikimedia.org/wiki/Category:Dice_faces#/media/File:Alea_6.png


add in dice stopping and time link 
'''