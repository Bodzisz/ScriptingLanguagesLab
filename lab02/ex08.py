import os

def getFilePath():
    return input("Enter file path: ")


def writeLines(filepath):
    try:
        with open(filepath, 'w') as file:
                file.write(line1 + '\n')
                file.write(line2 +'\n')
                for word in lines:
                    file.write(word + " ")
                file.write('\n')
    except:
        writeLines(getFilePath())


line1 = "Kacper"
line2 = "Wojcicki"
lines = ["Lech", "Poznan", "Mistrz", "Polski"]
site = input("Enter your fav website: ")

filePath = getFilePath()

writeLines(filePath)

print("FILE CONTENT: ")
with open(filePath, 'r') as file: 
    for line in file:
        print(line)