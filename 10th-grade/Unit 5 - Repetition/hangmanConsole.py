'''
Kesar Sampat 
Period 3: HCP
Unit 5: Repetition 
-Program to play hangman with user - use this logic to combine with the pygame (console version) 

'''

import random

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
    
    

def main():
    gameWord = getGameWord()
    wordsoFar = "-"*len(gameWord)   #creates initial dashes to show number of letters
    numWrong = 0                    #gameover when num = 6 or word is guessed 
    lettersGuessed = []
    
    print("Let's play Hangman!")
    
    while (numWrong<6 and gameWord != wordsoFar):
        print("Your Guessed Word: ", wordsoFar)
        print("You have", 6-numWrong, "incorrect guesses left")
        print("Used letters:", " ".join(lettersGuessed))
        
        letter = input("Guess a Letter:").lower()
        if (isValidGuess(letter,lettersGuessed)):
            #process the guess 
            lettersGuessed.append(letter)       #add to used letters
            if letter not in gameWord:
                numWrong += 1 
            wordsoFar = updateGuessedWord(lettersGuessed, gameWord)
                 
            
            
            
        else:
            print("Invalid guess")
            
    
    
    
    
main()