'''
Kesar Sampat 
Period 3: HCP
Unit 5: Repetition 
-code step by step guess2d

'''
import random

print("This program is a 2-D guessing game. \nI will think of a point somewhere \nbetween (1, 1) and (100, 100) \nand give hints until you guess it.")
playAgain = True
pointx = random.randint(1,20)
pointy = random.randint(1,20)
nums = 1
guesses = 0 
print("\n")
   
while playAgain:
    if nums != pointx or pointy:
    
        nums = input("Guess x and y: ").split() #x and y 
        numx = nums[0]
        numy = nums[1]
        print(pointx, pointy)
    
        distance = ((int(pointx)-int(numx))**2) + ((int(pointy)-int(numy)**2))
    
        if distance == 1.5:
            print("You're hot.")
            guesses =+ 1
        elif distance <= 5.0:
            print("You're warm. ")
            guesses =+ 1
        elif distance > 5.0:
            print("You're cold.")
            guesses =+ 1
        if distance == 0:
            
            print("You got it right in", guesses, "guesses!")
            
            
          
            
                            
again = str(input("Play again? "))
        
if again == "no":
    playAgain = False                    

                
                
            
    #if pointx > numx:
        #print("Go east")    
    #elif pointx < numx:
        #print("Go west")
    #elif pointy > numy:
        #print("Go south")
    #elif pointy < numy:
        #print("Go north")        
    
   
        
        

    
    
        
        
    
    
    
    




          