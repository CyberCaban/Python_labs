import collections
file_path = input("Enter path: ")
lines = []
try:
    with open(file_path, "r", encoding="UTF-8") as f:
        lines = f.readlines()
except FileNotFoundError:
    exit("file not found")

coll = collections.Counter()
lines = list(map(lambda x: x.lower(), lines))
for line in lines:
    for letter in line:
        if letter == "\n" or letter == " ":
            continue
        coll[letter] += 1

try:
    with open("res.txt", "w", encoding="UTF-8") as f:
        for key in dict(coll):
            f.write(f"{key}: {coll[key]}\n")
except FileNotFoundError:
    exit("file not found")
        