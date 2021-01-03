'''
Kesar Sampat 
Period 3 HCP
Unit 1 - IPO
Making a program that prompts the user for an amount of change
'''
try:
    cents = int(input("Enter an amount of cents: "))
    
    
    print("Change for", cents , "cents")
    print("-------------------")
    
    
    quarters = (cents//25) 
    cents = cents%25
    
    dime = (cents//10)
    cents = cents%10
    
    nickel = (cents//5)
    cents = cents%5
    
    pennies = (cents//1) 
    
 
    
    print( quarters, "Quarters")
    print(dime, "Dime")
    print(nickel, "Nickel")
    print(pennies, "Pennies")
    
    input("Press Enter to Quit")
    
except ValueError:
    print("Please Enter a Number")

