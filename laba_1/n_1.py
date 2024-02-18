words = input("Введите 10 слов: ").split(";")
ctrl = input("Введите контрольное слово: ")

if len(words) != 10:
    print("Нужно ввести 10 слов!!!")
    exit()

res = list(filter(lambda word: word.startswith(ctrl), words))
print(res)