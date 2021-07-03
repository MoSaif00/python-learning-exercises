# function contains the line with only dot
def new_line():
    print('.')

# function nested with three lines
def three_lines():
    new_line()
    new_line()
    new_line()

# to print 9 lines by nesting threeLine() function
def nine_lines():
    three_lines()
    three_lines()
    three_lines()

# function to print 25 lines
def clear_screen():
    nine_lines()
    nine_lines()
    three_lines()
    three_lines()
    new_line()


# main section to call nineLines() and clearScreen Functions 
# #source https://www.journaldev.com/17752/python-main-function
def main():
    print("Printing first 9 lines")
    nine_lines()
    print("Calling clearScreen() function with 25 lines")
    clear_screen()
    
if __name__ == "__main__":
    # execute only if run as a script
    main()