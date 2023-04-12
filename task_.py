
# """ ---> multiplication table ?
#  input 3
# output  [  [1],[2,4], [3,6,9]  ]
# num *1 ----> up to num * num
# """
""
# num = input("please enter number: ")
# if num.isdigit():
#     num = int(num)
#     print(num, type(num))
#     multiplication_table = []
#     for i in range(1, num+1):
#         print(i)
#         sublist = []
#         # sublist.append(i)
#         for numm in range(1, i+1):
#             sublist.append(numm*i)
#         multiplication_table.append(sublist)
#
#     print(multiplication_table)
# else:
#     print("please enter valid number ")
#
"""
    Mario
      *
     **
    ***
   ****


"""

dim = input("please enter number ")
if dim.isdigit():
    dim = int(dim)
    for i in range(dim+1):
        # print("*")
        no_of_spaces = dim- i
        print((' '*no_of_spaces)+('*'*i))


print("----------------------")



