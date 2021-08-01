# dict = {'Saif':24,'Sami':30,'Salem':27,'Nora':20}

# for key, value in dict:
#     print(key)
#     print(value)

# dict = {'Saif':24,'Sami':30,'Salem':27,'Nora':20}

# tupleDict =dict.items() # turn dictionary to list of tuples

# print(tupleDict)
# print(type(tupleDict[1])) # check index 1 for type if it is tuple of not.

# for key, value in tupleDict:  # loop through the collection of tuples
#     print("name: " + key + " | age : " + str(value)) # Print keys and its values

# names = ['Saif','Sami','Salem','Nora','Ahmed']
# # ages = ['Saif','Sami','Salem','Nora','Ahmed']
# # jobs = ['Saif','Sami','Salem','Nora','Ahmed']
# ages = [24,30,27,20]
# jobs = ['developer','teacher','Lawyer','Lawyer','developer']

# tuplesList= list(zip(names,ages,jobs))
# print(tuplesList)
# # def hasmatch(t1,t2,t3):
# #     for x, y, z in zip(t1,t2, t3):
# #         if x==y==z:
# #             return True
# #     return False 

# # print(hasmatch(names,ages,jobs))   
    
# for x, y, z in tuplesList:
#     print( x + " is " + str(y) +  " years old and works as "+ z)

# names = ['Saif','Sami','Salem','Nora','Ahmed']

# for i, element in enumerate(names):
#     print("index "+str(i)+ " Element is : "+element)