'''
Student Name: Kesar Sampat 
Game title: Growing Monster 
Period: 3
Features of Game: use pygame features to create a growing monster
'''

import pygame, sys, time, random
#jhyfrom pygame.locals import *

# set up pygame
pygame.init()

#instantiate a clock to control speed
clock = pygame.time.Clock()

# set up the window
w = 400
h = 400
surface = pygame.display.set_mode((w, h))
pygame.display.set_caption('Growing Monster')

# Color constants
BLACK = (0, 0, 0)
RED = (255,0,0)
WHITE = (255,255,255)

#constants

#every 1000 seconds, a USEREVENT will be added to the event queue 

pygame.time.set_timer(pygame.USEREVENT,1000)
NEWFOOD = 60   #a new food will be placed every second
SPEED = 6      #how fast monster moves per keydown


foodImage = pygame.image.load('treat3.png')   
playerRect = pygame.Rect(w/2-20,h/2-20,40,40) #initial position of monster



'''
Renders text for display onto the surface (does not blit)
returns:
text- an image of the words passed into the function
textBounds- bounding rectangle of the words passed into the function in the given font, size, etc

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
places cherries in the model @ random locations
returns list of Rect objects representing the placement of cherries 
'''
def placeCherries():
    
    cherriesList = []
    for i in range(20):
        x = random.randint(0,w-20)
        y = random.randint(0,h-20)
        cherriesList.append(pygame.Rect(x,y,20,20))
    return cherriesList

'''
checks whether the player collides with the surface boundaries
if so, it moves the player just inside of the appropriate wall(s)
'''
def collidesWithWall():
    #check top wall 
    if playerRect.top < 0:
        playerRect.top = 1 
        
    #check bottom wall
    if playerRect.bottom >= h:
        playerRect.bottom = h-1
        
    #check left wall
    if playerRect.left <=0:
        playerRect.left = 1 
    #check right wall
    if playerRect.right >=w:
        playerRect.right = w-1

'''
check collisions with cherries, removes if needed
NOTE: must send in specific player for comparison
'''
def eatCherries(cherriesList):
    # check if the playerRect has intersected with any cherry squares.
    for cherryRect in cherriesList:
        if cherryRect.colliderect(playerRect):
            cherriesList.remove(cherryRect)
            #player gets fatter 
            playerRect.width += 2 
            playerRect.height += 2
            
            #sound
            pickUpSound = pygame.mixer.Sound('pickup.wav')
            pickUpSound.play()
 
''''
Moves the player in a direction based on key(s) pressed 
Does not allow player to move beyond the surface walls
keys- list containing all current keys captured in the event loop

'''
def movePlayer(keys):
    
    if keys[pygame.K_LEFT]:
        playerRect.left -= SPEED
    if keys[pygame.K_RIGHT]:
        playerRect.left += SPEED  
    if keys[pygame.K_UP]:
        playerRect.top -= SPEED    
    if keys[pygame.K_DOWN]:
        playerRect.top += SPEED  

    collidesWithWall()
        
            
def drawScreen(cherries, gameOver,seconds):
    
    surface.fill(BLACK)
    
    showMessage(str(seconds), 20, "Consolas", w/10, h/12, WHITE)
    
    if gameOver == True:
        showMessage("Game Over", 60, "Consolas", w/2, h/2, RED,)
    
    playerImage = pygame.image.load('dog2.png')
    #scale image to correct size 
    playerStretched = pygame.transform.scale(playerImage,(playerRect.width, playerRect.height))
    
    #blits to surface 
    surface.blit(playerStretched, playerRect)


    #blit all cherries 
    for cherryRect in cherries:
        smallTreat = pygame.transform.scale(foodImage, (cherryRect.width+20, cherryRect.height+20))
        surface.blit(smallTreat,cherryRect)  

def main():
    foodCounter = 0 #add one cherry for every multiple of 60
    
    cherriesList = placeCherries()
        
    seconds = 0    

    #set up game control variables
    gameOver = False
    

    # run the game loop
    while True:
        
        #returns a list of booleans -which keys were pressed (continual keypress)
        keys = pygame.key.get_pressed()
      
       
        # check for the QUIT event
        for event in pygame.event.get():
            if gameOver == True:
                #if event.type == pygame.KEYDOWN and event.key ==pygame.K_ESCAPE or event.type == pygame.QUIT:
                pygame.time.delay(4000) #wait 4 seconds
                pygame.quit()
                sys.exit()
            
            #when game is over, delay before closing
            
            if event.type == pygame.USEREVENT:
                seconds +=1
                
        if not gameOver:
            foodCounter +=1
            #check to see if we need to add another cherry 
            if foodCounter %60==0:
                x = random.randint(0,w-20)
                y = random.randint(0,h-20)
                cherriesList.append(pygame.Rect(x,y,20,20))  
                
            if event.type == pygame.KEYDOWN and event.unicode == "x":
                playerRect.top= random.randint(0,h-playerRect.height)
                playerRect.left= random.randint(0,w-playerRect.width)
 
            #move the player
            movePlayer(keys)
            eatCherries(cherriesList)
                        
            if seconds >20:
                gameOver = True
                #turn off timer
                pygame.time.set_timer(pygame.USEREVENT,0)

        drawScreen(cherriesList, gameOver,seconds)
        pygame.display.update() 
        clock.tick(40)            

main()