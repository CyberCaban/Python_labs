import os
from pprint import pprint

path = input("Enter directory paht: ")
if not os.path.isdir(path):
    exit("Not valid path")

ext = input("enter extension: ")
if not ext.startswith("."):
    exit("Not a valid extension")

for curr_dir, _, files in os.walk(path):
    for file in files:
        file_path = os.path.join(curr_dir, file)
        if os.path.splitext(file_path)[1] == ext:
            pprint(file_path)