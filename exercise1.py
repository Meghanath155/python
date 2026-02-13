 # finding out the age (how many days, weeks, month) how many days left to live
 
age = int(input("Enter your age: "))

years_left = 90 - age
days = years_left * 365
weeks_left = years_left * 52
months_left = years_left * 12

print(f"You have {days} days, {weeks_left} weeks, and {months_left} months left.")

