# TO CLIMB THE ROLLER COSTER IN THE AMUSEMENT PARK 
# CREATING A RULES FOR THE RIDE ( USING IF ELSE IF STATEMENTS)

height = int(input("Enter your height:"))
bill = 0
if height >= 3:
    print("You can ride the roller coaster")
    age = int(input("Enter your age: "))
    if age < 12:
        bill = 150
        print("Your ticket price is 1500")
    elif age < 18:
        bill = 250
        print("Your ticket price is 250")
    elif age >= 18:
        bill = 500
        print("Your ticker price is 500")
    want_photo = input("do you want a photo Y or N: ").lower()
    if want_photo == "y":
        bill += 50
        print(f"Your total bill is {bill}")
print("Thank u for visiting")        