import math
epsilon = 0.0000001

def my_sqrt(a):
    x = a/5 # starting value for x
    while True:
        y = (x+ a/x) / 2.0
        if abs(y-x) < epsilon: # Rather than checking whether x and y are equal, better to use abs to compute the absolute value which epsilon = 0.0000001.
            return y
            break
        x = y

def test_sqrt():
    a=1 #starting value of a is 1 
    while a < 26: #loop to be calculated from 1 to 25 including 1
        a = a 
        mySqrt = my_sqrt(a) # find my_sqrt(a) by using my_sqrt() function
        mathSqrt = math.sqrt(a) # find math.sqrt(a)
        diff = abs(mySqrt-mathSqrt) # find absoulate diff between my_sqrt(a) and math.sqrt(a)
        print('a= ',a,' | ','my_sqrt(a) = ',mySqrt,' | ','math.sqrt(a) = ',mathSqrt,' | ','diff= ',diff )
        a = a + 1

test_sqrt()