from __future__ import division

from cmath import *
from math import *

import matplotlib.pyplot as plt


def init():
    plt.clf()
    plt.axhline(y=0, color='r', linestyle='-')
    plt.axvline(x=0, color='r', linestyle='-')
    plt.axes().set_aspect('equal')


def show_points(z_list, color="red", size=5):
    i = 0
    while i < len(z_list):
        plt.scatter(z_list[i].real, z_list[i].imag, color=color, s=size)
        if i >= 1:
            plt.plot([z_list[i - 1].real, z_list[i].real], [z_list[i - 1].imag, z_list[i].imag], color=color)
        i += 1
    plt.plot([z_list[-1].real, z_list[0].real], [z_list[-1].imag, z_list[0].imag], color=color)


array = [5 + 5j, 4 + 4j, 3 + 3j]


# show_points(list,"blue",50)

def get_circle(z0, r, n=100):
    i = 0
    my_list = []
    while i <= n:
        k = i / n
        z1 = (r * exp(2j * k * pi)) + z0
        my_list.append(z1)
        i += 1
    return my_list


def draw_segment(z0, z1, n=50):
    i = 0
    my_list = []
    while i < n:
        t = i / n
        my_list.append((1 - t) * z0 + t * z1)
        i += 1
    show_points(my_list)


def translation(z_liste, k):
    new_list = []
    for z in z_liste:
        new_list.append(z + k)
    show_points(new_list)


def homeothie(z_liste, v):
    new_list = []
    for z in z_liste:
        new_list.append(z * v)
    show_points(new_list)


def rotation(z_liste, angle):
    new_list = []
    for z in z_liste:
        new_list.append(z * exp(angle * 1j))
    show_points(new_list)


def symetrie(z_liste):
    new_list = []
    for z in z_liste:
        new_list.append(z.conjugate())
    show_points(new_list)


def inversion(z_liste):
    new_list = []
    for z in z_liste:
        try:
            new_list.append(1 / z)
        except:
            pass
    show_points(new_list)


def au_carre(z_liste):
    new_list = []
    for z in z_liste:
        new_list.append(z * z)
    return new_list


z0 = 0
z1 = z0 + 1 * 1j
z2 = z1 + 1
z3 = z2 - 1 * 1j
p = [z0, z1, z2, z3]
centre = (2 + 2j)


def initialisation_presentation():
    init()
    draw_segment(z0, z1)
    draw_segment(z1, z2)
    draw_segment(z2, z3)
    draw_segment(z3, z0)


# initialisation_presentation()
# p1 = translation(p,2-1j)
# c1 = translation(c,2-1j)
# plt.show()

# initialisation_presentation()
# homeothie(p,1.5)
# homeothie(c,1.5)
# plt.show()

# initialisation_presentation()
# rotation(c,pi/4)
# rotation(p,pi/4)
# plt.show()

# initialisation_presentation()
# symetrie(p)
# symetrie(c)
# plt.show()

# initialisation_presentation()
# inversion(c)
# inversion(p)
# plt.show()

# initialisation_presentation()
# au_carre(c)
# au_carre(p)

plt.show()
