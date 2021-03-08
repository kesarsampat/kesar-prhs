#import random 


#print("Welcome to Piglet!")
#dice = 0 
#sum = 0 


#while True:
    #dice = random.randint(0,6)
    #sum += dice 
    
    #if dice > 1:
        #print("You rolled a" , dice)
        #answer = str(input("Roll again? "))
        #if dice == 1:
                   
            #print("You got 0 points.")
            #break
        
            
        #if answer == "no":
            #print("You got", sum, "points.") 
            #break
        
        
                

     
      
   
            
        
        
#roll two dice 

#import random 


#sum = int(input("Desired sum: "))




#while True:
    #dice1 = random.randint(1,7)
    #dice2 = random.randint(1,7)
    
    #answer = dice1 + dice2
    
    #print(dice1, "and", dice2, "=" ,answer)
    
    ##if answer == sum:
        ##break
    
def printAverage():

    count = 0
    sum = 0 
    num = 1 
    
    while True:
        
        if num > 0:

            num = int(input("Type a number: "))
    
            sum += num
                
            count +=1

        if num < 0:
             
            print("Average was", sum/count)
            break
        

printAverage()

def print_average():

    count = 0
    sum = 0 
    num = 1 
    
    while True:
        num = int(input("Type a number: "))

        if num >= 0:

            sum += num
                
            count +=1
            
        if num < 0:
            break

    print("Average was", sum/count)
    
    
    
    
    coinFlip = []
    
    
    coin = random.randint(1,10)
    
    while True:
        
        if coin >=5:
            coinFlip.append("H")
        if coin <=5:
            coinFlip.append("T")
        break
        
    print(coinFlip)    
    
            
            
    
    
        
       

    
    
    
        
           
        
    
  

            
          
            
            






    
    




