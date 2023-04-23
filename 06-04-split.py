# Demo 06-04
FilePath = "C:\Python Programming\README.txt"
wordTemp = []
wordCount = 0
file = open(FilePath, 'r')

for line in file:
    for word in line.split():
        wordTemp.append(word)
        wordCount = wordCount + 1

print(wordTemp)
print(wordCount)

