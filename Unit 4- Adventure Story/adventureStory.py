#Kesar Sampat 
#Period 3
#Assignment: Adventure Story 
#Description: create an adventure story with emojis and using pygame features 
#Credits: Luke Szfranski, Mrs. Klosky for starter template code.
#Note: all images must be saved to same directory as this python file.

import pygame, sys, math, random

#Initializing game engine
pygame.init()

#Set up drawing surface
w = 640
h = 550
size = (w,h)
surface = pygame.display.set_mode(size)

#Set window title bar
pygame.display.set_caption("Kesar Sampat Adventure Story")

#Color Constants
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
DARKGREEN = (25, 109, 0)

#Set Rectangle bounds of where Left and right decision images will be located- use pygame.RECT
LEFT= pygame.Rect((w/4)-80, h/3, 160, 160)
RIGHT= pygame.Rect(3*(w/4)-80, h/3, 160, 160)
MIDDLE= pygame.Rect((w/2)-80, 90, 160, 160)

'''
draws boxes & border around the drawing surface for the game
function written by Luke Szfranski
'''
def drawBorder():
    pygame.draw.rect(surface,DARKGREEN,(0,2*h/3,w,h/3),0)
    pygame.draw.rect(surface,BLACK,(0,0,w,20),0)
    pygame.draw.rect(surface,BLACK,(0,0,20,h),0)
    pygame.draw.rect(surface,BLACK,(0,h-20,w,20),0)
    pygame.draw.rect(surface,BLACK,(w-20,0,20,h),0)
    pygame.draw.rect(surface,BLACK,(0,2*h/3,w,20),0)

'''
displays text left aligned at the line location specified. words display in specified size
  words- the text to display
  line- either UPPERLINE, MIDDLELINE, LOWERLINE
  size- integer value of text size
'''
def displayText(words,line,size):
    font = pygame.font.SysFont('Arial',size,1,0)
    text = font.render(words,1,WHITE)
    bounds = text.get_rect()
    bounds.topleft = line
    surface.blit(text,bounds)
    
'''
displays an image file picture at the location specified
   location- tuple of x,y values of where to place the picture
   picture- image filename 
'''
def displayPicture(picture,location):
    surface.blit(pygame.image.load(picture).convert_alpha(),location)
    
'''
returns 3-picture tuple of the main image and two choices for the next level (level below current level)
   levelcode- next level of game to be played
'''
def getPictures(levelCode):
    
    if levelCode == "1":
        leftPic='creditCard.png'
        rightPic='standing.png'
        middlePic='roller.png' 
    elif levelCode == "2A":
        leftPic='friends.png'
        rightPic='person.png'
        middlePic='money.png'     
    elif levelCode == "2B":
        leftPic='lunch.png'
        rightPic='roller.png'
        middlePic='ride.png'   
    elif levelCode == "2C":
        leftPic='person.png'
        rightPic='friends.png'
        middlePic='smiling.png'   
    elif levelCode == "2D":
        leftPic='chair.png'
        rightPic='roller.png'
        middlePic='phone.png'   
    elif levelCode == "3A":
        leftPic='discount.png'
        rightPic='smiling.png' 
        middlePic='dontKnow.png'   
    elif levelCode == "3B":
        leftPic='smiling.png'
        rightPic='thumbsUp.png'
        middlePic='discount.png' 
    elif levelCode == "3C":
        leftPic='thumbsUp.png'
        rightPic='smiling.png'
        middlePic='discount.png' #change
    elif levelCode == "3D":
        leftPic='person.png'
        rightPic='vomit.png'
        middlePic='roller.png' 
    elif levelCode == "3E":
        leftPic='roller.png'
        rightPic='person.png'
        middlePic='sadFace.png'
    elif levelCode == "3F":
        leftPic='smiling.png'
        rightPic='person.png'
        middlePic='happy.png' 
    elif levelCode == "3G":
        leftPic='phone.png'
        rightPic='dontKnow.png'
        middlePic='sadFace.png'  #otherone
    elif levelCode == "3H":
        leftPic='person.png'
        rightPic='smiling.png'
        middlePic='noPhone.png'     
    
        
    return (leftPic,middlePic,rightPic)

    # Add your code here with if statements to set the left choice, middle (pic that describes current level), and right choice  
'''
    returns the game text at the current level
       levelCode- current level
'''
def getLevelText(levelCode):
    if levelCode == "1":
        return "You go to a theme park for the day. What do you do first? Check in or wait at the entrance?"
    elif levelCode == "2A":
        return "You made it just in time for the special discount. Do you lose the discount or stay in line? "
    elif levelCode == "2B":
        return "You lose the discount, but now you are with friends. Lunch or a ride?"
    elif levelCode == "2C":
        return "You check in but your one friend doesn't like roller coasters. Do you split up or stay as a group? "
    elif levelCode == "2D":
        return "Your phone died but you need it to see if your friends are here. Charge it again even though its not working or go inside the park? "
    elif levelCode == "3A":
        return "You give your friend the free pass and the discount. She is super grateful. "
    elif levelCode == "3B":
        return "You come back from the bathroom, but the line is even longer. "
    elif levelCode == "3C":
        return "You are hungry, so you eat lunch at a small cafe nearby. You are energized and ready to have fun. "
    elif levelCode == "3D":
        return "You throw up because you didn't eat anything. AND you went on a loopy ride.  "        
    elif levelCode == "3E":
        return "You and your friend got to go to more rides because of your small group. It was kind of lonely. "  
    elif levelCode == "3F":
        return "The lines were longer with all of your friends. You still had a bunch of fun "   
    elif levelCode == "3G":
        return "Your phone is charged but your happiness levels are not. You missed a bunch of the day because you were charging your phone. "  
    elif levelCode == "3H":
        return "It's all about living in the moment. Who needs a phone? You ditch charging your phone and go on the rides. "      
'''
returns the next game level based on the currentLevel and choice made
   choice- either 'left' or 'right'
'''
def getNextLevel(currentLevel, choice):
    if currentLevel == "1":
        if choice =="left":
            return random.choice(("2A", "2B"))
        elif choice == "right":
            return random.choice(("2C", "2D"))        
    if currentLevel == "2A":
        if choice == "left":
            return "3A" 
        elif choice == "right":
            return "3B"
    if currentLevel == "2B":
        if choice == "left":
            return "3C"
        elif choice == "right":
            return "3D"
    if currentLevel == "2C":
        if choice == "left":
            return "3E"
        elif choice == "right":
            return "3F"
    if currentLevel == "2D":
        if choice == "left":
            return "3G"
        elif choice == "right":
            return "3H"       
        
    return currentLevel
'''
returns the 3 sentences of the text to display
pre: line must be at least 2 sentences long; 
     1st sentence must end in a period.  
     If 3 sentences, 2nd must end in a ?
     
post:  first sentence will end with a period 
       second sentence will end with a question mark (if not end of game)
       third sentence will contain any remaining text (if it exists)
'''
def splitText(line):
    period1=line.find('.')
    sentence1=line[0:period1+1]
    questionMark=line.find('?')
    if questionMark!=-1:  #found a ?
        sentence2=line[period1+1:questionMark+1]
        sentence3=line[questionMark +1:]
    else:
        sentence2=line[period1+1:]
        sentence3=""
    return sentence1,sentence2,sentence3
    
'''
draws all of the game screen
'''
def drawScreen(gameStage):
     #placement of 3 text labels
    UPPERLINE =  (w/20,35* h/48)
    MIDDLELINE = (w/20,77* h/96)
    LOWERLINE =  (w/20,42* h/48) 
    
    drawBorder()
    
    #get level images and text to display
    gameText= getLevelText(gameStage)

    #split gametext to 3 lines for output using slices
    first, second, last = splitText(gameText)
    displayText(first,  UPPERLINE, 16)
    displayText(second, MIDDLELINE, 16)
    displayText(last,   LOWERLINE, 16)
    
    #returns tuple with 3 pix for that level (leftpicture, middlepicture, rightpicture)
    picsToDisplay=getPictures(gameStage) 
    displayPicture(picsToDisplay[0],LEFT) 
    displayPicture(picsToDisplay[1],MIDDLE)
    displayPicture(picsToDisplay[2],RIGHT)
     
#*------------------------------------------ MAIN PROGRAM LOOP----------------------------------*
def main():
    #story starts at stage 1
    stage = "1"    
    
    while(True):
        for event in pygame.event.get():
            if((event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                pygame.quit()
                sys.exit()
                
            #add code here for mouse click detection & collision check
            #code will check collision with the LEFT and RIGHT RECT objects and getNextLevel() of the game to execute
            
            #was mouse clicked inside of LEFT or RIGHT Picture?
           
            mousePos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if LEFT.collidepoint(mousePos) == True:
                    print("leftClick")
                    stage = getNextLevel(stage, "left")
                if RIGHT.collidepoint(mousePos) == True:
                    print("rightClick")
                    stage = getNextLevel(stage, "right")
    
       
        #Set Background Fill
        surface.fill(WHITE)
        
        #Drawing code goes here
        drawScreen(stage) 
       
        pygame.display.update()
main()