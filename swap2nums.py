# swapping two nums without using temp variable
# a =10, b =20 after swaping a =20 b =10


#a = int(input("give a : "))
#b = int(input("give b : "))

#b = b+a
#a = b-a
#b = b-a

#print(f"value of a is: {a}")
#print(f"value of b is : {b}")

##>>>>> swapping varaibles using fuctions

def swap(a,b):
    b = b+a
    a = b-a 
    b = b-a
    print(f"value of a is: {a}")
    print(f"value of b is: {b}")
    
swap(5,10)
swap(20,30)