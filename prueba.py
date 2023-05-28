import numpy as np

alpha = np.sqrt(1239049)


def f(x):
    return np.sqrt(x**2 + 1) - 1


print(f(alpha))
print(round(alpha, 5))
