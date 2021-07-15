import math
# def hypotenuse(a,b):
#     aSquared = a**2
#     bSquared = b**2
#     hypotenuse_squared= aSquared + bSquared
#     hypotenuse_value = math.sqrt(hypotenuse_squared)
#     return round(hypotenuse_value,2) # round to 2 decimal values

# print("The hypotenuse is " ,hypotenuse(5,7))
# print("The hypotenuse is " ,hypotenuse(9,12))

def Area_of_Circle(radius):
    radiusSquared = radius ** 2
    result = math.pi * radiusSquared
    return round(result,2)

print("Area of circle is ", Area_of_Circle(6))
print("Area of circle is " ,Area_of_Circle(2))
print("Area of circle is " ,Area_of_Circle(3))
