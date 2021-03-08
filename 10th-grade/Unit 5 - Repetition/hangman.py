'''
Kesar Sampat 
Period 3: HCP
Unit 5: Repetition 
-Program to play hangman with user - use this logic to combine with the pygame (console version) 

'''

import random
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
def drawHangman():
    drawGallows()
    head()
    body()
    armR()
    armL()
    legR()
    legL()
    
#returns a random word to play hangman with
def getGameWord():
    words = ["computer", "concatenation", "binary", "function", "abstraction","programming", "python", "statement"]
    
    return random.choice(words)

def main():
    gameWord = getGameWord()
    print(gameWord)
    
    
drawHangman()    
main()