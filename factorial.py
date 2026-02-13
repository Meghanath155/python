n = int(input("give n value: "))
#printing factorial using a while loop
# n = 5 , expected output: 120
#factorial = 1
#while n > 0:
#     factorial *= n
#     n -= 1
#     print(factorial)

#>>> printing factorial using a for loop
factorial = 1
for i in range(1, n+1):
    factorial *= i
    
    print(factorial)
    
    