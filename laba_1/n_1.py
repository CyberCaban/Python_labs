words = input("Введите 10 слов: ").split(";")
ctrl = input("Введите контрольное слово: ")

if len(words) != 10:
    print("Нужно ввести 10 слов!!!")
    exit()

if ctrl == "":
    exit("вы не ввели контрольное слово")

res = list(filter(lambda word: word.startswith(ctrl), words))

if len(res) == 0:
    exit("Программа не нашла слова c вашим конторльным словом")

print(res)