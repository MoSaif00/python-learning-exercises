#1




import os


try:
    mainDir = os.path.abspath('text.txt') #By mistake i used file name instead of directory name
    listDir = os.listdir(mainDir) # I wass suppose to get two dir names which 'hi' 'hii'
    print(listDir)
except Exception as err:
    print("There is an error occurred :",err)
