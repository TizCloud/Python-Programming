# Demo 03-04
def changelist(mylist):
    mylist = [40,50, 60, 70]  # Assign new reference in mylist
    print("Values inside the function : ", mylist)
    return

mylist = [10,20,30]
changelist(mylist)
print ("Values outside the function : ", mylist)

