'''
Kesar Sampat 
Period 3: HCP
Unit 5: Repetition 
-Program to play a guessing game with the user
-Demo of while loops 

'''
import random 

#returns a game rating based on the number of tries and original game hi value

def getRating(numGuesses, ogGameHigh):
    
    #calculates 
    equalizer = 1000/ogGameHigh
    
    rating = numGuesses/equalizer * 100
    
    #percentages to find out ratings 
    
    if rating>=80:
        print("Rating: Outstanding!")
    elif rating>=70:
        print("Rating: Nice!!")  
    elif rating>=40:
        print("Rating: Fair!")      
    elif rating<40:
        print("Rating: Poor") 

    return rating

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


def main():
    #defining variables
    playAgain = True
    
    while playAgain:
        
        ogGameHigh = getNumBetween("Enter upper bound for the guessing game ", 1, 1000)
        guess = 0 
        secret = random.randint(1, ogGameHigh)
        low = 1
        high = ogGameHigh
        numGuesses = 0  
        
        
        
        print("Let's play a guessing game!")
        print("I am thinking of a number between", low, "and", high)
        
        while (secret != guess):
            guess = getNumBetween("Enter guess", low, high)
            numGuesses +=1
            
            #check guess (right, too low, too high)
            
            if guess == secret:
                print("\nYou won in" , numGuesses, "guesses \n")
                getRating(numGuesses, ogGameHigh) 
    
            elif guess < secret:
                print("That guess is too low")
                low = guess +1
            else:
                print("That guess is too high")
                high = guess -1
                
                
        again = str(input("Do you want to play again? (yes or no): "))
        if again == "no":
            playAgain = False

    print("Thanks for Playing!")     
 
main()

#play again feature until user chooses to quit DONE 

#thank user for playing once game is over DONE 

#rating DONE
