'''
Student Name: Kesar Sampat 
Game title: Line Art 
Period: 3
Features of Game: use pygame features to make a line art illusion 

'''

import pygame, sys , random                                     #pulls in the special code functions for pygame
pygame.init()                                           #initialize game engine

w=600                                                   #Open and set window size
h=600                                                   #must code graphics to auto resize based on window size
size=(w,h)


pygame.display.set_caption("Line Art")          #set window title

#declare global variables here

BLACK    = (   0,   0,   0)                             #Color Constants 
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

#other global variables (WARNING: use sparingly):



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
def drawLines(surface, xanchor, yanchor, color, numSegments): 

    segLen = w/numSegments
    
    #for loop to draw lines
    for i in range(numSegments):
        
        #x pattern
        if xanchor == (w,0):
            xanchor[0]-= segLen
            pygame.draw.line(surface, color, xanchor,yanchor, 1)

        else:
            pygame.draw.line(surface, color, xanchor, yanchor, 1)
            xanchor[1] += segLen
            
            
        #y pattern
        if yanchor == (0,0):
            
            pygame.draw.line(surface, color, xanchor, yanchor, 1)
            yanchor[1] += segLen

        else:
            yanchor[0] -= segLen 
            pygame.draw.line(surface, color, xanchor, yanchor, 1)

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
def main():              
    
    numSegments = getNumBetween("Choose a number",10,100)
    surface = pygame.display.set_mode(size)
    
    
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
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                c1 = randomColor()
                c2 = randomColor()
                c3 = randomColor()
                c4 = randomColor()                
             
        # ongoing game logic that occurs ever 1/60 second goes @ this indentation level
        
      
        #set background color
        surface.fill(BLACK) 
          
        drawLines(surface,[0,0], [w,0], c1, numSegments) #UL works 
        drawLines(surface,[w,h], [0,h], c2, numSegments) #LL  
        drawLines(surface,[w,0], [w,h], c3, numSegments) #LR works 
        drawLines(surface,[w,0], [w,h], c4, numSegments) #UR straight line?        
        
      
        #clock.tick(60)     
        
        pygame.display.update()
        
        
            
main()                                                   #this calls the main function to run the program
