import matplotlib.pyplot as plt
import Equation_Solver as Eq_Solver

plt.clf()
plt.axhline(y=0, color='r', linestyle='-')
plt.axvline(x=0, color='r', linestyle='-')
plt.axes().set_aspect('equal')


def affiche_racines(a, b, c, color="red"):
    X1, X2 = Eq_Solver.solve_trinome(a, b, c)
    plt.scatter(X1.real, X1.imag, color=color, s=100)
    plt.scatter(X2.real, X2.imag, color=color, s=100)


def affiche_famille(b, c, bb, cc, n=10):
    affiche_racines(1, b, c, color='red')
    affiche_racines(1, bb, cc, color='green')
    for k in range(1, n):
        t = k / n
        a = (1 - t) * b + t * bb
        b = (1 - t) * c + t * cc
        affiche_racines(1, a, b, color="blue")


affiche_famille(-2, 2, 3, (12 / 5), 300)

plt.show()
