'''
Kesar Sampat 
Period 3 HCP
Unit 1 - IPO
Making a program to find out how many cookies user wants 
'''
try:
    cookies = int(input("Enter the number of cookies you would like to make: "))
        
    print("Use the following amounts to complete the recipe:")
        
    strFormatFirst = "{0:<20s}{1:>2d}" 
    strFormat = "{0:<20s}{1:>.2f}" 

    print(strFormatFirst.format("# of Cookies:" , cookies))
    print(strFormat.format("Sugar (cups):" , (cookies*1.5)/48))
    print(strFormat.format("Butter (cups):",  (cookies*1)/48))
    print(strFormat.format("Flour(cups):",  (cookies*2.75)/48))
        
    input("Press Enter to Quit")

except ValueError:
    print("Please enter a number")



    
    
    
    



