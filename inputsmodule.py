
name = 'Ahmed'
def askforInt(message):
    while True:
        userinput= input(message)
        if userinput.isdigit():
            return int(userinput)

        print("please try again enter valid number:")



print("------------ welcome to inputs module ------")
def askforStr(message):
    while True:
        userinput= input(message)
        if userinput.isalpha():
            return userinput

        print("please try again enter valid string ")