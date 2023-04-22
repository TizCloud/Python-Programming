# Demo 03-03
def changelist(mylist):
    mylist.append([100, 200, 300, 400, 500])
    print("Values inside the function : ", mylist)
    return

mylist = [10,20,30]
changelist(mylist)
print ("Values outside the function : ", mylist)



