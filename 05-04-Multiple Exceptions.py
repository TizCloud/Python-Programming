# Demo 05-04
try:
    myfile = open("testfile2")
    myfile.write("This is my file for exception handling!!")
except(IOError, ValueError, SystemError):
    print("Error: can not find file or read data.")
else:
    print("Written file successfully")
    myfile.close()


