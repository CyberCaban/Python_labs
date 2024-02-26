from pprint import pprint


def mat_hypo(n):
    res = {"sequence": [], "seq_len": 0, "pique": n}
    while n != 1:
        res["sequence"].append(n)
        res["seq_len"] += 1
        if res["pique"] < n:
            res["pique"] = n
        if n % 2 == 0:
            n /= 2
        else:
            n = n * 3 + 1
    return res


try: 
    inp = int(input("Введите число N: "))
except ValueError:
    print("Нужно ввести ЧИСЛО!!!")
    exit()

if inp < 0:
    exit("Введите натуральное число!!!")

pprint(mat_hypo(inp))
