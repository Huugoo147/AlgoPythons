from __future__ import division

from math import *


def derive(f, a, h=0.00000001):
    return (f(a + h) - f(a)) / h


def verif_primitive(f, F, a, b, n, epsilon):
    for k in range(0, n + 1):
        xk = a + k * ((b - a) / n)
        derive_xk = derive(F, xk)
        print(xk, derive_xk)
        if abs(derive_xk - f(xk)) <= epsilon:
            continue
        else:
            return False
    return True


f = lambda x: x ** 2
F = lambda x: (1 / 3) * x ** 3


# print(verif_primitive(f,F,5,9,10,0.0001))

def integrale(F, a, b):
    return F(b) - F(a)


# print(integrale(F,1,2))
# print(integrale(lambda x : -cos(x),0,pi))

def integrale_rectangle(f, a, b, n):
    h = (b - a) / n
    x = a
    integrale_returned = 0
    for k in range(0, n):
        integrale_returned += h * f(a)
        a += h
    return integrale_returned


# print(integrale_rectangle(f,1,2,100))

def integrale_trapeze(f, a, b, n):
    h = ((b - a)) / n
    x = a;
    sum = 0
    for k in range(n):
        sum += (f(a) + f(a + h)) / 2 * h
        a += h
    return sum


# print(integrale_trapeze(f,1,2,100))
# print(4*integrale_trapeze(lambda x : (1-x**2)**0.5,0,1,30))

def integrale_simpson(f, a, b, n):
    h = (b - a) / n
    x = a
    integrale = 0
    for i in range(n):
        integrale = integrale + (f(a) + 4 * f(a + h / 2) + f(a + h)) / 6 * h
        a = a + h
    return integrale


# print(integrale_simpson(f,1,2,100))

def integrale_Gauss1():
    N = 25
    return integrale_trapeze(lambda x: exp(-x ** 2), -N, N, N ** 2)


# print(integrale_Gauss1(), pi**0.5)

def integrale_Gauss2(x):
    N = 30
    return integrale_trapeze(lambda x: exp(-x ** 2), -N, x, N ** 2)


# print(integrale_Gauss2(10))

def normale_gauss(x, mu, sigma2):
    P = lambda x: 1 / sqrt(2 * pi * sigma2) * exp(-1 / 2 * (x - mu) ** 2 / sigma2)
    infini = 20 * sqrt(sigma2)
    p = integrale_simpson(P, -infini, x, 100)
    return p


print(normale_gauss(4, 4, 1))
qi = 1 - normale_gauss(115, 100, 225)
print("Pourcentage de population QI > 115 : {}".format(qi))
