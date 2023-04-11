"""

    tuple is the most versitle data structure in python
    tuple can hold different data from different datatypes
    --> tuple is immutable data type --> once created cannot be changed
    --> tuple count its elements
    --> access its element using index  --> start from zero

"""

"""1- define a tuple """
t = ()
myt = tuple([])

"""2-tuple can hold different data from different datatypes """
myt = ('Ahmed', 44, 435.545, True , ['python','ccna'], 'iti', 'iti')
print(myt)
#
"3-access its element using index  --> start from zero"
print(myt[2])
print(myt[4][1])
"4- get len of the tuple "
print(len(myt))
"5- count element occurrence in the tuple "
print(myt.count('iti'))
"6- get index of element in the tuple "
print(myt.index('iti')) # return index of the first occurence of the element






"13- tuple concatenation "
t1 = (4,5,6,'34')
# t2 = ('python', 'java', 'ccna')
# t3= t1+t2
# print(t3)

"""15 loop over the tuple"""
for element in t1:
    print(f"element= {element}")

""" 16- check existence of the element """
print('Ahmed' in t1)

"""19- cast string to the tuple """
name = 'Ahmed'
name = tuple(name)
print(name)



#
""" min , max"""
names = ('mahmoud', 'mohamed', 'Mohamed', 'fathy','omar', 'Islam', 'somaya', 'nada')

print(min(names))
print(max(names))

"cast list to tuple ?"
l = [34,4,4,True]
myt = tuple(l)  # return new tuple ?
print(myt)

name = tuple("ahmed")
print(name)
name = list(name)
print(name)

mytt = ("noha",)
print(mytt, type(mytt))

############# range ##########
" generate list or tuple of number "
r = range(0,10)  # generate numbers from start to end-1
for i in r:
    print(f'i = {i}')

"    noha - -> nh ===> iti ---> 0 , 2 " \
"" \
"1 , 2 , 3" \
"3 , [[1], [2,4], [3,6,9]]"
# print(r)
#
# r = list(r)
# print(r)