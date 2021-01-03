'''
Kesar Sampat 
Period 3 - HCP
Unit 4 Decisions 
Program to obtain a score from the user and determine % and letter 
'''
def getGrade(perc):
    
    perc*=100
    
    if perc >=90:
        return "A"
    elif perc >=80:
        return "B"
    elif perc >=70:
        return "C"
    elif perc >=60:
        return "D"
    else:
        return "F"
    
    
def main():
    
    try:
        score = float(input("Enter your quiz score: "))
        possible = float(input("Enter points possible: "))
        
        percent = score/possible 
        
        #letterGrade = getGrade(percent)
        
        print("You scored {:.1%}".format(percent))
        print("Your grade is", getGrade(percent))
        
    except ValueError:
        
        print("Error-enter numeric scores only")
        
main()
        
        
        

