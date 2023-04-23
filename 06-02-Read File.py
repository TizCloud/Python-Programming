#Demo 06-02
FilePath = "C:\Python Programming\README.txt"
try:
    f = open(FilePath)
    str = f.read()
    print(str)
    print("********************************************")

    f = open(FilePath)
    str = f.readlines(15)
    print(str)
    print("********************************************")

    f = open(FilePath)
    while 1:
        line = f.readline()
        if len(line):
            print(line)
        else:
            break
except IOError as err:
    print("Cann't open file because :",err.args)
else:
    print("********************************************")
    print("This file was closed!")
    f.close()

