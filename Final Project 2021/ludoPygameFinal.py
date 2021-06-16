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


sw = 512/15   #background picture is 512, and 15 squares per row

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



'''
need to keep track of the row and column of each piece

'''



#m = middle
#bg=base green
#by=base yellow
#bb=base blue
#br=base red
#gp = greenpiece
#yp = yellowpiece
#bp = bluepiece
#rp = red piece

def makeBoard():
    
    board = [ ["bg","bg","bg","bg","bg","bg","w","w","w","by","by","by","by","by","by"],
               ["bg","bg","bg","bg","bg","bg","w","y","y","by","by","by","by","by","by"],
               ["bg","bg","gp","gp","bg","bg","g","y","w","by","by","yp","yp","by","by"],
               ["bg","bg","gp","gp","bg","bg","w","y","w","by","by","yp","yp","by","by"],
               ["bg","bg","bg","bg","bg","bg","w","y","w","by","by","by","by","by","by"],
               ["bg","bg","bg","bg","bg","bg","w","y","w","by","by","by","by","by","by"],
               ["w","g","w","w","w","w", "m", "m", "m", "w","w","w","y","w","w"],
               ["w","g","g","g","g","g", "m", "m", "m", "b","b","b","b","b","w" ],
               ["w","w","r","w","w","w", "m", "m", "m", "w","w","w","w","b","w" ],
               ["rb","rb","rb","rb","rb","rb","w","r","w","bb","bb","bb","bb","bb","bb"],
               ["rb","rb","rb","rb","rb","rb","w","r","w","bb","bb","bb","bb","bb","bb"],
               ["rb","rb","rp","rp","rb","rb","w","r","b","bb","bb","bp","bp","bb","bb"],
               ["rb","rb","rp","rp","rb","rb","r","r","w","bb","bb","bp","bp","bb","bb"],
               ["rb","rb","rb","rb","rb","rb","r","r","w","bb","bb","bb","bb","bb","bb"],
               ["rb","rb","rb","rb","rb","rb","w","w","w","bb","bb","bb","bb","bb","bb"]]
    return board



pygame.display.set_caption("Ludo Game")          #set window title

#declare global variables here

BLACK    = (   0,   0,   0)                             #Color Constants 
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 165, 29, 29)
BLUE     = (   0,   0, 255)
GREY     = (193, 193, 193)
YELLOW   = (255, 153, 51)
DKGREY   = (132, 131, 131)

#other global variables (WARNING: use sparingly):
   
xplay = w/5.7       
yplay = w/7  

#boxes/spaces
box = w/25

#borders 
borders = [pygame.Rect(0,0, w, w/22), pygame.Rect(0,0, w/12, h), pygame.Rect(w-42.3,0, w/10, h), pygame.Rect(0,h-65, w, w/5)]


#player path lists 

greenPath =  [ [6,1], [6,2], [6,3], [6,4], [6,5], [5,6], [4,6], [3,6], [2,6], [1,6], [0,6], [0,7], [0,8], [1,8], [2,8], [3,8], [4,8], [5,8], [6,9], [6,10], [6,11], [6,12], [6,13], [6,14], [7,14] , [8,14], [8,13], [8,12], [8,11], [8,10], [8,9], [9,8], [10,8], [11,8], [12,8], [13,8], [14,8], [14,7] ,[14,6], [13,6], [12,6],[11,6],[10,6], [9,6], [8,5], [8,4], [8,3], [8,2], [8,1],[8,0],[7,0], [7,1],[7,2],[7,3],[7,4], [7,5], [7,6]]
yellowPath = [ [1,8], [2,8], [3,8], [4,8], [5,8], [6,9], [6,10], [6,11], [6,12], [6,13], [6,14], [7,14] , [8,14], [8,13], [8,12], [8,11], [8,10], [8,9], [9,8], [10,8], [11,8], [12,8], [13,8], [14,8], [14,7], [14,6], [13,6], [12,6],[11,6],[10,6], [9,6], [8,5], [8,4], [8,3], [8,2], [8,1],[8,0],[7,0], [6,0], [6,1], [6,2], [6,3], [6,4], [6,5], [5,6], [4,6], [3,6], [2,6], [1,6], [0,6], [0,7], [1,7], [2,7], [3,7], [4,7], [5,7], [6,7] ]
bluePath =   [ [8,13], [8,12], [8,11], [8,10], [8,9], [9,8], [10,8], [11,8], [12,8], [13,8], [14,8], [14,7], [14,6], [13,6], [12,6],[11,6],[10,6], [9,6], [8,5], [8,4], [8,3], [8,2], [8,1],[8,0],[7,0], [6,0], [6,1], [6,2], [6,3], [6,4], [6,5], [5,6], [4,6], [3,6], [2,6], [1,6], [0,6], [0,7], [0,8], [1,8], [2,8], [3,8], [4,8], [5,8], [6,9], [6,10], [6,11], [6,12], [6,13], [6,14], [7,14], [7,13], [7,12], [7,11], [7,10,], [7,9], [7,8]]
redPath =    [ [13,6], [12,6],[11,6],[10,6], [9,6], [8,5], [8,4], [8,3], [8,2], [8,1],[8,0],[7,0], [6,0], [6,1], [6,2], [6,3], [6,4], [6,5], [5,6], [4,6], [3,6], [2,6], [1,6], [0,6], [0,7],[0,8], [1,8], [2,8], [3,8], [4,8], [5,8], [6,9], [6,10], [6,11], [6,12], [6,13], [6,14], [7,14] , [8,14], [8,13], [8,12], [8,11], [8,10], [8,9], [9,8], [10,8], [11,8], [12,8], [13,8], [14,8], [14,7], [13,7], [12,7], [11,7], [10,7], [9,7], [8,7] ]


gpHomePositions = [ [2,2], [2,3], [3,2], [3,3] ]
ypHomePositions = [ [2,11], [2,12], [3,11], [3,12] ]
bpHomePositions = [ [11,11], [11,12], [12,11], [12,12] ]
rpHomePositions = [ [11,2], [11,3], [12,2], [12,3] ]

homePositions = gpHomePositions + ypHomePositions + bpHomePositions + rpHomePositions

#end positions (empty lists to append later)
gEnd = []
yEnd = []
bEnd = []
rEnd = []

#gameOver
gameOver = False



'''
store players in terms of what row and column they are located at in the grid

'''

greenPlayers = [pygame.Rect(xplay, yplay, 38,38), pygame.Rect(xplay+49, yplay, 38,38), pygame.Rect(xplay, yplay+49, 38,38), pygame.Rect(xplay+49, yplay+49, 38,38) ]


players =["GREEN","YELLOW","BLUE", "RED",]    

diceRect = pygame.Rect(0,h-90, 78,78)


clock = pygame.time.Clock()                            # Manage timing for screen updates
                                                        # Uncomment when timing/animation is needed


#Program helper functions:

'''
the beginning screen before playing with the title and 'click to play'
-uses mouse clicks 
'''

def startScreen(gameInPlay, pickPlayer, diceValue,board,currentTurn):
    for wall in borders:
        pygame.draw.rect(surface, GREY, wall)
   
    showMessage("LUDO!", 120, "Consolas", w/2-10, h/2-10, GREY)
    showMessage("Click To Play", 30, "Consolas", w/2-15, h/2+60, WHITE, GREY)  
    
    showMessage("-try to roll a 6 to get out and pick which player to move", 15, "Consolas", w/2-15, h/2+120, DKGREY)
    showMessage("-each player only gets one turn!", 15, "Consolas", w/2-15, h/2+150, DKGREY)    
    showMessage("-click player to move throughout to get to home ", 15, "Consolas", w/2-15, h/2+180, DKGREY)
    showMessage("-goal is to be the first one in your home ", 15, "Consolas", w/2-15, h/2+210, DKGREY)
    

    if pickPlayer == True:
        
        surface.fill(WHITE)
        gameInPlay == True
        drawScreen(diceValue,board,currentTurn)

    return gameInPlay
        

'''
-uses a random generated number (1-6) to roll the dice and returns the value to be stored in main
-player can only get out of base if 6 is rolled 
-if 6 is rolled, player gets out AND can also PLAY AGAIN
-dice value is displayed on screen 

'''
def blitDice(diceVal):
  
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
   
    time.sleep(0.5)

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
-background, borders, startMessage, dice implementations, currentTurn, 
'''
def drawScreen(diceValue,board,currentTurn):
    #background
    background = pygame.image.load('background.jpg')
    surface.blit(background, [45,26])
    
    #displaying grey borders all 4 sides 
    for wall in borders:
        pygame.draw.rect(surface, GREY, wall)
    
    #dice start message
 
    showMessage("Click dice to start.", 15, "Consolas", w-400, h-20, BLACK)
    showMessage("Roll 6 to get out!", 15, "Consolas", w-200, h-20, BLACK)
    
    #draws the player circles from the model
    y=26
    for row in board:
        x =45
        for square in row:
            if square=="gp":
                pygame.draw.ellipse(surface,GREEN,[x,y,sw,sw],0)
            if square=="yp":
                pygame.draw.ellipse(surface,YELLOW,[x,y,sw,sw],0)
            if square=="rp":
                pygame.draw.ellipse(surface,RED,[x,y,sw,sw],0)
            if square=="bp":
                pygame.draw.ellipse(surface,BLUE,[x,y,sw,sw],0)
            x+=sw
        y+=sw
    
    #game over
    if gameOver == True:
        if len(gEnd) == 4:
            showMessage("GREEN WON!", 50, "Consolas", w/2, h/2, GREEN)
        elif len(yEnd) == 4:
            showMessage("YELLOW WON!", 50, "Consolas", w/2, h/2, YELLOW)
        elif len(bEnd) == 4:
            showMessage("BLUE WON", 50, "Consolas", w/2, h/2, BLUE)
        elif len(rEnd) == 4:
            showMessage("RED WON", 50, "Consolas", w/2, h/2, RED)                                  
          
    blitDice(diceValue) 
    
    currentTurnMessage = players[currentTurn]+"\'s Turn"
    showMessage(currentTurnMessage, 40, "Consolas", w/2, h-45, GREY)
    showMessage(currentTurnMessage, 40, "Consolas", (w/2)-5, h-43,DKGREY )   #casts a shadow effect     

'''
returns the row and column of where you have clicked on the grid, negative values indicate that the player did not click on the board

'''
def getClickRowColumn(mousepos):
    x=mousepos[0]
    y=mousepos[1]
    if x<45 or x>557 or y<26 or y>538: #clicked out of bounds
        return -1,-1
    else:
        x=mousepos[0] - 45 #offset for blit position of board
        y=mousepos[1]-26
        row=int(y//sw)
        col=int(x//sw)
        print(row,col)
        return row,col
        
 
 
    
'''
gets the dice value from rollDice and moves the piece 
-needs to know whose turn it is 
-when mouse is clicked on player, it directly goes to the first colored space out 
-player can only move if 6 is rolled 
'''    
def movePiece(diceValue, currentTurn, board, currentPlayer, pieceRow, pieceCol):
    
    #first play...pieces are still home 
    if [pieceRow,pieceCol] in homePositions:
        firstTime = True
    else:       #not first time, move player regularly 
        firstTime = False
    
    #first time getting out 
    
    if diceValue == 6:      #dice needs to be 6 to get out 
        if [pieceRow,pieceCol] in homePositions:
            
            #clicked piece is at the first base location of path
            
            if currentTurn == 0:    #GREEN
                
                board[pieceRow][pieceCol] = "bg"        
                                
                board[6][1] = "gp"
                
            elif currentTurn == 1:    #YELLOW
                            
                board[pieceRow][pieceCol] = "by"
                                
                board[1][8] = "yp"
                
            elif currentTurn == 2:    #BLUE
                            
                board[pieceRow][pieceCol] = "bb"
                                
                board[8][13] = "bp"
                
            elif currentTurn == 3:    #RED
                                    
                board[pieceRow][pieceCol] = "br"
                                
                board[13][6] = "rp"
           
            firstTime = True
        else:
            firstTime = False
   
    #regular play through 
    if not firstTime:
        
  
            if currentTurn == 0:
                
                #checking to see if green piece in position and capture position 
                if "gp" == board[pieceRow][pieceCol]:   
                    
                    gIndex = greenPath.index([pieceRow, pieceCol])      #find index for position
                    
                    newGreenPos = gIndex + diceValue        #creating new postion for piece to move 
                    if newGreenPos > len(greenPath):
                        newGreenPos = len(greenPath) -1
                    
                    coordx = greenPath[newGreenPos][0]
                    coordy = greenPath[newGreenPos][1]
         
                    board[coordx][coordy] = "gp"
                    
                    if [coordx,coordy] == greenPath[0]:     #changing piece to blit piece 
                        
                        board[pieceRow][pieceCol] = "g"
                    
                        
                    else:
                        board[pieceRow][pieceCol] = "w"     #blitting white square back 
                        
                        
                        
                    #end game contents - easier without a function because it works for every player (would be repetitive)
                    if [coordx, coordy] == greenPath[-1]:
                        gEnd.append(True) 
                        print("in movePiece %d" % len(gEnd))
                        
                        if len(gEnd) == 4:
                            gameOver = True 
                            print("in movePiece %s" % gameOver)
                 
            elif currentTurn == 1:
                
                #same as green but for YELLOW 
                if "yp" == board[pieceRow][pieceCol]:
                    
                    yIndex = yellowPath.index([pieceRow, pieceCol])
                    
                    newYellowPos = yIndex + diceValue
                    
 
                    if newYellowPos > len(yellowPath):
                        newYellowPos = len(yellowPath) -1                      
                    
                    coordx = yellowPath[newYellowPos][0]
                    coordy = yellowPath[newYellowPos][1]
                    
               
                    board[coordx][coordy] = "yp"
                    
                    
                    
                    if [coordx,coordy] == yellowPath[0]:
                        
                        board[pieceRow][pieceCol] = "y"
                    
                        
                    else:
                        board[pieceRow][pieceCol] = "w"
                
                    if [coordx, coordy] == yellowPath[-1]:
                        yEnd.append(True) 
                        
                        if len(yEnd) == 4:
                            gameOver = True                 
                
            
                
            elif currentTurn == 2:
                #same as green but for BLUE 
                if "bp" == board[pieceRow][pieceCol]:
                    
                    bIndex = bluePath.index([pieceRow, pieceCol])
                    
                    newBluePos = bIndex + diceValue
                    
                    if newBluePos > len(bluePath):
                        newBluePos = len(bluePath) -1                      
                    
                    coordx = bluePath[newBluePos][0]
                    coordy = bluePath[newBluePos][1]
                    
                    board[coordx][coordy] = "bp"
                    
                    if [coordx,coordy] == bluePath[0]:
                        
                        board[pieceRow][pieceCol] = "b"
                    
                        
                    else:
                        board[pieceRow][pieceCol] = "w"
                        
                    if [coordx, coordy] == bluePath[-1]:
                        bEnd.append(True) 
                        
                        if len(bEnd) == 4:
                            gameOver = True                         
         
                  
                  
            elif currentTurn == 3:
                #same as green but for RED 
                if "rp" == board[pieceRow][pieceCol]:
                    
                    rIndex = redPath.index([pieceRow, pieceCol])
                    
                    newRedPos = rIndex + diceValue
                    
 
                    if newRedPos > len(redPath):
                        newRedPos = len(redPath) -1                      
                    
                    coordx = redPath[newRedPos][0]
                    coordy = redPath[newRedPos][1]
                    
                    board[coordx][coordy] = "rp"
                    
                    if [coordx,coordy] == redPath[0]:
                        
                        board[pieceRow][pieceCol] = "r"
                    
                        
                    else:
                        board[pieceRow][pieceCol] = "w"
                            
                    if [coordx, coordy] == redPath[-1]:
                        rEnd.append(True) 
                        
                        if len(rEnd) == 4:
                            gameOver = True                 
    
    #switching players 
    currentTurn+=1  #index for whose turn it is
    currentTurn = currentTurn%4
    players =["GREEN", "YELLOW","BLUE", "RED"]
    currentPlayer=players[currentTurn]        
   
    currentTurnMessage = players[currentTurn]+"\'s Turn"
              
       
    return currentTurn
        
    
                
orgBoard=makeBoard()  #when you move pieces off of one space onto another, you will need to restore the space to the color that was there before you put a piece on it.  Use this board to do that.   Global access, you should not change this board


# -------- Main Program Loop -----------
def main():                                             #every program should have a main function
                                                        #other functions go above main
    
    #declare local game variables here 
    gameInPlay = True
    diceRoll = True #only goes when clicked 
    diceValue=1 
    gameBoard = False      #turns true only on the start screen when the mouse is clicked, otherwise is false
    gameOver = False    #ends the game when all 4 pieces are in the home
      
                
    
    #increase currentTurn by 1 everytime you switch players.  currentPlayer=players[currentTurn%4] 
    currentTurn=0  #index for whose turn it is
    currentTurn = currentTurn%4
    players =["GREEN", "YELLOW","BLUE", "RED"]
    currentPlayer=players[currentTurn]     
    
    
    
    board=makeBoard()    # board for placing players 
        

        
            
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
                    pieceRow, pieceCol = getClickRowColumn(pygame.mouse.get_pos())   
                    
                    if (pieceRow, pieceCol) == (15, 0):
                        
                        pass
                    else:
                        movePiece(diceValue, currentTurn, board, currentPlayer, pieceRow, pieceCol)
                    
                        gameBoard = True
                  
                #dice 
                if diceRect.collidepoint(pygame.mouse.get_pos()):
                    if( event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 ):    
                        
                        #so it works only when mouse collides with dice and NOT the gameboard 
                        diceValue = random.randint(1,6) #for testing sake 
                        
                        #checking bounds and making sure clicks stay inside 
                        if (pieceRow, pieceCol) == (15, 0):

                            pass                        
                        
                        else:
                            currentTurn = movePiece(diceValue, currentTurn, board, currentPlayer, pieceRow, pieceCol) 
                        
                #gameOver (no reset)
                if gameOver == True:
                    board = orgBoard
                    diceRoll = False
                    gameBoard = False
                    gameInPlay = False
                    
                    print("gameOver")
            
        
        # ongoing game logic that occurs ever 1/60 second goes @ this indentation level
        
     
        
        
        surface.fill(WHITE)  #set background color
        startScreen(gameInPlay,gameBoard, diceValue,board,currentTurn)
        
        
        
        clock.tick(60)                                  #Change FPS - frames per sec- when animating
        pygame.display.update()                          #updates the screen- usually in main
        
        
        
            
main()                                                   #this calls the main function to run the program


'''
--------------------------REFERENCES------------------------------

1.) ludo background image accessed on 5/11/21 - https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pinterest.com%2Fpin%2F355010383129618020%2F&psig=AOvVaw0WiyvIjBVHHgRTBv9ckiET&ust=1622899865363000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCNDz8KuL_vACFQAAAAAdAAAAABAE
2.) dice face images accessed on 5/10/21 - https://commons.wikimedia.org/wiki/Category:Dice_faces#/media/File:Alea_6.png
3.) dice stopping and time updates accessed on 5/14/21 - https://tuxar.uk/a-graphical-dice-simulator/


'''