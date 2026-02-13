#def add(*numbers):
 # c=0
  #for i in numbers:
 #   c =  c+i
 # print(f"The sum is {c}")    
#add(2,5,5)     

#def greet(name,dep):
 #   print(f"HI {name}")
  #  print(f"ARE U FROM {dep} department")
#greet("suman","AI&DS")

def info_person(**kwargs):
  for key,value in kwargs.items():
    print(key,value)
info_person(name = "SUMAN",age = 22, dep = "AI & DS")    
info_person(name = "MEGHANATH",dep = "CSE")

    