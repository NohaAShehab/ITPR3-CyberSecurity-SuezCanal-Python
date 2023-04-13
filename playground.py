# def askforInt(message):
#     while True:
#         userinput= input(message)
#         if userinput.isdigit():
#             return int(userinput)
#
#         print("please try again enter valid number:")
#
#
# def calculator():
#     num1 = askforInt("please enter num1: ")
#     num2 = askforInt("please enter num2: ")
#     res = num1 + num2
#     print(res)
#
# calculator()

""" import function from another python file  --> .py --

    .py file ---> python module
"""
""" import module """
# import inputsmodule  # all module parts are imported in your module
#
# def calculator():
#     """ modulename.function_name"""
#     num1 = inputsmodule.askforInt("please enter num1: ")
#     num2 = inputsmodule.askforInt("please enter num2: ")
#     res = num1 + num2
#     print(res)
#
# calculator()
#
# myname= inputsmodule.askforStr("please enter name ")
# print(myname)
# import inputsmodule
""" import part of the module """
# from inputsmodule import askforInt, name
# print(name)
# name = 'noha'
#
# def calculator():
#     """ modulename.function_name"""
#     num1 = askforInt("please enter num1: ")
#     num2 = askforInt("please enter num2: ")
#     res = num1 + num2
#     print(res)
#
# calculator()
#
#
#
#




""" alias module name , import """

# import inputsmodule as myinputs
#
# print(myinputs.askforStr('please enter first name '))


# from inputsmodule import askforInt as askforage
#
# print(askforage("please enter age: "))

""" package ??---> package is a directory """
""" import packagename.modulename """
# import cybersecurity.connection  # import module
# cybersecurity.connection.connect_to_server()

""" import part of the module"""
# from cybersecurity.connection import connect_to_server
#
# connect_to_server()

import cybersecurity.connection as conn

conn.connect_to_server()


# import os
# os.chdir('/home/noha/PycharmProject/cybersecuritySuez/day03')
# print(os.getcwd())
# print(os.system('ls'))
# print(__name__)
# print(__file__)
# from functions_ import introduceyourself
# introduceyourself(name='noha')

#
# from day03.functions_ import introduceyourself
#
# introduceyourself(name='nasnd')