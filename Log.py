from __future__ import division

from math import *

import matplotlib.pyplot as plt


def init():
    plt.clf()
    plt.axhline(y=0, color='r', linestyle='-')
    plt.axvline(x=0, color='r', linestyle='-')
    plt.grid()
    plt.axes().set_aspect('equal')


init()


def magnitude(E):
    return (2 / 3) * log(E / (1.6 * 10 ** -5), 10) - 3.2


# E = 10
# i = 1
# while magnitude(E) < 7 :
# E *= 10
# i+=1

def decibels(P):
    return 20 * log(P / (2 * 10 ** -5), 10)


#
# print(decibels(632))
# print(decibels(2))
# print(decibels(0.355))
# print(decibels(0.07))
# print("De {} a {}".format(decibels(0.002),decibels(0.02)))
# print(decibels(0.00007))
# print(decibels(2*10**-5))
# print(decibels(6*10**-6))

def afficher_pointsxy(liste_points):
    for x, y in liste_points:
        plt.scatter(x, y, color="red", s=10)


def afficher_pointsxlogy(liste_points):
    for x, logy in liste_points:
        plt.scatter(x, log(logy, 10), color="green", s=10)


def afficher_pointslogxlogy(liste_points):
    for logx, logy in liste_points:
        plt.scatter(log(logx, 10), log(logy, 10), color="blue", s=10)


jeux1 = [[2, 5.66], [3, 10.39], [5, 22.36], [7, 37.04], [11, 72.97]]
jeux2 = [[2, 5], [3, 6.5], [5, 9.5], [7, 12.5], [11, 18.5]]
jeux3 = [[2, 5.01], [3, 6.31], [5, 10], [7, 15.84], [11, 39.81]]

afficher_pointsxy(jeux2)
afficher_pointsxlogy(jeux3)
afficher_pointslogxlogy(jeux1)
plt.show()


def test_propritetes_ln(a=2, b=3, n=7):
    print("ln(a*b) = {}, or ln(a) = {} et ln(b) = {}, donc ln(a)+ln(b) = {}".format(log(a * b), log(a), log(b),
                                                                                    log(a) + log(b)))
    print("ln(a/b) = {}, or ln(a) = {} et ln(b) = {}, donc ln(a)-ln(b) = {}".format(log(a / b), log(a), log(b),
                                                                                    log(a) - log(b)))
    print("ln(a**0.5) = {}, or (1/2)*ln(a) = {}".format(log(a ** 0.5), (1 / 2) * log(a)))
    print("ln(1/a) = {}, or -ln(a) = {}".format(log(1 / a), -log(a)))
    print("ln(a**n) = {}, or n.ln(a) = {}".format(log(a ** n), n * log(a)))


# test_propritetes_ln()
# print("\n\n\n\n")
# test_propritetes_ln(3/2,1/3,pi)

def table_ln(x, N):
    x = log(x)
    x = x * 10 ** N
    x = floor(x)
    x = x * 10 ** -N
    return x


def table_exp(x, N):
    x = exp(x)
    x = x * 10 ** N
    x = floor(x)
    x = x * 10 ** -N
    return x


def multiplication(a, b, N=1):
    y = table_ln(a, N) + table_ln(b, N)
    return table_exp(y, N)


# print(multiplication(98.765,43.201,4))

def k_base10(x):
    y = 10;
    k = 0
    while y < x:
        y *= 10;
        k += 1
    return (k)


# print(k_base10(1000),log(1000,10))

def k_base2(x):
    y = 2;
    k = 0
    while y < x:
        y *= 2;
        k += 1
    return k


# print(k_base2(666),log(666,2))
def dichotomie(n):
    counter = 0
    while n > 1:
        n = max(n // 2, n - n // 2)
        counter = counter + 1
    return counter


# print(dichotomie(1000),log(1000,2))

def log_base(x, b):
    return log(x) / log(b)


# print(log_base(1,e),log(1,e))

def nombre_chiffre(x, b):
    k = floor(log_base(x, b)) + 1
    return k


# print(nombre_chiffre(123,2))

def log_serie1(x, N):
    u = x - 1;
    somme = 0
    for i in range(1, N):
        if i % 2 == 0:
            somme -= (u ** i) / i
        else:
            somme += (u ** i) / i
    return somme


# print(log_serie1(10,100),(log(10)))

def log_serie2(x, N):
    u = (x - 1) / (x + 1);
    somme = 0
    for i in range(1, N, 2):
        somme += 2 * (u ** i) / i
    return somme


# print(log_serie2(10,100))

def reduction_intervalle_e(x):
    k = 0
    while x > 1.5:
        x /= e
        k += 1
    while x < 0.5:
        x *= e
        k -= 1
    return [x, k]


def log_serie3(x, N):
    new_x, k = reduction_intervalle_e(x)
    return log_serie2(new_x, N) + k


# print(log_serie3(154.433,10),log(154.433))

def log_inverse(x, N):
    if x <= 0:
        return None
    u = 1
    for i in range(N):
        u -= (exp(u) - x) / exp(u)
    return u


# print(log_inverse(2*e,100))

def reduction_intervalle_10(x):
    k = 0
    while x > 10:
        x /= 10
        k += 1
    return [x, k]


def log_Cordic(x, N):
    if x <= 0:
        return None
    y, k = reduction_intervalle_10(x)
    p = log(10)
    for i in range(N - 1):
        q = 1 + 10 ** -i
        while q * y <= 10:
            y = q * y
            p = p - log(q)
    return p + k * log(10)


# print(log_Cordic(10,1),log(10))

def briggs(x, Epsilon):
    n = 0
    while abs(x - 1) > 10 ** Epsilon:
        x = x ** 0.5
        n += 1
    l = x - 1
    for i in range(0, n):
        l *= 2
    return l


print(briggs(10, -5), log(10))
