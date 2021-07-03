# #1
# def print_value(arg_value):
#     print('I am fan of ', arg_value)


# #2 
# fav_fruit="Orange"
# print_value("Apple")
# print_value(fav_fruit)
# print_value("Sushi "*2)

#3
# def func_local_var(): #defined function with local variable.
#     my_name="Saif"
#     print("My name is ",my_name)

# func_local_var()
# print(my_name)

#4 
# def print_para(saif):
#     print("My name is ",saif)

# print_para("Saif")

# print(saif)


# 5
my_name="Mo"

def print_name():
    my_name="Saif"
    print("Local Variable ",my_name)

print_name()
print("Global Variable ",my_name)