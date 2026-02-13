import math
def paint_calculation(height, width, cover):
        area = height * width
        number_of_cans = math.ceil(area / cover)
        print(f"you need {number_of_cans} cans of paint ")
h = int(input("Enter the height of wall: "))
w = int(input("Enter the width of wall: ")) 
coverage = 7
paint_calculation(height = h , width = w , cover = 5)

                             