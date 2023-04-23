# Demo 03-09

myfunc1 = lambda mynum1 : mynum1 + 50
print(myfunc1(100))
print('-------------------------------')

myfunc2 = lambda mynum1, mynum2 : mynum1 * mynum2
print(myfunc2(10, 5))
print('-------------------------------')

def myfunc3(n):
  return lambda mynum3 : mynum3 * n

mydouble = myfunc3(2)
print(mydouble(10))


