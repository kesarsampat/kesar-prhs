'''
Student Name: Kesar Sampat 
Game title: Hangman Pygame 
Period: 3
Features of Game: use pygame features to create a hangman game w/ user 
'''

import pygame, sys, random                                    #pulls in the special code functions for pygame
pygame.init()                                           #initialize game engine

w=800                                                   #Open and set window size
h=600                                                   #must code graphics to auto resize based on window size
size=(w,h)
surface = pygame.display.set_mode(size)
xu = w/9
yu = h/14  


pygame.display.set_caption("Hangman")          #set window title

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
def drawGallows():
    pygame.draw.rect(surface, BLACK, (xu*2, yu*10, w/2, h/4))
    pygame.draw.line(surface, BLACK, (xu*4.3, yu*10), (xu*4.3, yu), 8)
    pygame.draw.line(surface, BLACK, (xu*4.3, yu), (xu*5.5, yu),  8)
    pygame.draw.line(surface, BLACK, (xu*5.5, yu), (xu*5.5, yu*3), 8)
def head():
    pygame.draw.ellipse(surface, BLACK,(xu*5, yu*3 , xu, yu*2), 6)
def body():
    pygame.draw.line(surface, BLACK, [xu*5.5, yu*5], [xu*5.5, yu*7.5], 4)
def armR():
    pygame.draw.line(surface, BLACK, [xu*5.5,yu*6.5], [xu*5,yu*5.5], 5)    
def armL():
    pygame.draw.line(surface, BLACK, [xu*5.5,yu*6.5], [xu*6,yu*5.5], 5)
def legR():
    pygame.draw.line(surface, BLACK, [xu*5.5, yu*7.5], [xu*5.1, yu*9], 5)
def legL():
    pygame.draw.line(surface, BLACK, [xu*5.5, yu*7.5], [xu*5.8, yu*9], 5)
    
#draws the hangman    
def drawHangman(numWrong,gameWord): #add parameter
    if numWrong == 1:
        head()
    if numWrong == 2:
        head()
        body()
    if numWrong == 3:
        head()
        body()
        armL()
    if numWrong == 4:
        head()
        body()
        armL()
        armR()
    if numWrong == 5:
        head()
        body()
        armL()
        armR()
        legL()
    if numWrong == 6:
        head()
        body()
        armL()
        armR()
        legL()
        legR()
        showMessage("YOU LOST!", 60, w/2, h/2, RED, bg=BLACK)
        showMessage(gameWord, 30, w/2, h/27, BLACK, bg=WHITE) 
        showMessage("Press enter to play again", 20, w/2, h-200, WHITE, bg=BLACK)
    
#returns a random word to play hangman with
def getGameWord():
    words = ["computer", "concatenation", "binary", "function", "abstraction","programming", "python", "statement"]
    
    return random.choice(words)

#return true if guess is valid, false otherwise  
def isValidGuess(letter,lettersGuessed):
    if len(letter) != 1:
        return False 
    if letter in lettersGuessed:
        return False 
    if letter<'a' or letter> 'z':
        return False 
    return True     #letter is valid 

#updates the user's guessed word based on the letters guessed 
def updateGuessedWord(lettersGuessed, gameWord):
    newWord = ""
    for letter in gameWord: #check each letter to see if it was guessed 
        if letter in lettersGuessed:
            newWord+=letter
        else:
            newWord+='-'
            
    return newWord 

#function to show message 
def showMessage(words, size, x, y, color, bg=None):
    font = pygame.font.SysFont("Calibri", size, True, False,)
    text = font.render(words,True, color, bg)
    textBounds = text.get_rect()
    textBounds.center=(x,y)
    surface.blit( text, textBounds)

def drawScreen(lettersGuessed,wordsoFar,numWrong,gameWord):
    drawGallows()
    #winner
    if numWrong <=6 and wordsoFar == gameWord:
        #sound
        correct = pygame.mixer.Sound('pickup.wav')
        correct.play()   
        
        showMessage("Winner!", 60, w/2, h/2, WHITE, bg=BLACK)
        #play again
        showMessage("Press enter to play again", 20, w/2, h/4, WHITE, bg=BLACK)
    #displaying used letters title
    showMessage("".join(lettersGuessed), 20, w/2, h-100, RED)
    showMessage(wordsoFar, 40, w/2, h/24, BLACK)    
    drawHangman(numWrong,gameWord)

# -------- Main Program Loop -----------
def main():                                             #every program should have a main function
                                                        #other functions go above main
    gameInPlay = True
    gameWord = getGameWord()
    wordsoFar = "-"*len(gameWord)                       #creates initial dashes to show number of letters
    numWrong = 0                                        #gameover when num = 6 or word is guessed 
    lettersGuessed = []    
    
    while (True):
        
        for event in pygame.event.get():                #get all events in the last 1/60 sec & process them
            
            if ( event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
                pygame.quit();                          #for ending the game & closing window
                sys.exit();
        
            # if your program has a button, mouse, or keyboard interaction, code goes at this indentation level
            #ending game
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and gameInPlay == False:
                drawScreen(lettersGuessed, wordsoFar, numWrong, gameWord)
     
            #allowing user to input letters from the keyboard 
          
            if event.type == pygame.KEYDOWN and gameInPlay == True:
                letter = event.unicode.lower()
                if isValidGuess(letter,lettersGuessed):
                    #process the guess 
                    lettersGuessed.append(letter)       #add to used letters
                    if letter not in gameWord:
                        numWrong += 1 
                    wordsoFar = updateGuessedWord(lettersGuessed, gameWord)
                    
                                  
     
        surface.fill(WHITE)                             #set background color
        drawScreen(lettersGuessed, wordsoFar,numWrong, gameWord)
       
        
        
        
        #clock.tick(60)                                  #Change FPS - frames per sec- when animating
        pygame.display.update()                          #updates the screen- usually in main
        
        
        
            
main()                                                   #this calls the main function to run the program
