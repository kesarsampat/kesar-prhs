###
# Kesar Sampat 
#  PD. 3
# Honors Computer Programming
# Assignment: Slots
# Purpose: Allows players to bet in game credits on a slot game
###

import pygame, sys, math, random

#initialize game engine
pygame.init()

#open and set window size
w = 380
h = 450
surface = pygame.display.set_mode((w, h))

#set title bar
pygame.display.set_caption("Slots")

#color constants
BLACK  = (  0,   0,   0)
WHITE  = (255, 255, 255)
RED    = (255,   0,   0)
GREEN  = (  0, 255,   0)
BLUE   = (  0,   0, 255)
YELLOW = (255, 255,   0)

#time for animation 
clock = pygame.time.Clock()


#instantiate picture objects
slot_machine = pygame.image.load("slot_machine.png").convert_alpha()
seven_icon = pygame.image.load("7slot_icon.png").convert_alpha()
banana_icon = pygame.image.load("banana_icon.png").convert_alpha()
bar_icon = pygame.image.load("bar_icon.png").convert_alpha()
bell_icon = pygame.image.load("bell_icon.png").convert_alpha()
cherry_icon = pygame.image.load("cherry_icon.png").convert_alpha()
grape_icon = pygame.image.load("grape_icon.png").convert_alpha()
lemon_icon = pygame.image.load("lemon_icon.png").convert_alpha()
orange_icon = pygame.image.load("orange_icon.png").convert_alpha()
watermelon_icon = pygame.image.load("watermelon_icon.png").convert_alpha()

icons = [seven_icon, banana_icon, bar_icon, bell_icon, cherry_icon,grape_icon,lemon_icon,orange_icon,watermelon_icon]


#instantiate picture objects for winning image and a transparent placeholder image
coin_image = pygame.image.load("bitcoin.png").convert_alpha()
placeholder_image = pygame.image.load("empty.png").convert_alpha()



#--------------------functions--------------------

#draws the screen at the start w backgrounds and icon placement 
def drawScene(left, mid, right):
    surface.fill(WHITE)
    surface.blit(slot_machine, [0, 0])
    surface.blit(left, (37,125))
    surface.blit(mid, (146,125))
    surface.blit(right, (253,125))
    
#code for writing a message 
def showMessage(words, size, x, y, color, bg=None):
    font = pygame.font.SysFont("Comic Sans MS", size, True, False,)
    text = font.render(words, True, color, bg)
    textBounds = text.get_rect()
    textBounds.center=(x,y)
    return text, textBounds

#shows the messages at the start and bets message 
def showText():
    startText, startTextBounds = showMessage("Press Enter To Play!", 22, w/2, h/2, WHITE, bg=BLACK)
    arrowText, arrowTextBounds = showMessage("Use Up and Down Arrows To Change Bets", 12, w/2, h-20, WHITE, bg=BLACK)
    betText, betTextBounds = showMessage("Bet:  ", 27, w/2, h-70, WHITE, bg=BLACK)    
    creditsText, creditsTextBounds = showMessage("Credits:  ", 23, w-80, h/6, WHITE, bg=BLACK)     
    surface.blit(startText, startTextBounds)
    surface.blit(arrowText, arrowTextBounds)    
    surface.blit(betText, betTextBounds)
    surface.blit(creditsText, creditsTextBounds)
    
def showWinner(left,mid,right):
    #left = mid and right wins 
    if left == mid:
        surface.blit(coin_image, [w/2-47,h-195])
    if left == right:
        surface.blit(coin_image, [w/2-47,h-195])
    if left == mid == right:
        surface.blit(coin_image, [w/2-47,h-195])  
    #mid = right 
    if mid == right:
        surface.blit(coin_image, [w/2-47,h-195])    
   
#----------------main program loop----------------
def main():       
 
    # data initializations (model)
    left = placeholder_image
    mid = placeholder_image
    right = placeholder_image
     
    betText = 0
    creditText = 10
    
    
    
    #main program loop
    while(True):
        
        #controller code
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                pygame.quit()
                sys.exit()
            #other single keypress events 
            
            #enter key press to start 
    
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                left = random.choice(icons)
                mid = random.choice(icons)
                right = random.choice(icons)
            
            #up and down arrow for bets
            #if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                #betText = 1  
               
                
                
    
 
 
 
 
        #game logic statements here to change the model
            
        
        
        
        #draw the view
        drawScene(left, mid, right)
        showWinner(left, mid, right)
        showText()

  
  
  
        #updates screen
        clock.tick(60)
        pygame.display.update()
        
        
main()