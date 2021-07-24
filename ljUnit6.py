# #1
# example = 'I drink coffee every morning'
# print('Main String :', example)

# #2
# exampleList = example.split()
# print('The string turned into List : ',exampleList)

# #3
# exampleList.pop(4)
# print('list after using pop :',exampleList)
# del exampleList[0]
# print('list after using delete operator :',exampleList)
# exampleList.remove('every')
# print('list after using remove :',exampleList)

# #4
# exampleList.sort()
# print('sorted list:',exampleList)

# #5
# exampleList.append('every')
# print("new list after appending: ",exampleList)
# exampleList.extend(['night'])
# print("new list after extending new list: ",exampleList)
# exampleList.insert(0,'I')
# print("new list after inserting new element: ",exampleList)

# #6
# delimiter = ' '
# exampleList = delimiter.join(exampleList)
# print("Single string using join : ", exampleList)

#part2

# #1
# characterList = ['Mo', 24, 1.70]
# skills = ['coding','cooking','football']
# characterList.append(skills)
# print('nested list : ' , characterList)

# #2
# horray = ['horray']
# cheering = horray * 5
# print(horray)
# print('Our team won: ',cheering)

# #3
# oldHobbies = ['reading','football','running','chess','movies','sleeping']
# newHobbies = oldHobbies[:4]
# print('My old Hobbies : ',oldHobbies)
# print('My new Hobbies : ',newHobbies)

# #4 
# marks = [95,75,80,85,90]
# total = 0 
# for mark in marks:
#     total += mark

# print("total marks :", total)

# #5
# gradesAndMarks = ['a', 90,'a',95,'b',85,'b',84,'c',75]
# onlyGrades = []
# for item in gradesAndMarks:
#     if type(item) == str:
#         onlyGrades.append(item)

# print('Print only grades: ' ,onlyGrades)

#6


goals2021 = ['drivingLicence', 'camping','new Job']
newGoal='graduation'
GoalsList = goals2021.append(newGoal) #Legal but Wrong, GoalsList will return None 
print(GoalsList)
print(goals2021) # Append method modifies the main object

goals2021.append(newGoal) # correct way 