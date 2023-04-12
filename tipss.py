

# myrange = range(1, 10,2) # range object  --> 0 to 9
# nums = list(myrange)
# print(nums)
#
# myrange = range(100,10,-2) # range object  --> 0 to 9
# nums = list(myrange)
# print(nums)

""" for loop ---> known number of iterations  """
# for i in range(10):
#     print(i)

""" while loop ---> unknown number of itertion """

# while True:
#     num = input("please enter num ")
#     if num.isdigit():
#         print(int(num))
#         break
#     print("====== please enter valid number ======")

"""
    while (condition statisfied):
        do something 

"""


# names= []
# counter = 0
# while counter < 5:
#     stdname =input(f"please enter name of student {counter+1}")
#     names.append(stdname)
#     counter +=1
#
# print(names)
#

### break keyword - -> stop loop --> while loop , for loop
## break the loop

# for i in range(10):
#     if i ==4:
#         break
#     print(i)



""" ask user to enter password 3 times  ---> block account """

# for i in range(3):
#     password = input("please enter password: ")
#     if password=='123':
#         break  # break ---> while executing the last iteration
#     print("---invalid password please enter it again ")
#
# print(i)
#
# if i==2:
#     print("---- your account been blocked")
# else:
#     print("------ password correct ")


################ for - else block

# for i in range(3):
#     password = input("please enter password: ")
#     if password=='123':
#         print("=== password correct =====")
#         break  # break ---> while executing the last iteration
#     print("---invalid password please enter it again ")
#
# else:
#     "this block will be executed only if the loop wasn't broken"
#     print("---- your account been blocked")

###################################################

# for i in range(5):
#     print(f'i= {i}')
#
# print("---------- loop reached the end")

# for i in range(5):
#     if i==3:
#         break
#     print(f'i= {i}')
#
# print("---------- loop reached the end")


# for i in range(5):
#     # if i==3:
#     #     break
#     print(f'i= {i}')
# else:
#     print("---------- loop reached the end-------")

""" continue """
# for i in range(10):
#     if i==9:
#         continue  # skip to the next iteration
#     print(f'i= {i}')
# else:
#     print("---------- loop reached the end-------")
#
# print("-------------")
#

"""pass keyword"""
"""
    # if(name=='Ahmed'):
    #     print("hi")
    if(name=='Ahmed'):
    print("==========")

"""
name = 'test'
if(name=='Ahmed'):
    pass  # null
print("==========")


"""
    if(name=='Ahmed'){
    }
"""

if name=='ahmed':
    pass  # represent null operation --> used when a statement is required syntactically


print("-------------------")








""" pass keyword """
































