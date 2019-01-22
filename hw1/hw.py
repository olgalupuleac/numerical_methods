import matplotlib.pyplot as plt
import numpy as np


def A(z):
    return 1 / np.sqrt(1 + 4 * z)


def x1(z):
    return (1 + np.sqrt(1 + 4 * z)) / 2


def x2(z):
    return (1 - np.sqrt(1 + 4 * z)) / 2


eps = 1e-6


def is_valid(n, z):
    return n ** 2 - n - z > 0 and abs(A(z) * np.log((n - x1(z)) / (n - x2(z)))) < eps


def binary_search(left, right, z):
    while right - left > 1:
        m = (right + left) // 2
        if is_valid(m, z):
            right = m
        else:
            left = m
    return right


def N(z):
    n = int(2 * z) + 1
    while not is_valid(n, z):
        n *= 2
    return binary_search(1, n, z)


def sum_member(k, z):
    return 1 / (k ** 2 - k - z)


def w(z):
    n = N(z)
    res = 0
    for k in range(1, n):
        res += sum_member(k, z)
    return res

print(np.log((2 - x1(1)) / (2 - x2(1))))

t = np.arange(start=0.01, stop=1.99, step=0.01)
s = [w(ti) for ti in t]

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='z', ylabel='wA(z)',
       title='Первая часть первого задания')
ax.grid()

fig.savefig("plot1.png")
plt.show()


