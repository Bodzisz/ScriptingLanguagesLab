import time
import os


def printDate(date, additional=""):
    print(additional, date.tm_year, "/", date.tm_mon, "/",
          date.tm_wday, " ", date.tm_hour, ":", date.tm_min, ":",
          date.tm_sec)


dirPath = input("Insert path: ")
if not os.path.isdir(dirPath):
    print("path is not pointing to directory!")
else:
    fullPath = dirPath + "/" + input("Enter file name: ")
    lastMod = time.localtime(os.path.getmtime(fullPath))
    created = time.localtime(os.path.getctime(fullPath))
    access = time.localtime(os.path.getatime(fullPath))
    printDate(lastMod, "Last modified: ")
    printDate(created, "Created: ")
    printDate(access, "Last accessed: ")
    print("Size (bytes): ", os.path.getsize(fullPath))
