from __future__ import division

from math import *

nb = 2 ** 63
# print("il faudrai {} grains de riz".format(nb))
tonne = (nb / 50000) * 10 ** -3
# print("Ce qui correspond a {}tonnes".format(tonne))
euro = (2 ** 30) * 10 ** -2
# print("Alors, un milion maintenant ou {} euros a la fin du mois ?".format(euro))

S0 = 100 / 1.5 ** 10


def surface_nenuphar(x):
    return S0 * exp(log(1.5) * x)


def jour_nenuphar(S):
    n = log(S / S0) / log(1.5)
    return n


T = 5370


def carbn14(t, N0=1000, T=5730):
    return N0 * exp(-(t * log(2)) / T)


# print(carbn14(10*T))

def datation14(N, N0=1000, T=5730):
    return -T / log(2) * log(N / N0)


# print(datation14(200))

k = (-1 / 10) * log(40 / 75)


def temperature(t):
    return (100 - 25) * exp(-k * t) + 25


# print(temperature(42))

def my_exp(x, n):
    return (1 + (x / n)) ** n


# print(my_exp(2.8,10))
# print(my_exp(2.8,100))
# print(my_exp(2.8,1000))
# print(my_exp(2.8,10000))
# print(exp(2.8))

def factorielle(x):
    fact = 1
    compteur = 0
    for i in range(1, x + 1):
        fact *= i
        compteur += 1
    return [fact, compteur]


# print(factorielle(1),factorielle(10))

def somme_exp(x, n):
    somme = 0
    compteur = 0
    for k in range(0, n + 1):
        somme += (x ** k) / factorielle(k)[0]
        compteur += k + factorielle(k)[1]

    print("Il y a eu {}".format(compteur))
    return somme


# print(somme_exp(2.8,100))

def expo_honrer(x, n):
    s = 0
    while n > 0:
        s = (x / n) * s + 1
        n -= 1
    return s


# print(expo_honrer(2.8,1000

def expo_euler(x, n):
    S = 0
    for k in reversed(range(1, n)):
        S = x / (k + x - k * S)
    S = 1 / (1 - S)
    return S


def expo_astuce(x, n):
    e1 = expo_honrer(1, n)
    k = floor(x)
    f = x - k
    fexp = expo_honrer(f, n)
    kexp = e1 ** k
    return fexp * kexp