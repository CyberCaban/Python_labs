import os
from operator import itemgetter

def is_file_exist(f_path):
    if not os.path.isfile(f_path):
        print(f"Файла {f_path} нет")
        exit()

file_path = input("Введите путь до файла: ")
is_file_exist(file_path)

lines = []
with open(file_path, "r", encoding="UTF-8") as f:
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

is_file_exist("res.txt")

filtered_by_user = list(map(lambda x: f"{x[0]}\n" if int(x[1]) > inp else "", lines)) 
with open("res.txt", "w", encoding="UTF-8") as f:
    f.writelines([f"Участники, балл которых выше {inp}\n", *filtered_by_user])