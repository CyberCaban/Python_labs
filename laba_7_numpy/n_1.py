
import numpy as np
import numpy.random as random

try:
    n = int(input("Enter n: "))
    op = input("Enter operation(>, <, ==): ")
    
    if op != ">" and op != "<" and op != "==":
        exit("Unknown operation")
except ValueError:
    exit("Нужно ввести ЧИСЛО!!!")

a = np.matrix(random.randint(1, 100, (n, n)))
b = np.matrix(random.randint(1, 100, (n, n)))

print("a = \n", a)
print("b = \n", b)

c = eval("a" + op + "b")
print("c = a " + op + " b\n", c)