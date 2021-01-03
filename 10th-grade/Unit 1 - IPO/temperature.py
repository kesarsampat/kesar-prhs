'''
Kesar Sampat 
HCP 3
Unit 1 - IPO 
Temperature Conversion 

'''
try:
    temp = float(input("Type in a temperature in Fahrenheit:"))
    celsius = (temp - 32)*(5/9)
               
    print("{0:.1f} degrees Fahrenheit = {1:.1f} degrees celsius".format(temp, celsius))
    
               
            
except ValueError:
    print("Please type in a number:")
