"""
arthematic operators """

x = 10
y = 2
z = x ** y
print(z)

# x = x + 10
x += 10

""" comparison operators 

    > , < ---> compare data from the same type
"""

print('Ahmed' >  'Maham')


# compare strings A, m according the ascii code of each char

# print('19'> 223) #TypeError: '>' not supported between instances of 'str' and 'int'

# print('19' > '100')


#########################

# print(6 == '6')
# print(1 == True)
# print(True == ' ')
#################### represent true vs == true

""" and make sure that all the expression parts equal True or represent True."""
print(1 and 10 )  ### and

print(100 and 'noha')

x = '' and 'Ahmed' and True
print(x)  # empty string represent false

""" or --> make sure that at least one of the expression parts represent true """


print('Ahmed' or False )

print('' or 'noha' or 'iti' or True)

print(not "          ")

print(not '')

name =input("please enter name: ")  # ask user to enter element --> read in form of string
print(name, type(name))
if name =='ahmed':
    print("hi")
elif name =='Ali':
    print('welcome')
else:
    print("=== bye===")
