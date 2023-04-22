# Demo 02-19

mylst = [i*1 for i in range(10)]

print("List Member: ",mylst)
print('--------------------------------------')

del mylst[0], mylst[2], mylst[4]
print("List After Remove Member: ",mylst)
print('--------------------------------------')

del mylst
print("List After Remove Member: ",mylst)

