def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)


def countup(n):
    if n >= 0:
        print('Blastoff!')
    else:
        print(n)
        countup(n+1)

number = int(input("What is the number you would like to count \n"))
if number > 0 :
    print("start counting")
    countdown(number)
elif number < 0:
    print("start counting")
    countup(number)
else:
    print('Blastoff!')

