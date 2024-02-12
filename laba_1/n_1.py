words = input("Введите 10 слов: ").split(";")
ctrl = input("Введите контрольное слово: ")

if len(words) != 10:
    print("Нужно ввести 10 слов!!!")
    exit()

res = list(map(lambda word: (word) if word.startswith(ctrl) else None, words))
res = list(filter(lambda x: x != None, res))
print(res)