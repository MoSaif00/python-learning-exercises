# Dictionary with name of employees as key and each employee has list of data [age, occupation, gender, country]
employees = { "Saif":[24, "Web developer","Male", "Yemen"],"Sami":[20, "Web developer","Male", "Syria"], "Salwa":[24,"Sales Manager","Female","Lithuania"],"Ahmed":[25,"Software Engineer","Male", "Yemen"]}

# From Section 11.5 of: 
# Downey, A. (2015). Think Python: How to think like a computer scientist. Needham, Massachusetts: Green Tree Press. 

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

# Original Dictionary
print("The Original Dictionary:")
print(employees)

print('\n ------------------ \n')

# Inverted Dictionary 
newInverted = invert_dict(employees)
print("The Inverted Dictionary :")
print(newInverted)