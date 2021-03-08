'''
Student Name: Kesar Sampat 
Game title: Line Art 
Period: 3
Features of Game: use pygame features to make a line art illusion 
#xanchor[0] += 
'''

import pygame, sys , random                                     #pulls in the special code functions for pygame
pygame.init()                                           #initialize game engine

w=800                                                   #Open and set window size
h=600                                                   #must code graphics to auto resize based on window size
size=(w,h)
surface = pygame.display.set_mode(size)



pygame.display.set_caption("Line Art")          #set window title

#declare global variables here

BLACK    = (   0,   0,   0)                             #Color Constants 
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

#other global variables (WARNING: use sparingly):

segLen = w/10



#clock = pygame.time.Clock()                            # Manage timing for screen updates
                                                        # Uncomment when timing/animation is needed


#Program helper functions:

#gets a random color 
def randomColor():
    
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    
    return r,g,b

#drawing the lines 
def drawLines(xanchor, yanchor, color, numSegments): 
    segLen = w/numSegments
    
    #for loop to draw lines
    for i in range(numSegments):
        
        #x pattern
        if xanchor == (w,0):
            xanchor[0]-= segLen
            pygame.draw.line(surface, color,xanchor ,yanchor, 5)
            
        else:
            xanchor[0] += segLen
            pygame.draw.line(surface, color, xanchor, yanchor, 5)
            
        #y pattern
        if yanchor == (0,0):
            yanchor[1] += segLen
            pygame.draw.line(surface, color, xanchor, yanchor, 5)
            
        else:
            yanchor[1] -= segLen 
            pygame.draw.line(surface, color, xanchor, yanchor, 5)
        

def getNumBetween(prompt, low, high):
    
    num = low-1  #out of range value needed to enter the loop
    
    #while loop 
    while(num<low or num>high):
        #getting OGhigh num from user
        try:
            num = int(input(prompt + " between " + str(low) + " and " + str(high) + ": "))
                      
            if num<low or num>high:
 
                print("Error - number entered is out of range\n")
                
        except ValueError:
            print("Error - integer value expected\n")
            
    return num


# -------- Main Program Loop -----------
def main():                                             #every program should have a main function
                                                        #other functions go above main
    
    #declare local game variables here 
    
    c1 = randomColor()
    c2 = randomColor()
    c3 = randomColor()
    c4 = randomColor()
        
    
    while (True):
        
        for event in pygame.event.get():                #get all events in the last 1/60 sec & process them
            
            if ( event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
                pygame.quit();                          #for ending the game & closing window
                sys.exit();
        
            # if your program has a button, mouse, or keyboard interaction, code goes at this indentation level
        
        # ongoing game logic that occurs ever 1/60 second goes @ this indentation level
        
        getNumBetween("Choose a number between", 10, 60)
      
        surface.fill(WHITE)     
        #set background color

        #clock.tick(60)     
        #Change FPS - frames per sec- when animating
        pygame.display.update()
        drawLines([w,0], [0,0], c1, 10) #UL
        drawLines([0,h], [0,0], c2, 10) #LL
        drawLines([w,0], [w,h], c3, 10) #UR
        drawLines([0,h], [w,h], c4, 10) #LR   
        #updates the screen- usually in main        
        
            
main()                                                   #this calls the main function to run the program
