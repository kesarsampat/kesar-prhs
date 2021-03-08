'''
Student Name: Kesar Sampat
Game title: Maze
Period: 3
Features of Game: use pygame features to create a maze
'''

import pygame, sys, random                                   #pulls in the special code functions for pygame
pygame.init()                                           #initialize game engine

w=800                                                   #Open and set window size
h=600                                                   #must code graphics to auto resize based on window size
size=(w,h)
surface = pygame.display.set_mode(size)
xu = w/23
yu = h/17


pygame.display.set_caption("Maze Game")          #set window title

#declare global variables here

BLACK    = (   0,   0,   0)                             #Color Constants
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

#other global variables (WARNING: use sparingly):
SPEED = 6      #how fast monster moves per keydown

playerImage = pygame.image.load('blackWidow.png')
playerRect = pygame.Rect(400,300, 20, 20) #initial position of player

borderWalls = [pygame.Rect (0, 0, w , yu), pygame.Rect (0, 0+10, xu , h), pygame.Rect (xu*22.1, yu , xu , h), pygame.Rect (xu, yu*16.1, xu*18 , yu)]

exitRect = pygame.Rect(xu*18, yu*16.1, xu , yu)


hWalls = [pygame.Rect (xu, yu*2, xu*4, yu), pygame.Rect (xu, yu*4, xu*6, yu), pygame.Rect (xu, yu*5, xu*6, yu), pygame.Rect (xu, yu*8, xu*2, yu), pygame.Rect (xu*3, yu*13.5, xu*6, yu), pygame.Rect (xu*3, yu*13, xu*6, yu),
          pygame.Rect (xu*3, yu*12, xu*2, yu), pygame.Rect (xu*3, yu*14.5, xu*2, yu), pygame.Rect (xu*3, yu*15.2, xu*2, yu), pygame.Rect (xu*3, yu*14.5, xu*2, yu), pygame.Rect (xu*10, yu*6, xu*4.5, yu), pygame.Rect (xu*14, yu*9, xu*2.5, yu), pygame.Rect (xu*15.5, yu*12, xu*7, yu), pygame.Rect (xu*21.2, yu*3, xu*1.5, yu), pygame.Rect (xu*12, yu*3, xu*5.5, yu), pygame.Rect (xu*17, yu*2, xu*2, yu), pygame.Rect (xu*2.2, yu*9, xu*4.8, yu)     ]
vWalls = [pygame.Rect (xu*6, yu, xu, yu), pygame.Rect (xu*6.5, yu*2.7, xu*1.5, yu*5), pygame.Rect (xu*12, yu*6.9, xu*1.5, yu*10),
          pygame.Rect (xu*16, yu*15.2, xu*1.2, yu*1.2),pygame.Rect (xu*18, yu*10, xu*1.2 , yu*3), pygame.Rect (xu*16, yu, xu*1.5, yu*6), pygame.Rect (xu*19, yu*6.8, xu, yu*4), pygame.Rect (xu*8.4, yu*15.13, xu*1.5, yu)]

#gem images

gemImage= pygame.image.load('gem5.png')


clock = pygame.time.Clock()                            # Manage timing for screen updates
                                                        # Uncomment when timing/animation is needed


#Program helper functions:

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
''''
Moves the player in a direction based on key(s) pressed
Does not allow player to move beyond the surface walls
keys- list containing all current keys captured in the event loop

'''
def movePlayer(keys):

    if keys[pygame.K_LEFT]:
        playerRect.left -= SPEED
        if collidesWithWall(playerRect):
            showMessage("no", 20, "Consolas", w/2, h/2, RED)
            playerRect.left += SPEED

    if keys[pygame.K_RIGHT]:
        playerRect.left += SPEED
        if collidesWithWall(playerRect):
            showMessage("no", 20, "Consolas", w/2, h/2, RED)
            playerRect.left -= SPEED

    if keys[pygame.K_UP]:
        playerRect.top -= SPEED
        if collidesWithWall(playerRect):
            showMessage("no", 20, "Consolas", w/2, h/2, RED)
            playerRect.top += SPEED

    if keys[pygame.K_DOWN]:
        playerRect.top += SPEED
        if collidesWithWall(playerRect):
            showMessage("no", 20, "Consolas", w/2, h/2, RED)
            playerRect.top -= SPEED

'''
Determine whether or not your player or a gem collides with a wall of the maze
'''

def collidesWithWall(playerRect):

    for walls in borderWalls:
        if playerRect.colliderect(walls):
            return True

    for walls in vWalls:
        if playerRect.colliderect(walls):
            return True


    for walls in hWalls:
        if playerRect.colliderect(walls):
            return True

    return False

'''
Chooses 5 random locations to put gems for the player to capture
'''
#don't use a for loop
def placeGems():

    gemList = []

    for i in range(5):
        gemX = random.randint(0,400)
        gemY = random.randint(0,400)

        gemList.append(pygame.Rect(gemX,gemY,5,5))

    return gemList



    #while len(gemList) < 5:


def drawMaze():
    surface.blit(playerImage,playerRect)
    pygame.draw.rect(surface, RED, exitRect)


    for wall in borderWalls:
        pygame.draw.rect(surface, BLACK, wall)

    for wall in vWalls:
        pygame.draw.rect(surface, BLACK, wall)

    for wall in hWalls:
        pygame.draw.rect(surface, BLACK, wall)


    #for gemRect in gems:
        #surface.blit()





# -------- Main Program Loop -----------
def main():                                             #every program should have a main function
                                                        #other functions go above main

    #declare local game variables here


    while (True):

        #returns a list of booleans -which keys were pressed (continual keypress)
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():                #get all events in the last 1/60 sec & process them

            if ( event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
                pygame.quit();                          #for ending the game & closing window
                sys.exit();

            # if your program has a button, mouse, or keyboard interaction, code goes at this indentation level

        # ongoing game logic that occurs ever 1/60 second goes @ this indentation level



        surface.fill(WHITE)
        movePlayer(keys)
        drawMaze()
        placeGems()




        clock.tick(60)                                  #Change FPS - frames per sec- when animating
        pygame.display.update()                          #updates the screen- usually in main




main()                                                   #this calls the main function to run the program
