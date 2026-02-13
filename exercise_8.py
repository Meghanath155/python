numbers = input("Enter a numbers: ").split()
count = 0
for i in numbers:
    count += 1
print("The lenght of the list: ",count)
maximum_number = numbers[0]
for number in numbers:
    if number > maximum_number:
        maximum_number = number
print(f"The maximum number is:{maximum_number}")