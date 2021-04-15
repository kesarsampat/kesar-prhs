'''
Student Name: Kesar Sampat 
Game title: Blackjack
Period: 3
Features of Game: use pygame features and dictionaries to create a blackjack card game
'''

import pygame, sys, os, random                          #pulls in the special code functions for pygame
pygame.init()                                           #initialize game engine

w=600                                                   #Open and set window size
h=400                                                   #must code graphics to auto resize based on window size
size=(w,h)
surface = pygame.display.set_mode(size)


pygame.display.set_caption("Blackjack Card Game")          #set window title

#declare global variables here

BLACK    = (   0,   0,   0)                             #Color Constants 
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
YELLOW   = (255, 255, 0)

#other global variables (WARNING: use sparingly):





#clock = pygame.time.Clock()                            # Manage timing for screen updates
                                                        # Uncomment when timing/animation is needed


#Program helper functions:

'''
displays the message on the screen when called 
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
creates the card deck by reading all the images into a list 
'''
def createDeck():
    cardDict = {}
    
    cardFileNames = os.listdir("card_images")
        
    #populating the dictionary 
    for card in cardFileNames:
        if card[1] == "k" or card[1] == "q" or card[1] == "j" or card[2] == "0":
            value = 10 
        else:
            value = int(card[1])
            
        cardDict["card_images/"+card] = value
    
    return cardDict


'''
draws the screen with the background, buttons, and images 
'''
def drawScreen(playerHand, dealerHand,mouseOver,btnMessage,standMessage,hitMessage,gameOver,gamePlay):
    
    #loading the background 
    background = pygame.image.load("blackBack.jpg")
    surface.blit(background, [0,0])
    
    #blitting game time title 
    showMessage("BLACKJACK", 50, "Open Sans", w/2, h/20, YELLOW)
    
    #blitting dealer and player hand labels 
    
    showMessage("DEALER", 20, "Open Sans", w/5, h/5, WHITE)
    
    showMessage("PLAYER", 20, "Open Sans", w/5, h/1.7, WHITE)
    
    #blitting stand, hit, and deal hand buttons
    if gameOver == True:
        showMessage("STAND", 18, "Open Sans", w/4, h-45, WHITE, BLACK)
        showMessage("HIT", 18, "Open Sans", w/6, h-45, WHITE, BLACK)        
    else:
        showMessage("DEAL HAND", 18, "Open Sans", w/2.5, h-45, WHITE, BLACK)
    
    #totals

    getHandTotal(playerHand, dealerHand, lookupDeck)      

    #changing button colors when mouse is over 
    if mouseOver == True:
        
        #deal hand
        if btnMessage =="DEAL HAND ":
            buttonText,buttonBounds = showMessage("DEAL HAND", 18, "Open Sans", w/2.5, h-45, WHITE, BLACK)

        else:
            buttonText, buttonBounds = showMessage(btnMessage, 18, "Open Sans", w/2.5, h-45, BLACK, YELLOW)
            
        #stand
        if standMessage == "STAND":
            standText, standBounds = showMessage("STAND", 18, "Open Sans", w/4, h-45, WHITE, BLACK)
        else:
            standText, standBounds = showMessage(standMessage, 18, "Open Sans", w/4, h-45, BLACK, YELLOW)
            
        #hit

        if hitMessage == "HIT":
            hitText, hitBounds = showMessage("HIT", 18, "Open Sans", w/6, h-45, WHITE, BLACK)
        else:
            hitText, hitBounds = showMessage(hitMessage, 18, "Open Sans", w/6, h-45, BLACK, YELLOW)


    #going through and bltting blank card 
    blueBack = pygame.image.load("blueback.gif")
    px = w/23
    py = h/4
    
    dx = w/23
    dy = h-150
    for card in playerHand:
        if card == None:
            surface.blit(blueBack, [px,py])
            
        
        else:
            cardImage = pygame.image.load(card).convert_alpha()
            surface.blit(cardImage, [px,py])
            
        px+=w/20
            
    for card in dealerHand:
        if card == None:
            surface.blit(blueBack, [dx,dy])
        
        else:
            cardImage = pygame.image.load(card).convert_alpha()
            surface.blit(cardImage, [dx,dy])
            
        dx+=w/20    

'''
deals a random card from the deck to a hand depending on which hand is sent in
'''    
def dealCard(hand,cardDict):

    #making sure the list contains cards 
    if len(cardDict) == 0:
        cardDict = createDeck()
        
    cardList = list(cardDict.keys())
    cardKey = random.choice(cardList)
    hand.append(cardKey)
    del(cardDict[cardKey])
    

    return hand,cardDict

'''
begins a new game of blackjack 
'''    
def newHand(deck):
    player = []
    dealer = []
    
    player, deck = dealCard(player, deck) 
    dealer, deck = dealCard(dealer, deck)
    player, deck = dealCard(player, deck)
    
        
    dealer.append(None)     #dealer initially shows only one hand

    return player, dealer , deck


'''
calculates the numerical value of one hand 
'''
def getHandTotal(playerHand, dealerHand, lookupDeck):

    aceCountP = 0 
    aceCountD = 0 
    pTotal = 0 
    dTotal = 0 

    for card in playerHand:

        if card in lookupDeck: 
            cardValue = lookupDeck[card]               
            
            #ace
            if cardValue == 1:
                aceCountP+=1
            else:
                pTotal += cardValue
                
            #adding on other aces 
            if aceCountP > 1:
                for i in range(aceCountP-1):
                    pTotal+=1
            #last ace 
    #if aceCountP > 0:
        #pTotal+=1
    #else:
        #pTotal+=11            

    showMessage(str(pTotal), 55, "Open Sans", w/1.9, h-250, YELLOW)
    
    for card in dealerHand:
   
        if card in lookupDeck: 
            cardValue = lookupDeck[card]                
            
            #ace
            if cardValue == 1:
                aceCountD+=1
            else:
                dTotal += cardValue
                
            #adding on other aces 
            if aceCountD > 1:
                for i in range(aceCountD-1):
                    dTotal+=1
            #last ace 
            #if aceCountD > 0 and dTotal +11 >21:
                #dTotal+=1
            #else:
                #dTotal+=11            
       
    showMessage(str(dTotal), 55, "Open Sans", w/1.9, h-100, YELLOW)
    
        

    return pTotal, dTotal


'''
looks at player and dealer hands and returns a string message regarding the winner
'''
def findWinner(pTotal, dTotal, mouseOver):
    if pTotal < dTotal:
            showMessage("YOU WIN!", 40, "Open Sans", w/2, h-180, YELLOW)    
        
    if pTotal > dTotal:
        showMessage("DEALER WIN!", 40, "Open Sans", w/2, h-180, YELLOW)
    
    else:
        showMessage("DEALER WINS", 40, "Open Sans", w/2, h-180, YELLOW)
            
    if pTotal == 21:
        showMessage("YOU BUST", 40, "Open Sans", w/2, h-180, YELLOW)
        
    if dTotal == 21:
        showMessage("DEALER BUST", 40, "Open Sans", w/2, h-180, YELLOW)

    if pTotal == dTotal:
        showMessage("DRAW!", 40, "Open Sans", w/2, h-180, YELLOW)
        

lookupDeck = createDeck()   #looks up card values when totaling up the hand
   

# -------- Main Program Loop -----------
def main():                                             #every program should have a main function
                                                        #other functions go above main
    
    #declare local game variables here 
    
    gameOver = False 
    reset = True  
    gamePlay = False 
    
    mainDeck = createDeck()    #deals cards, each time a card is dealt, it is removed 
    playerHand, dealerHand, mainDeck = newHand(mainDeck)
    
    pTotal, dTotal = getHandTotal(playerHand, dealerHand, lookupDeck)
    
    
    dealerHand = [None,None]
    playerHand = [None,None]
    
    
    #BUTTON BOUNDS COLLISON DETECTION
    
    buttonText,buttonBounds = showMessage("DEAL HAND", 18, "Open Sans", w/2.5, h-45, WHITE, BLACK)
    btnMessage = "DEAL HAND"
    
    standText,standBounds = showMessage("STAND", 18, "Open Sans", w/4, h-45, WHITE, BLACK)
    standMessage = "STAND" 
 
    hitText,hitBounds = showMessage("HIT", 18, "Open Sans", w/6, h-45, WHITE, BLACK)
    hitMessage = "HIT"    


    while (True):
        
        for event in pygame.event.get():                #get all events in the last 1/60 sec & process them
            
            if ( event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
                pygame.quit();                          #for ending the game & closing window
                sys.exit();
        
            # if your program has a button, mouse, or keyboard interaction, code goes at this indentation level
            mouseOver = False 
            
            if buttonBounds.collidepoint(pygame.mouse.get_pos()):
                
                mouseOver = True 
                gameOver = False 
                
                
                if( event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                    gameOver = True
                    dealCard(playerHand, mainDeck)
                    dealCard(dealerHand, mainDeck)  
                    dealCard(dealerHand, mainDeck)
                    
                    
            if standBounds.collidepoint(pygame.mouse.get_pos()):

                mouseOver = True 
                gameOver = True
                gamePlay = True 
                reset = True 

                if( event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
           
                    dealCard(playerHand, mainDeck)
                    dealCard(playerHand, mainDeck)

                    findWinner(pTotal,dTotal,mouseOver)
                    
                #if reset == True:
                    
           
            if hitBounds.collidepoint(pygame.mouse.get_pos()):
                           
                mouseOver = True 
                gameOver = True 
                
                if( event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                    dealCard(dealerHand, mainDeck)


        # ongoing game logic that occurs ever 1/60 second goes @ this indentation level
        
        
      
        surface.fill(WHITE)                             #set background color
        
        drawScreen(playerHand, dealerHand,mouseOver,btnMessage,standMessage,hitMessage,gameOver,gamePlay)
        
        
        #clock.tick(60)                                  #Change FPS - frames per sec- when animating
        pygame.display.update()                          #updates the screen- usually in main
        
        
        
            
main()                                                   #this calls the main function to run the program















     






















