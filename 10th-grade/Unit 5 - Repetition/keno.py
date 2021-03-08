'''
Kesar Sampat 
Period 3: HCP
Unit 5: Repetition 
Keno Program
-lottery game, gets user input and compares numbers to randomly generated computer numbers
-gets certain amount of money after betting within $100 (to start with) and play again 

'''
import random

#asking for info to start 
print("Welcome to Kesar's Casino!")
    
#gets info from user 
def getInfo(name,money):

    answer = str(input(name+", you have $"+ str(money)+ ", would you like to play or quit? ")) 

    if answer == "play" or answer == "Play":    
       return True
    else:
        print("\nThanks for playing!")
        return False
        
        
#getting num between
def getNumBetween(prompt, low, high):
    
    num = low-1  #out of range value needed to enter the loop
    
    #while loop 
    while(num<low or num>high):
        #getting OGhigh num from user
        try:
            num = int(input(prompt))
            #num = int(input(prompt + " between " + str(low) + " and " + str(high) + ": "))
                      
            if num<low or num>high:
 
                print("Number entered is out of range. Please enter again. \n")
                
        except ValueError:
            print("Error - integer value expected\n")
            
    return num
#generates the computer number using random.randint + puts it into a list to store 
def generateCompNum():
    
    
    compList = []
    
    while len(compList) < 20:
        compNum = random.randint(1,80)
        
        if compNum not in compList:
            
            compList.append(compNum)
    
        
    return compList


#generates the user numbers and puts it into a list 
def generateUserNum():

    print("\nPlease enter 7 unique numbers between 1 and 80.\n")
    
    userNum = 1
    userList = []
    count = 1 
    
    while len(userList) <7:
        userNum = getNumBetween("Enter number "+ str(count) + ": " ,1, 80)
        
        if userNum not in userList:
            
            userList.append(userNum) 
            count += 1
        
        else:
            print("sorry, you already entered that number. Please choose another. ")
            
    return userList
        
       

#shows and gets the matches to compare

def getMatches(compList, userList, money, match):

    
    compList.sort()
    userList.sort()

    
    for i in range (len(userList)):
        if userList[i] in compList:
            match+=1
    
    
    print("The comptuer picks: ", compList)
    print("Your picks: ", userList)
    print("You matched", match, ". You win", money, "dollars!" )
    

def main():
    playAgain = True
    name = str(input("What is your name? "))
    while playAgain:
            
        money = 100
        userList = []
        compList = []
        match = 0 
            
        gameInPlay = getInfo(name, money)
        
        while (gameInPlay == True):
            
            
            bet = getNumBetween("How much would you like to bet? ", 1, money)
            userList = generateUserNum()
            compList = generateCompNum()
            
            
            if match < 4:
                money = bet 
            elif match == 4:
                money = bet
            elif match == 5:
                money = 20*bet
            elif match == 6:
                money = 200*bet
            elif match == 7:
                money = 12000*bet        
    
            break
        if len(userList) == 7:
            
            getMatches(compList, userList, money, match)
        #playing again 
        again = str(input("Do you want to play again? "))
        if again == "quit":
            playAgain = False
    
        if again == "play":
            money = (100-bet) + 400
            return money 
            
            
    print("Thanks for Playing!")
        

main() 

    
    
    