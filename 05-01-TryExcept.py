# Demo 05-01
try:
    myfile = open("mytextfile", "w")
    myfile.write("This is my file for Exception Handling Example.")
except IOError:
    print("Error - can not find file or read data.")
else:
    print("Written the file successfully.")
    myfile.close()


    