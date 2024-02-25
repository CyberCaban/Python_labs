import os
from operator import itemgetter

file_path = input("Введите путь до файла: ")

try:
    with open(file_path, "r", encoding="UTF-8") as f:
        lines = f.readlines()
except FileNotFoundError:
    exit("file not found")

lines = list(map(lambda x: " ".join(x.split()).split(" "), lines))
names = sorted(lines)
pts = sorted(lines, key=itemgetter(1))

print(f"Сортировка по именам: {names}")
print(f"Сортировка по баллам: {pts}")

try:
    inp = int(input("Введите балл: "))
except ValueError:
    print("Введите ЧИСЛОО!!!")
    exit()

filtered_by_user = list(map(lambda x: f"{x[0]}\n" if int(x[1]) > inp else "", lines)) 
try:
    with open("res.txt", "w", encoding="UTF-8") as f:
        f.writelines([f"Участники, балл которых выше {inp}\n", *filtered_by_user])
except FileNotFoundError:
    exit("file not found")