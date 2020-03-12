from __future__ import division

import matplotlib.pyplot as plt


def init():
    plt.clf()
    plt.axhline(y=0, color='r', linestyle='-')
    plt.axvline(x=0, color='r', linestyle='-')
    plt.axis([-4, 4, -4, 4])


def derive(f, a, h=0.00000001):
    return (f(a + h) - f(a)) / h


def graph(f, a, b, n):
    list_point = []
    h = (b - a) / n
    x = a
    for t in range(0, n + 1):
        y = f(x)
        list_point.append([x, y])
        x += h
    return list_point


def show_dots(list_points):
    for point in list_points:
        plt.scatter(point[0], point[1], s=30)


def draw_graph(f, a, b):
    point = graph(f, a, b, 100)
    i = 0
    while i < len(point):
        plt.scatter(point[i][0], point[i][1], s=10)
        if i > 0:
            plt.plot([point[i - 1][0], point[i][0]], [point[i - 1][1], point[i][1]], color='red')
        i += 1


def tracer_tangeante(f, a):
    x = a;
    y = f(a)
    dx = 1;
    dy = derive(f, a)
    plt.scatter(x, y, color="black", s=20)
    plt.plot([x, x + dx], [y, y + dy], color="black")
    plt.plot([x, x - dx], [y, y - dy], color="black")


def int_len(a):
    i = 0
    for char in str(a):
        i += 1
    return i


def dichotomie(f, a, b, incertitude):
    while int_len(a) <= incertitude or int_len(b) <= incertitude:
        milieu = (a + b) / 2
        if f(milieu) >= 0:
            b = milieu
        else:
            a = milieu
        print(a, b)
    return [round(a, incertitude), round(b, incertitude)]


def newton(f, a, n):
    for i in range(n):
        a = a - (f(a) / derive(f, a))
        print(a)
    return a


# f = lambda x: x ** 2 - 3
# init()
# draw_graph(f, -20, 20)
# print(newton(f, 2, 5))
# print(dichotomie(f, 1, 3, 5))
# plt.show()
