#list = [1,4,8,[10,20,30],3,5]
#print(len(list)-2)
#print(list[3][1])
#print(list[::-1])

matrix=[["💀","💀","💀"],["💀","💀","💀"],["💀","💀","💀"]]

row = int(input("Enter a row number: "))
column = int(input("Enter a cloumn number: "))

matrix[row][column] = "❤️"
print(f"here is your updated matrix{matrix}")