import matplotlib.pyplot as plt
import numpy as np

eps = 1e-6


def sum_member_A(k, z):
    return 1 / (k ** 2 - k - z)


def wA(z):
    n = int(1 / eps) + 1
    return sum(map(lambda k : sum_member_A(k, z), range(1, n)))




def sum_member_B(k, z):
    return z / ((k ** 2 - k - z) * k * (k - 1))


def wB(z):
    n = int((z / (3 * eps)) ** (1 / 3)) + 2
    return sum(map(lambda k: sum_member_B(k, z), range(2, n))) + 1 - 1 / z


def plot(w, file_to_save, title=None, func_name=None):
    t = np.arange(start=0.01, stop=1.99, step=0.01)
    s = [w(ti) for ti in t]


    fig, ax = plt.subplots()
    ax.plot(t, s)

    ax.set(xlabel='z', ylabel=func_name,
           title=title)
    ax.grid()

    fig.savefig(file_to_save)
    plt.show()

#plot(wA, 'plot1.png', 'Первая часть первого задания', 'wA(z)')
#plot(wB, 'plot2.png', 'Вторая часть первого задания', 'wB(z)')
plot(lambda z : wA(z) - wB(z), 'plot3.png', 'Третья часть первого задания', 'wA(z) - wB(z)')