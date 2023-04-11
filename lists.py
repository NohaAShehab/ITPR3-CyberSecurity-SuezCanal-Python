"""

    list is the most versitle data structure in python
    list can hold different data from different datatypes
    --> list is mutable data type --> modify its content in the run
    --> list count its elements
    --> access its element using index  --> start from zero

"""

"""1- define a list """
l = []
myl = list([])

"""2-list can hold different data from different datatypes """
myl = ['Ahmed', 44, 435.545, True , ['python','ccna'], 'iti', 'iti']
print(myl)

"3-access its element using index  --> start from zero"
print(myl[2])
print(myl[4][1])
"4- get len of the list "
print(len(myl))
"5- count element occurrence in the list "
print(myl.count('iti'))
"6- get index of element in the list "
print(myl.index('iti')) # return index of the first occurence of the element
"""7- list is mutable datatype """
myl[3]= 'Python'
print(myl)
# myl[4][1]='CCNA'
myl[4][1]= myl[4][1].upper()
""" 8- append element to the list --> added to the end of the list """
myl.append('added element')
print(myl)
"""9-insert element at certain index """
myl.insert(2,'inserted value')
"10- pop element from the list"
print(myl)
popped_element = myl.pop()  # pop the last element in the list and return with it
print(myl)
print(popped_element)


""" 11- pop element at index"""
popped_element = myl.pop(4)
print(popped_element)
""" 12- remove element at index """
myl.remove('iti')  # remove first occurrence
print(myl)

"13- list concatenation "
l1 = [4,5,6,'34']
l2 = ['python', 'java', 'ccna']
l3= l1+l2
print(l3)
"""14- extend a list """
l1.extend(l2)
print(l1)
print(l2)

"""15 loop over the list"""
for element in l1:
    print(f"element= {element}")

""" 16- check existence of the element """
print('Ahmed' in l1)

""" 17 - sort a list ---> list elements must be from the same type """
# print('iti'>10) # '>' not supported between instances of 'str' and 'int'
# l = ['4545',34,345]
# l.sort()
names = ['mahmoud', 'mohamed', 'Mohamed', 'fathy','omar', 'Islam', 'somaya', 'nada']
names.sort() # sort list itself --> ascending
print(names) # names iii
# print(names.sort())
names.sort(reverse=True) # sort list itself --> desc
print(names)

"""18- reverse a list"""

myl =[4345,65,'Ahmed', True, ['iti', 'python']]

myl.reverse()

print(myl)

"""19- cast string to the list """
name = 'Ahmed'
name = list(name)
print(name)

'20- split string to a list '
message = 'I love python'
res = message.split(' ')
print(res)

"21- concate list of strings into a new string"


l= ['r', 'm', 'test', '98']

newstring ='||'.join(l)
print(newstring)

""" min , max"""
names = ['mahmoud', 'mohamed', 'Mohamed', 'fathy','omar', 'Islam', 'somaya', 'nada']

print(min(names))
print(max(names))