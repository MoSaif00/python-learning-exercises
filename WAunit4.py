def is_divisible(x, y): #function to check if the x is divisible by y without remaining value
    return x % y == 0  # == operator work as bollean condition, so if it is divisible will return true or else will return false
        
def is_power(x,y):   # function to check if x is power of y which include recursive function is_power()
    if x == 1 or y==1: #to check if x or y is equal to 1 because 1 is power of 1 
        return x==1  # In both cases will return 1 as true value

    if not is_divisible(x ,y): # check if the x and y is not divisible then will return false
        return False
        
    return is_power(x/y, y)  #recursive function which will apply the same function again if the all cases are passed .
    


print("is_power(10, 2) returns: ", is_power(10, 2)) #expected to be False
print("is_power(27, 3) returns: ", is_power(27, 3)) #expected to be True
print("is_power(1, 1) returns: ", is_power(1, 1)) #expected to be True
print("is_power(10, 1) returns: ", is_power(10, 1)) #expected to be False
print("is_power(3, 3) returns: ", is_power(3, 3))  #expected to be True