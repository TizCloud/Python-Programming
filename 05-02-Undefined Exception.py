# Demo 05-02
try:
    myfile = open("mytextfile", "w")
    myfile.write("This is my file for Exception Handling Example.")
except:
    print("IO Error with File.")
else:
    print("Written the file successfully.")
    myfile.close()

    
