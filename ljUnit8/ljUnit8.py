import ast  #import abstract functions

# Dictionary with name of employees as key and each employee has list of data [age, occupation, gender, country]
employees = { "Saif":[24, "Web developer","Male", "Yemen"],"Sami":[20, "Web developer","Male", "Syria"], "Salwa":[24,"Sales Manager","Female","Lithuania"],"Ahmed":[25,"Software Engineer","Male", "Yemen"]}


# # From Section 11.5 of: 
# # Downey, A. (2015). Think Python: How to think like a computer scientist. Needham, Massachusetts: Green Tree Press. 
# function that passes a dictionary as parameter 
def invert_dict(d):
     inverse = dict() # empty dictionary to store the new inverted data
     for key in d:
          val = d[key]  
          for items in val: # iterate through each value of the origina keys. 
            if items not in inverse: 
                inverse[items] = [key]
            else:
                inverse[items].append(key)
     return inverse 

# write the dictionary items in new file as string format 
with open('employeesList.txt','w') as employeesStrList:
    employeesStrList.write("{\n")
    for key, value in employees.items():
        employeesStrList.write("'%s':%s, \n" %(key,value))
    employeesStrList.close()

# append three items to the previous list 
with open('employeesList.txt','a+') as employeesStrList:
    employeesStrList.write(
        "'Dyha':[20, 'Technician', 'Male', 'Turkey'], \n"
        "'Daniel':[33, 'Lead Manager', 'Male', 'Netherlands'], \n"
        "'Manal':[24, 'Marketing Manager', 'Female', 'Yemen'] \n"
    )
    employeesStrList.write('}')
    employeesStrList.close()

with open('employeesList.txt','r') as employeesDictList:
    dictList=[]
    dictList = ast.literal_eval(employeesDictList.read()) #convert the string list to dictionary using abstract build in function
    newInvertedDict = invert_dict(dictList)
    
    with open('employeesInvertedList.txt','w') as employeesInvertedList: # open new file to write the inverted dictionary 
        employeesInvertedList.write("{\n")
        for key, value in newInvertedDict.items():
            employeesInvertedList.write("'%s':%s, \n" %(key,value))
        employeesInvertedList.write("}")
        employeesInvertedList.close()

    # Original Dictionary
    print("The Original Dictionary:")
    print(dictList)
    print('\n ------------------ \n')
    # Inverted Dictionary 
    print("The Inverted Dictionary :")
    print(newInvertedDict)
    employeesDictList.close()


