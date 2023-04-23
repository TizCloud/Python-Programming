# Demo 05-03
try:
    myfile = open('integers.txt')
    mystream = myfile.readline()
    i = int(mystream.strip())
except IOError:
    print("I/O Error.")
except ValueError:
    print("No valid integer.")
except:
    print("Unexpected error.")