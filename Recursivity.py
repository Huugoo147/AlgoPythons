from __future__ import division
from __future__ import print_function

import turtle
from random import randint

LONGEUR = 800;
LARGEUR = 800
turtle.setup(LONGEUR, LARGEUR)
turtle.title("Sah")
turtle.bgcolor("white")
turtle.showturtle()


def somme_carres_classique(n):
    somme = 0
    for i in range(n + 1):
        somme += i ** 2
    return somme


# somme_carres_classique(50)


def somme_carre_recur(n):
    if n == 1:
        somme = 1
    else:
        somme = somme_carre_recur(n - 1) + n ** 2
    return somme


def inversion_liste(my_array):
    if len(my_array) <= 1:
        return my_array
    else:
        x0 = my_array[0]
        fin_liste = my_array[1:]
        liste_inverse = inversion_liste(fin_liste)
        liste_inverse.append(x0)
        print(liste_inverse)
    return liste_inverse


def maximum(my_array):
    if len(my_array) <= 1:
        return my_array
    else:
        x0 = my_array[0]
        max = maximum(my_array[1:])
        if x0 >= max:
            M = x0
        elif x0 < max:
            M = max
    return M


def binaire(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        chaine = binaire(n // 2)
        if n % 2 == 0:
            chaine += "0"
        else:
            chaine += "1"
    return chaine


def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        x1 = fibo(n - 1)
        x2 = fibo(n - 2)
        print(x1, x2)
        return x1 + x2


def coef_newton(k, n):
    if k == 0 or k == n:
        return 1
    else:
        return coef_newton(k - 1, n - 1) + coef_newton(k, n - 1)
        print(k, n)


def pascal(N):
    for n in range(N):
        for k in range(n + 1):
            element = coef_newton(k, n)
            print(element, end=" ")
        print()


def pascal_impaire(N):
    for n in range(N + 1):
        for k in range(n + 1):
            element = coef_newton(k, n)
            if element % 2 == 0:
                element = " "
            else:
                element = "X"
            print(element, end=" ")
        print()


def somme_chiffres(n):
    if n < 10:
        return n
    else:
        x = n % 10
        nn = n // 10
        S = x + somme_chiffres(nn)
    return S


def residu(n):
    if n < 10:
        return n
    new_sum = somme_chiffres(n)
    mew_try = residu(new_sum)
    return mew_try


turtle.up()
turtle.goto(0, 0)
turtle.down()
turtle.speed("fastest")


def kosh(l, n):
    if n == 0:
        turtle.forward(l)
    else:
        kosh(l / 3, n - 1)
        turtle.left(60)
        kosh(l / 3, n - 1)
        turtle.right(120)
        kosh(l / 3, n - 1)
        turtle.left(60)
        kosh(l / 3, n - 1)


# kosh(1000,3)

def arbre(l, n):
    if n == 0:
        return
    P = turtle.position()
    turtle.setheading(-120)
    turtle.forward(l)
    arbre(l / 2, n - 1)
    turtle.goto(P)
    turtle.setheading(-60)
    turtle.forward(l)
    arbre(l / 2, n - 1)
    turtle.goto(P)


def triangle(l, n):
    if n == 0:
        return
    for i in range(3):
        triangle(l / 2, n - 1)
        turtle.fd(l)
        turtle.left(120)


# triangle(100,5)


def hilber(teta, n):
    if n == 0:
        return
    turtle.left(-teta)
    hilber(-teta, n - 1)
    turtle.fd(10)
    turtle.left(teta)
    hilber(teta, n - 1)
    turtle.fd(10)
    hilber(teta, n - 1)
    turtle.left(teta)
    turtle.fd(10)
    hilber(-teta, n - 1)
    turtle.left(-teta)


# hilber(90,10)

def quart_cercle(pas):
    for i in range(45):
        turtle.left(2)
        turtle.forward(pas)


def fractale_cercle(l, n):
    if n == 0:
        return

    for __ in range(4):
        quart_cercle(l)

        hasard = randint(0, 3)
        if hasard == 2:
            fractale_cercle(l / 3, n - 1)

    return


# fractale_cercle(4,50)
# arbre(100,7)


turtle.exitonclick()
