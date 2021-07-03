import math
def  print_volume(r):
    volume = (4/3)*math.pi*(r**3)
    print("The volume_of_sphere is",volume)
 
print_volume(3.5)
print_volume(12)
print_volume(20)

def drink_age(age):
    if age >= 21:
        print("Because your age is",age,",Then you are allowed to drink")
    elif age > 15:
        print("You need to take your parents permission to drink in this age")
    else:
        print("Please, don't drink in the age",age)

drink_age(20)
drink_age(21)
drink_age(10)