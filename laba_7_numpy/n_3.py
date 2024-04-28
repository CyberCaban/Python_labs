from io import TextIOWrapper
import numpy as np


def read_matrix(n: int, f: TextIOWrapper) -> np.matrix:
    try:
        res = np.matrix([list(map(float, f.readline().split())) for _ in range(n)])
    except ValueError:
        exit("линейное уравнение составлено неправильно")
    return res


nt = float
with open("n3_input.txt", "r") as f:
    try:
        n = int(f.readline())
        a = read_matrix(n, f)
        b = read_matrix(n, f)
    except ValueError:
        exit("линейное уравнение составлено неправильно")


print("a = \n", a)
print("b = \n", b)
try:
    x = np.linalg.solve(a, b)
except np.linalg.LinAlgError:
    exit("нет решения")
print("x = \n", x)
