import os
from operator import itemgetter

if not os.path.isfile("input.txt"):
    print("Файла нетт!!!")
    exit()

lines = []
with open("input.txt", "r", encoding="UTF-8") as f:
    lines = f.readlines()

lines = list(map(lambda x: " ".join(x.split()).split(" "), lines))
names = sorted(lines)
pts = sorted(lines, key=itemgetter(1))

print(f"Сортировка по именам: {names}")
print(f"Сортировка по баллам: {pts}")

try:
    inp = int(input("Введите балл: "))
except:
    print("Введите ЧИСЛОО!!!")
    exit()

with open("res.txt", "w", encoding="UTF-8") as f:
    f.writelines((list(map(lambda x: f"{x[0]}\n" if int(x[1]) > inp else None, lines))))