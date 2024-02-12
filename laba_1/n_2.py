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

inp = input("Введите число N: ")

try: 
    int(inp)
except ValueError:
    print("Нужно ввести ЧИСЛО!!!")
    exit()

print(mat_hypo(int(inp)))