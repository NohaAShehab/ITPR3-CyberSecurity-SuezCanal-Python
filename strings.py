

"""

    string is sequence of chars
    any operation you apply on the string --> results in new string
    ---> string is immutable --> cannot be changed after created

"""

"1- to define  a string "
message = 'Hello world'

"""2- string treated like an array  you can access string parts using index start from zero"""
# print(message[2])   # return new string
# print(message[2:8]) # chars from start to end-1
# print(message[2:])
# print(message[3:33])
# print(message[30])
# print(message[-1])
# print(message[::-1])  # new string
# print(message)
"""3- get length of the string """
# print(len(message))

"""4- count chars in the string --> count char or sequence of chars in the string """
message = "Python is easy, we are enjoying it."
print(message.count('i'))
print(message.count('it'))

"""5- get index of char in the string"""
print(message.index('i'))  # return with the index of the first occurrence of the string.

""" 6- string concatenation """
fname = 'Noha '
midname='Abdelhady '
lname= 'Shehab'

# fullname = fname + midname + midname + lname
# print(fullname)

# mymessage = fname + 10  #  can only concatenate str (not "int") to str
"""7- string interpolation """
# fullname = fname + midname*2 + lname
# print(fullname)
# print("____ "*17)
# print("____|"*17)

"""8- string format """
# fname = input("please enter your firstname name: ")
# lname = input("please enter last name: ")
# message = input("please leave your message: ")

""" your firstname is    , lastname    , message is  """
# temp = "your firstname is {0}, lastname {1}, message is {2}"
# # print(temp.format(fname, lname, message))
# print(temp.format(fname, message, lname))  # you must pass the arguments in correct order
# #### temp.format ---> return new string

#
# temp = "your firstname is {myfirstname}, lastname {mylastname}, message is {mymessage}"
# print(temp)
# print(temp.format(myfirstname=fname,mymessage=message,mylastname=lname))

"""f-format string ==> use existing variables in create new string  """
#
# name = 'Ahmed'
# age = 25
# # temp = f"my name is {name}," + str(age)
# temp = f"my name is {name}, age = {age}"  #
#
# # string depends on the existence of name, age variables
# print(temp)

""" string operations  -->"""
"1- convert string to capital letters "
# name ='ahmed'
# print(name.upper())
# print(name.lower())
# message = 'hello world'
# print(message.capitalize())
# print(message.title())

"""examine string content """
# print(message.islower())
# print(message.isupper())


## isdigit === isnumeric
# num = input("please enter number: ")
# print(num.isdigit())  # return true if string contains only numbers --> integer number
# if num.isdigit():
#     num = int(num)
#     print(num, type(num))
# else:
#     print("please provide valid number ")

### isspace
# message = input("please enter message: ")
# print(f"#{message}#")
# print(message.isspace()) # return true if the string consists only from spaces
# if message.isspace():
#     print("--- please enter valid message ---")

""" strip string """
# fname = input("please enter firstname")
# lname = input("please enter firstname")
# print(fname, lname)
# print(f"#{fname}{lname}#")
# # strip spaces from the beginning and the end of the string
# fname = fname.strip()
# lname = lname.strip()
### strip chars
# print(f"#{fname}{lname}#")
# strip spaces from the beginning and the end of the string
# fname = fname.strip("# ")  # strip any char passed here -->
# # strip from the beginning and the end of the string
# print(f"strip = {fname}")


# fname = fname.lstrip("# ")  # strip any char passed here -->
# # strip from the beginning of the string
# print(f"strip = {fname}")

# fname = fname.rstrip("# ")  # strip any char passed here -->
# # strip from the end of the string
# print(f"strip = {fname}")

""" string replace -"""
# message = 'My name is Noha, I love python much. o o o '  # o ==> @
# print(message.replace('o', '@'))
# print(message.replace('o', '@', 2)) # replace only the 2 first occurrences

""" check if char exists in the string """
""" in operator """
message = 'hello world'
print('a' in message)

""" loop over the string 

    for (char in mymessage):
        print(char)
"""

# for abbass in message:
#     print(f"{abbass}")

for char in message:
    print(f"char= {char}")

print('-------------------------')



# z = 4 + 5j # complex

# a, b, c, d = 10, 66.66, 76.3, 100.54
# print(round(b))
# print(round(c))
# print(min(a, b, c, d))
# print(max(a, b, c, d))


