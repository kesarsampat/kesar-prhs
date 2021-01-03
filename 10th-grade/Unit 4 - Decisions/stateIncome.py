'''
Kesar Sampat 
Period 3 - HCP
Unit 4 Decisions 
program to calculate the state income tax for a family based on their taxable income
'''

def calcTax(inc):
    tax = 0

    if inc <= 20000:
        tax = 0.02 *inc  
    else:
        if inc <= 50000:
            tax = 400 + 0.025 * (inc - 20000) #check after school
        else:
            tax = 1150 + 0.035 * (inc - 50000)
    return tax 
        
def main(): 
    print("State Income Tax Calculator")
    print("---------------------------")    
    try:   
        income = float(input("Enter Your taxable income: "))  
               
        if income >= 0:
            finalTax = calcTax(income)
            
            print("State income tax for the year is ${:.2f}".format(finalTax))  
        else:
            print("\n")
            print("enter a postive value only")
        
        
        
        
    except ValueError:
        print("error-postive numerical income values only")
        
    #add a space before like example n thing
    print("\n")
    input(("Press Enter key to exit..."))
    
        
         
main()    

