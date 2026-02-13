#CLACULATING THE BMI USING IF ELSE STATEMENTS
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meterts: "))

bmi = round(weight / height ** 2)

if bmi < 18.5:
    print(f"you are bmi is {bmi} and you are underweight")
elif bmi < 25:
    print(f"your bmi is {bmi} and You are normal")
elif bmi < 30:
    print(f"your bmi is {bmi} and you are overweight")
elif bmi < 35:
    print(f" your bmi is {bmi} and you are obese")
else:
    print("STAY HEALTHY") 