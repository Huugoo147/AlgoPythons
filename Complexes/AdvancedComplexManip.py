from __future__ import division
from math import *
from cmath import *


def polaire_to_cartesion(r, arg):
    return r * cos(arg) + 1j * r * sin(arg)


def cartesion_to_polaire(z):
    arg = atan2(z.imag, z.real)
    mod = sqrt(z.real ** 2 + z.imag ** 2)
    return [mod.real, arg]


def argument_intervalle(angle):
    while True:
        if angle > 2 * pi:
            angle -= 2 * pi
        elif angle < -2 * pi:
            angle += 2 * pi
        else:
            break
    return angle


def my_cosinus(t):
    cos = (exp(1j * t) + exp(-1j * t)) / 2
    return cos.real


def my_sinus(t):
    sin = (exp(1j * t) - exp(-1j * t)) / 2j
    return sin.real


def my_pow(z, n):
    info = cartesion_to_polaire(z)  # [0] = module , [1] = arg
    new_mod = info[0] ** n
    new_arg = (info[1] * n)
    return polaire_to_cartesion(new_mod, new_arg)


def new_multiplication(a, b, c, d, methode=1):
    if methode == 0:
        print("Methode commune : (ac - bd) + i(ad + bc)")
        return (a * c - b * d) + 1j * (a * d + b * c)
    elif methode == 1:
        print("Methode 1 : (r - s) + i(t - r - s) avec\nr = ac, s = bd, t = (a+b)(c+d)")
        r = a * c
        s = b * d
        t = (a + b) * (c + d)
        return (r - s) + 1j * (t - r - s)
    elif methode == 2:
        print("Methode 2 : (r - t) + i(r + s) qvec\nr = c(a+b), s = a(d-c), t = b(c + d)")
        r = c * (a + b)
        s = a * (d - c)
        t = b * (c + d)
        return (r - t) + 1j * (r + s)
    else:
        return None
