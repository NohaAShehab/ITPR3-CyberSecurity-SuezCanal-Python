"""# any variable defined in the python script can be accessed anywhere in the script """
# course = 'python'  # global variable
# print(course)
# course = 'Abc'
# print(course)

""" any variable defined inside a function ? can be accessed only inside the function ? """


# def askfornames():
#     # firstname --> can be accessed only inside the function
#     ## local variable
#     firstname = input("please enter firstname: ")
#     print(f"From inside the function firstname ={firstname}")
#
# askfornames()
# print(firstname)  # run time error


""" =======> global variable and function <========== """

# course= 'Python'
# ### you access the global variable value from inside the function
# def printcourseValue():
#     print(f"from inside the function --> {course}")
#
# printcourseValue()


""" ---- modify global variable from inside the function -----"""
# course= 'Python'
# ### you access the global variable value from inside the function
# def modifycourseValue():
#     global course
#     course = 'CCNA'
#     print(f"from inside the function --> {course}")
#
# modifycourseValue()
# print(course)


""" ====>example <==========="""

# no_of_connections = 0
# def connect_to_server():
#     global no_of_connections
#     print("===connect to server ====")
#     no_of_connections +=1
#     print(no_of_connections)
#
# connect_to_server()
# connect_to_server()
# connect_to_server()

""" ====> function inside a function <============== """


# def outerfunction():
#
#     course = 'Python'
#
#     def innerfunction():
#         print(f"from inside the inner function")
#
#     innerfunction()
#
#
#     print(f"from inside the outer function ---> {course}")
#
# outerfunction()




# def outerfunction():
#     course = 'Python'  # local variable for the outer function
#
#     def print_course_inner():  # this is the inner function
#         stdname = 'OMAR'  # new local variable from the print_course_inner function
#         print(f"from inside the inner function {course}, {stdname}")
#
#
#     print_course_inner()
#     print(f"from inside the outer function ---> {course}")
#     # print(stdname)
#
# outerfunction()


""" =====================inner function and global variable ========================="""
# course = 'Python'  # global variable
# def outerfunction():
#     def print_course_inner():  # this is the inner function
#         stdname = 'OMAR'  # new local variable from the print_course_inner function
#         print(f"from inside the inner function {course}, {stdname}")
#     print_course_inner()
#     print(f"from inside the outer function ---> {course}")
#
# outerfunction()

""" modify global variable from inner function """

# course = 'Python'  # global variable
# def outerfunction():
#     def print_course_inner():  # this is the inner function
#         global course
#         course = 'Network'
#         print(f"from inside the inner function {course}")
#     print_course_inner()
#     print(f"from inside the outer function ---> {course}")
#
# outerfunction()

""" ---> modify local variable from inner function """
# def outerfunction():
#     name = 'Ahmed'
#     def print_name_inner():  # this is the inner function
#         nonlocal name
#         name = 'Ali'
#         print(f"from inside the inner function {name}")
#     print_name_inner()
#     print(f"from inside the outer function ---> {name}")
#
# outerfunction()

####################################################3


# def outerfunction():
#     name = 'Ahmed'
#
#     def test():
#         def print_name_inner():  # this is the inner function
#             nonlocal name
#             name = 'Ali'
#             print(f"from inside the inner function {name}")
#         print_name_inner()
#     test()
#     print(f"from inside the outer function ---> {name}")
#
# outerfunction()


def connect_to_server():
    no_of_tests = 0
    def test_connection():
        nonlocal no_of_tests
        print("--- performing intial test ")
        no_of_tests +=1

    test_connection()
    test_connection()
    test_connection()
    test_connection()


    print(no_of_tests)


connect_to_server()






































