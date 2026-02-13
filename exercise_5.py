# leap year checker

year = int(input("Enter a year: "))

leap = False 

if year % 4 == 0:
    print("True")
elif year % 100 == 0 & year % 400 == 0:
    print("False")    
else:
    print("False")    