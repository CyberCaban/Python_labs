import numpy as np

MIN_EL = 0
MAX_EL = 4

try:
    n = int(input("Enter n: "))
except ValueError:
    exit("Нужно ввести ЧИСЛО!!!")

a = np.matrix(np.random.randint(MIN_EL, MAX_EL, (n, n)))

b = np.sum(a, axis=0)
c = np.where(b == np.amin(b))[1][0]
print("a = \n", a)
print("b = \n", b)
print("c =", c + 1)
