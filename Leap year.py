def leap_year():
    print()
    year=int(input("Enter a year >>"))
    if(year%4==0 and year%100!=0 or year%400==0):
        print("It is a leap year")
        print("******")
        print()
        wcontinue()
    else:
        print("It is a not leap year")
        print("******")
        print()
        wcontinue()


    
def height_calc():
    print()
    height=int(input("Enter height in cm >>"))
    inches=height/0.394
    feet=height/0.0328
    print("Your height in inches is",round(inches,2))
    print("Your height in feet is",round(feet,2))
    print("******")
    print()
    wcontinue()

def wcontinue():
    check=input("Wanna continue? (Yes/No)>>")
    if(check=="yes"or check=="Yes"):
        print()
        options()
    elif(check=="no" or check=="No"):
        print("Thank You")
    else:
        print()
        print("Invalid Input, Try again")
        wcontinue()

    
def options():
    print("Want to check for a leap year or convert you height in to inches and feet?")
    print("1) Leap Year")
    print("2) Converter")
    what=int(input("Which option (1,2) >>"))
    if(what==1):
        
        leap_year()
    elif(what==2):
        
        height_calc()
    else:
        print()
        print("Invalid option, Try again")
        options()


        
what=0
options()


        
    
    
    
