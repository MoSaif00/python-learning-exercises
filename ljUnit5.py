# prefixes = 'JKLMNOPQ'
# suffix = 'ack'
# for letter in prefixes:
#     if letter == 'Q' or letter == "O":
#         print(letter+'u'+suffix)
#     else:
#         print(letter + suffix)

# prefixes = 'JKLMNOPQ'
# suffix = 'ack'
# exceptionalLetters = 'OQ' # use this variable if we have many letters to except from prefix for more simple program
# for letter in prefixes:
#     if letter in exceptionalLetters:
#         print(letter+'u'+suffix)
#     else:
#         print(letter + suffix)

# s = "watermelon"
# reversed_string = s[::-1] # step value is -1
# print(reversed_string)

# s = "watermelon"
# new_substring2 =s[8:1:-2]
# print(new_substring2)

s = "watermelon"
negative_index = s[-8:-2] #first point exluded and end ponsition included.
print(negative_index)
