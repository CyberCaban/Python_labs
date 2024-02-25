import os
from pprint import pprint

path = input("Enter directory paht: ")
if not os.path.isdir(path):
    print("Not valid path")
    exit()

ext = input("enter extension: ")
if not ext.startswith("."):
    print("Not a valid extension")
    exit()

for curr_dir, dirs, files in os.walk(path):
    for file in files:
        file_path = os.path.join(curr_dir, file)
        if os.path.splitext(file_path)[1] == ext:
            pprint(file_path)