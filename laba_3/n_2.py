import os

path = input("Enter directory paht: ")
if not os.path.isfile(path):
    print("Not valid path")
    exit()

print(os.path.getsize(path))