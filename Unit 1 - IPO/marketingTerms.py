'''
Kesar Sampat 
Period 3 HCP
Unit 1 - IPO
Make a program that allows the user to enter certain inputs to output the markup, percentage, etc. 
'''
try:
    
    print("Profit Calculator")
    print("-----------------")
    itemName = str(input("Enter the name of your stock item: "))
    purchasePrice = float(input("Enter purchase price:  "))
    sellingPrice = float(input("Enter selling price: "))
    markup = sellingPrice - purchasePrice 
    
    strFormat="{0:22s}{1:.1f}%"
    strFormatDiff="{0:22s}${1:.2f}"
    
  
  
    print("---Profit Results for Brooks Adrenaline Running Shoe---")
    
    print(strFormatDiff.format("Markup:" ,markup))
    print(strFormat.format("Percentage Markup:" , markup/purchasePrice *100 ))
    print(strFormat.format("Profit Margin:", markup/sellingPrice *100 ))
          
    input("Press Enter to Quit")

except ValueError:
    print("Please enter a number or Item")