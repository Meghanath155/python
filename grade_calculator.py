m = int(input("marks in maths: "))
s = int(input("marks in science: "))
e = int(input("marks in english: "))

total_marks = m + s + e

average = total_marks / 3

percentage = (total_marks / 300)*100

grade = ''

if percentage > 90:
    grade = 'A'
elif percentage > 80:
    grade = 'B'
elif percentage > 70:
    grade = 'c'
else:
    grade = 'p'
    
print(f"total marks: {total_marks}") 
print(f"average: {average}")
print(f"percentage: {percentage}")
print(f"grade: {grade}")

            
