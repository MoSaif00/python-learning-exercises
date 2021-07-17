# prefixes = 'JKLMNOPQ'
# suffix = 'ack'
# for letter in prefixes:
#     if letter == "O" or letter == "Q":
#         print(letter + "u" + suffix)
#     else:
#         print(letter + suffix)

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)