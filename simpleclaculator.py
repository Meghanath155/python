num1 = int(input("Enter your first num: "))
num2 = int(input("Enter your second num: "))

operator = input("give operator: ")

if operator == "+":
    print(f"Addition of two nums is {num1 + num2}")

elif operator == "-":
    print(f"Subtraction of two nums is {num1 - num2}")

elif operator == "*":
    print(f"Multiplication of two nums is {num1 * num2}")

elif operator == "/":
    print(f"Division of two nums is {num1 / num2}")
                
else :
    print("Invalid operator!")
                    