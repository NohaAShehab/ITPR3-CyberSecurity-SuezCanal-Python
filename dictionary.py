"""



"""
#
# info = ['Noha', 'iti', 30 , 'reading']
# print(info)
""" datatype

    :keyword datatype ---> 
    --> dictionary ? 
    --> keyword: meaning 
    
    comma seperated key:value pairs 
"""

""" 1- define a dict """
d = {}
myd = dict([])
print(d)
print(myd)
""" 2- use keywords to present the data --
    unique keywords --> keywords --> hashable keywords ?
    
    dict --> mutable datatype 
"""

myinfo = {
    "name":'Noha',
    "work":"ITI",
    "age":30,
    "Hoppy": "reading",
    "name":"Noha Shehab"
}
print(myinfo)
""" 3- use keys to access dict items """
print(myinfo["name"])
myinfo["name"]="TEST"
print(myinfo)
myinfo["salary"]=10000  # if ket doesn't exists --> add new keyvalue pair at the end of the dict

"4- get len of the dict "
print(len(myinfo))

"5- pop element from the dict "
popped_element=myinfo.pop("Hoppy")
print(popped_element)

'6- loop over the dict elements '
# for item in myinfo:  # item-> key
#     print(f"item = {item}")

for item in myinfo:  # item-> key
    print(f"key={item} value={myinfo[item]}")


"7- check existence "
print('TEST' in myinfo)  # False ? why ?
# in operator check if the given element exists in the keys

""" 8- get keys """
keys = myinfo.keys()  # dict_keys(['name', 'work', 'age', 'salary'])
# print(keys[0]) # 'dict_keys' object is not subscriptable
keys_list = list(keys)
print(keys_list)

""" 8- get values """
values = myinfo.values()  # dict_keys(['name', 'work', 'age', 'salary'])
print(values) # 'dict_keys' object is not subscriptable
values_list = list(values)
print(values_list)


"""9- dictionary items """
items = myinfo.items()
print(items, type(items))
d_items = list(items)
print(d_items)

for key, value in myinfo.items():
    print(f"key={key}, value={value}")

"""10- update dict  """
myinfo = {
    "name":'Noha',
    "work":"ITI",
    "age":30,
    "Hoppy": "reading",
    "name":"Noha Shehab"
}

iti_instructor = {
    'name':"Noha Shehab",
    "course":[
        "Admin1",'shell scripting', 'python'
    ]
}

myinfo.update(iti_instructor)  # update existing dict
## if key doesn't exist --> add it , if key exists --> will update the value
print(myinfo)


"""clear dict ? """
# myinfo.clear()
# print(myinfo)

""" cast dict to a list"""
myinfo_list= list(myinfo)  # for loop , in operator
print(myinfo_list)

""" delete dict """