alphabet = "abcdefghijklmnopqrstuvwxyz"   
test_dups = ["zzz","dog","bookkeeper","subdermatoglyphic","subdermatoglyphics"] 
test_miss = ["zzz","subdermatoglyphic","the quick brown fox jumps over the lazy dog"] 

# From Section 11.2 of: 
# Downey, A. (2015). Think Python: How to think like a computer scientist. Needham, Massachusetts: Green Tree Press. 
def histogram(s):
     d = dict()
     for c in s:
          if c not in d:
               d[c] = 1
          else:
               d[c] += 1
     return d 

# Part 1
def has_duplicates (strLetter):
    histogramItems = histogram(strLetter).items() # call Histogram Function() to Return collection of tuples with key is string and pair value is count of each letter 
    for key, count in histogramItems: # loop through tuple and check each pair value 
        if count > 1:
            return True # if pair value greater than one then return True
    return False

for item in test_dups:   # iterate through each item in the variable
    if has_duplicates(item): # pass the item into had_duplicates function if Retrun True then has duplicates
        print(item, " Has duplicates")
    else:
        print(item, "has not duplicate")

print("\n ------------------------- \n")

#part 2
def missing_letters(sLetter):
    newList = [] # create new empty list to store the returned data
    for items in alphabet: #iterate through all letters in alphabet
        if items not in histogram(sLetter): # if the letters are not returned from histogram
            newList.append(items) # then append them to the new list the items are not true.
            newList.sort() # sort the new list
    return "".join(newList)  # join betwen the items of list to return new string


for item in test_miss:
    missedLetters = missing_letters(item) # call the previous function and pass each item inside the test_miss list
    if len(missedLetters) > 0 or missedLetters != "": # handle the cases if the string either zero length or has empty space
        print(item + " is missing letters :  " + missedLetters)
    else :
        print(item + " uses all the letters .")

