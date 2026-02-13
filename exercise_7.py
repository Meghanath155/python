# calculate the average highet form a list of height

height = (input("Enter all the digits sepearted by a space: "))
height_split = height.split()
count = 0
for height in height_split:
    count = count+1
print(count)   
for i in range(count):
    height_split[i] = int(height_split[i])
total = 0
for person in height_split:
    total += person
avg = total / count
print(round(avg))        