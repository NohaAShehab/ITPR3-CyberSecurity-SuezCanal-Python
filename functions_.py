"""
    built-in functions ?

    --> each function has a name
    --> function may accept arguments
    --> function may return with data

    function ---> block of code --> is written once, call many
    can accept data or return data or both
    you must define the function before calling it.

"""
# print("ahmed")
# mystring ='ahmed'.replace('a','@')  # replace accept arguments , return with result
# print(mystring)

""" define function """

# def sayhello():
#     pass
#
# res= sayhello()
# print(res)  # None ---> function by default 0--> unless you specify --> it will return None

# """ function do something """
# def sayhello():
#     print("---- Hello world  -------------")
#
# res= sayhello()
# print(res)  # None ---> function by default --> it will return None

# """ function accept arguments """
#
# def ask_for_fullname(firstname, lastname):
#     print(f"fullname={firstname} {lastname}")
#
# res = ask_for_fullname('Ahmed', 'Ali')
# print(res)  # None


""" function accept arguments  and return with result """

# def ask_for_fullname(firstname, lastname):
#     fullname = f"fullname={firstname} {lastname}"
#     print(fullname)
#     return fullname
#
# res = ask_for_fullname('Ahmed', 'Ali')
# print(res)  # None


# def calculator(num1, num2):
#     res = num1 + num2
#     print(f"from inside the function res = {res}")
#
#
# summnums = calculator(3,5)
# print(summnums)


""" """

# def calculator(num1, num2):
#     res = num1 + num2
#     print(f"from inside the function res = {res}")
#     return
#
#
# summnums = calculator(3,5)
# print(summnums)


""""""
# def calculator(num1, num2):
#     res = num1 + num2
#     print(f"from inside the function res = {res}")
#     return res
#
#
# summnums = calculator(3,5)
# print(summnums)


""" python loosely dynamically typed lang? python detect datatype of the variable
in the runtime ---> you can modify variable datatype
"""

# def sumnums (num1, num2):
#     print(f"num1= {num1}, num2={num2}")
#     res = num1 + num2
#     print(f'res = {res}')
#     return res
#
# x = sumnums(10,10)
# y = sumnums('34', '87')
# y = sumnums('iti', 'cyber security')
# # z= sumnums(23,'iti')  # unsupported operand type(s) for +: 'int' and 'str'
#
# print(y)


""" function with defined parameter type """

# def sumnums(num1: int, num2: int) -> object:    # type hints for documentary purpose
#     print(f"num1= {num1}, num2={num2}")
#     res = num1 + num2
#     print(f'res = {res}')
#     return res
#
#
# x = sumnums(10, 10)
# # y = sumnums('34', '87')
# y = sumnums('iti', 'cyber security')
# z= sumnums(23,'iti')  # unsupported operand type(s) for +: 'int' and 'str'

# print(y)

""" manually make sure the data type of variable statisfy the requirements """

# print(isinstance(10 , int))
# print(isinstance('Ahmed', int))
# print(isinstance('100', int))
######################################################3
print(isinstance(True, bool))
print(isinstance(3.14, float))


def mulnum(num1, num2):
    if isinstance(num1, int) and isinstance(num2, int):
        res = num1 * num2
        print(res)
        return res
    else:
        print("---- num1 , num2 must be integers ----")


# mulnum(3,5)
# r=mulnum(2,'iti')
# print(r)
# mm=mulnum('55','44')
# print(mm)


################################
"""
        isdigit works with string ? 
        isinstance(val, str) ---> True 
        val.isdigit()

"""
# def test(num):
#     if isinstance(num,int):
#         print(num)
#     elif isinstance(num,str ):
#         if num.isdigit():
#             print(f"num is numeric string {num}")
#
# test("10")

""" functions ------------------> with default arguments  --> """

""" at least you must pass one argument , 2 at most """
# def sumnum(num1, num2=10):  # num2 --> is optional, num1--> is mandatory
#     print(f"num1={num1},num2={num2} ")
#     print(num1 + num2)
#
#
# sumnum(4)
# sumnum(434, 6)
#
# print('Ahmed', 'Ali', sep='_____')
# print("Noha", end='#')
# print('Test', end=";")
# print("ITI", end='|')

##################################################

# def askfornames():
#     fname = input("please enter first name: ")
#     lname = input("please enter lastname: ")
#     fullname = f'{fname} {lname}'
#     return fullname, fname  # result in tuple ?
#
#
# res = askfornames()
# print(res)
#
#


""" function with unknown number of argument """

# print("Ahmed",4,54,6,45)
# print()

# * ---> represent zero or more
# def askforstudnets(*students):  # students --> variable number of arguments may be zero or more
#     print(students) # accept data tuple
#     print("-----------------------")
#
# askforstudnets('Ahmed', 'Ali')
# askforstudnets()
# askforstudnets("ahmed", 'Mohamed','test', 3234, 35,908)

#########################################################

""" function with variable number keyword arguments """


def introduceyourself(**info):  # ** -> unknow number of keyword arguments
    print(info)  # dictionary

introduceyourself(name='noha', work='iti', age=30)
# introduceyourself()
# introduceyourself(fname='Ali', lname='ahmed')
# introduceyourself("Ahmed", 'Ali')

# temp = "My name is {username}, I lives in {city}"
# print(temp.format(username='ahmed', city='Cairo'))


temp = "My name is {0}, I lives in {1}"
print(temp.format('ahmed', 'Cairo'))
