import os
import collections

def is_file_exist(f_path):
    if not os.path.isfile(f_path):
        print(f"File {f_path} not found")
        exit()
    
file_path = input("Enter path: ")
is_file_exist(file_path)

lines = []
with open(file_path, "r", encoding="UTF-8") as f:
    lines = f.readlines()

coll = collections.Counter()
lines = list(map(lambda x: x.lower(), lines))
for line in lines:
    for letter in line:
        if letter == "\n" or letter == " ":
            continue
        coll[letter] += 1

is_file_exist("res.txt")
with open("res.txt", "w", encoding="UTF-8") as f:
    for key in dict(coll):
        f.write(f"{key}: {coll[key]}\n")
        