# def any_lowercase1(s):
#      for c in s:
#         if c.islower():
#             return True
#         else:
#             return False
            
# print(any_lowercase1("Hai"))
# print(any_lowercase1("hAi"))
# print(any_lowercase1("hi"))
# print(any_lowercase1("HI"))
# print(any_lowercase1("HiH"))
# print(any_lowercase1("aH"))

# def any_lowercase2(s):
#      for c in s:
#         if 'c'.islower():
#             return 'True'
#         else:
#             return 'False'

            
# print(any_lowercase2("HI"))
# print(any_lowercase2("hAi"))
# print(any_lowercase2("hi"))

# It is not working because it just check 'c' not c in s , return value is string 

# def any_lowercase3(s):
#      for c in s:
#           flag = c.islower()
#      return flag

# print(any_lowercase3("Hai"))
# print(any_lowercase3("hAi"))
# print(any_lowercase3("hi"))
# print(any_lowercase3("HI"))
# print(any_lowercase3("HiH"))
# print(any_lowercase3("aH"))

# def any_lowercase4(s):
#      flag = False
#      for c in s:
#           flag = flag or c.islower()
#      return flag

# print(any_lowercase4("Hai"))
# print(any_lowercase4("hAi"))
# print(any_lowercase4("hi"))
# print(any_lowercase4("HI"))
# print(any_lowercase4("HiH"))
# print(any_lowercase4("aH"))
def any_lowercase5(s):
     for c in s:
        if not c.islower():
            return False
     return True
print(any_lowercase5("Hai"))
print(any_lowercase5("hAi"))
print(any_lowercase5("hi"))
print(any_lowercase5("HI"))
print(any_lowercase5("HiH"))
print(any_lowercase5("aH"))