# Demo 03-03-02
def changelist(mylist):
    mylist[2] = 40
    print("Values inside the function : ", mylist)
    return

mylist = [10,20,30]
changelist(mylist)
print ("Values outside the function : ", mylist)