# Demo 02-30

mydict = {'Name': 'James Wilson', 'Age': 35, 'Class': 'First'}
print("Original Dictionary :",mydict)

del mydict['Class'] # delete member dictionary
print("After removed :",mydict)

mydict.clear() # remove all entries in dictionary
print("After cleared all member :",mydict)

del mydict     # delete entire dictionary
print("After deleted form memory :",mydict)

