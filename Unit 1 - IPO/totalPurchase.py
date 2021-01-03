'''
Kesar Sampat 
Period 3 HCP
Unit 1 - IPO
Making a program to find out how many cookies user wants 
'''
try:
    
    print("Welcome to the Ram Supply Outlet!")
    print("---------------------------------")
    
    item1 = str(input("Enter name of item 1: "))
    price1 = float(input("Enter price of" + " " + item1 + ": "))
    item2 = str(input("Enter name of item 2: "))
    price2 = float(input("Enter price of" + " " + item2 + ": "))
    item3 = str(input("Enter name of item 3: "))
    price3 = float(input("Enter price of" + " " + item3 + ": "))
    item4 = str(input("Enter name of item 4: "))
    price4 = float(input("Enter price of" + " " + item4 + ": "))
    
    subtotal = price1 + price2 + price3 + price4
    tax = (0.07 *subtotal)
    totalDue = tax + subtotal
    
    print("---------------------------------")
    
    strFormat = "{0:<20s}{1:>.2f}"  
    strFormatTitle = "{0:<20s}{1:>.7s}" 
    
    
    print("Order Summary:")
    print(strFormatTitle.format("Item" , "Price"))
    print(strFormatTitle.format("----" ,  "-----"))
    print(strFormat.format(item1, price1 ))
    print(strFormat.format(item2 , price2 ))
    print(strFormat.format(item3 , price3))
    print(strFormat.format(item4 , price4))
    print("---------------------------------")
    
    print(strFormat.format("Subtotal: " , subtotal ))
    print(strFormat.format("Tax: " , tax ))
    print(strFormat.format("Total Due: " , totalDue ))
    print("---------------------------------")
   
    amountTendered = float(input("Enter amount tendered: "))
    changeDue = amountTendered - totalDue   
    
    print(strFormat.format("Amount tendered", amountTendered))
    print(strFormat.format("Change due: " , changeDue ))
    
    input("Press Enter to Quit")
    
except ValueError:
    
    print("Please enter the correct total")