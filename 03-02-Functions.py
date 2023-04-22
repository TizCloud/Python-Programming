# Demo 03-02
def sumnum(begin, end):
    sum = 0
    for i in range(begin, end + 1):
        sum += i

    print(f'Result of {begin}..{end} = {sum}')

sumnum(1, 10)
sumnum(10, 20)

