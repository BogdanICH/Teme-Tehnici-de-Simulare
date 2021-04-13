import numpy as np
import math

# TS
#Tema 2 - Iordache Bogdan Mihai

#cerinta 1

"""
U = np.random.uniform(0, 1)
Y = np.random.exponential(1)

cal = pow(math.pi, -(Y*Y)/2 + Y - 0.5)

while not(U <= cal):
    U = np.random.uniform(0, 1)
    Y = np.random.exponential(1)

X1 = Y
U = np.random.uniform(0, 1)

if U <= 0.5:
    s = 1
else:
    s = -1

X = s*X1

#Y = m + sigma * X
calculez = 4 + 7 * X
print("N(4, 7) = ", calculez)
"""
#cerinta 2

A = int(input("Numărul de bile albe = "))
B = int(input("Numărul de bile negre = "))
N = A + B
n = int(input("n = "))
while (n >= N):
    print("n trebuie să fie mai mic decât", N)
    n = int(input("n = "))
p = A/N
j = 0
X = 0

while j != n:
    U = np.random.uniform(0, 1)
    if U < p:
        X = X + 1
        S = 1
    else:
        S = 0
    N = N - 1
    A = A - S
    if N != 0:
        p = A/N
    j = j + 1

print("Numărul de bile albe extrase: ", X)



