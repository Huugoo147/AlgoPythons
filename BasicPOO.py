from __future__ import division

from math import *
from Tkinter import Canvas, Tk, LEFT


class Vecteur:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "({}, {}, {})".format(self.x, self.y, self.z)

    def norme(self):
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def produit_par_scalaire(self, k):
        W = Vecteur(self.x * k, self.y * k, self.z * k)
        return W

    def __add__(self, V2):
        W = Vecteur(self.x + V2.x, self.y + V2.y, self.z + V2.z)
        return W

    def change(self, x=None, y=None, z=None):
        if x != None and (type(x) == int or type(x) == float):
            self.x = x
        if y != None and (type(y) == int or type(y) == float):
            self.y = y
        if z != None and (type(z) == int or type(z) == float):
            self.z = z


class Matrice:
    def __init__(self, a, b, c, d):
        self.a = a;
        self.b = b
        self.c = c;
        self.d = d

    def __str__(self):
        return "{} {}\n{} {}".format(self.a, self.b, self.c, self.d)

    def tr(self):
        return self.a + self.d

    def det(self):
        return self.a * self.d - self.b * self.c

    def produit_par_scalaire(self, k):
        W = Matrice(self.a * k, self.b * k, self.c * k, self.d * k)
        return W

    def inverse(self):
        determinant = self.det()
        if determinant == 0:
            return None
        NewM = Matrice(self.d, -self.b, -self.c, self.a)
        return NewM.produit_par_scalaire(1 / determinant)

    def __add__(self, M2):
        return Matrice(self.a + M2.a, self.b + M2.b, self.c + M2.c, self.d + M2.d)

    def __mul__(self, M2):
        a = self.a * M2.a + self.b * M2.c
        b = self.a * M2.b + self.b * M2.d
        c = self.c * M2.a + self.d * M2.c
        d = self.c * M2.b + self.d * M2.d
        return Matrice(a, b, c, d)


def fibonacci(rang):
    W = Matrice(0, 1, 1, 1)
    Wi = W
    for i in range(rang - 2):
        W *= Wi
    return W.d


# M1 = Matrice(4, 3, 2, 1)
# M2 = Matrice(1, 0, -1, 1)
# M3 = M1 + M2
# M4 = M1 * M2
#
# root = Tk()
# can = Canvas(root, width=800, height=800, background='white')
# can.pack(side=LEFT, padx=5, pady=5)


class BasicTurtle:
    def __init__(self, x=0, y=0, color='red', taille=2):
        self.x = x
        self.y = y
        self.trace = True
        self.color = color
        self.taille = taille

    def coords(self):
        return [self.x, self.y]

    def goto(self, x, y):
        if self.trace:
            can.create_line(self.x, self.y, x, y, fill=self.color, width=self.taille)
        self.x = x;
        self.y = y

    def up(self):
        self.trace = False

    def down(self):
        self.trace = True

    def couleur(self, couleurv):
        self.color = couleurv

    def taille(self, New):
        self.taille = New


# T = BasicTurtle()
# T.goto(100,100) ;  T.up(); T.goto(200,100); T.down(); T.goto(100,200)

# T1 = BasicTurtle() ; T2 = BasicTurtle() ; T3 = BasicTurtle()
# T2.couleur("blue") ; T3.couleur("green")
# for i in range(400):
# x1,y1 = (3/2)*i,i
# x2,y2 = i,5*sqrt(i)
# x3,y3 = (x1+x2)/2,(y1+y2)/2
# T1.goto(x1,y1) ; T2.goto(x2,y2), T3.goto(x3,y3)

def reduction_mesure(x):
    while True:
        if x >= 360:
            x -= 360
        elif x <= -360:
            x += 360
        else:
            break
    return x


class AdvancedTurtle(BasicTurtle):
    def __init__(self, x=0, y=0, color='red', taille=2):
        BasicTurtle.__init__(self, x, y, color, taille)
        self.direction = 0

    def change_direction(self, x):
        self.direction = reduction_mesure(x)

    def rotation(self, angle):
        self.direction += reduction_mesure(angle)

    def avancer(self, l):
        newX = self.x + l * cos(2 * pi / 360 * self.direction)
        newY = self.y + l * sin(2 * pi / 360 * self.direction)
        self.goto(newX, newY)

    def orienter_vers(self, other):
        x1, y1 = self.x, self.y
        x2, y2 = other.x, other.y
        teta = (360 / (2 * pi)) * atan2(y2 - y1, x2 - x1)
        self.change_direction(teta)

#
# T1 = AdvancedTurtle(color="blue", taille=1)
# T2 = BasicTurtle(x=700, taille=2)
# for i in range(2000):
#     T2.goto(T2.x, i)
#     T1.orienter_vers(T2)
#     T1.avancer(2)
#     if T1.x == T2.x:
#         print("es")
#         break
#
# root.mainloop()
