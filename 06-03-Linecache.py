# Demo 06-03
import linecache

FilePath = "C:\Python Programming\README.txt"

for line in range(4):
    print(linecache.getline(FilePath, line))
linecache.clearcache()


