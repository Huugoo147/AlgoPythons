from __future__ import division

from math import *
from random import *
from time import sleep

from Tkinter import *

root = Tk()
LONGUEUR = 800;
HAUTEUR = 600
can = Canvas(root, width=LONGUEUR, height=HAUTEUR, background='white')
can.pack(side=LEFT)

axe_i = lambda x: LONGUEUR // 2 + x
axe_j = lambda y: HAUTEUR // 2 - y


class Particule():
    def __init__(self, x, y, vx, vy, m, color):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.m = m
        self.color = color
        self.compteur = 0

    def __str__(self):
        return "P : ({},{})\nV : ({},{})\nm : {}".format(self.x, self.y, self.vx, self.vy, self.m)

    def action_vitese(self):
        self.x += self.vx
        self.y += self.vy

    def action_gravite(self, g):
        self.vy -= g

    def bord(self):
        if self.x >= (LONGUEUR / 2) - self.m or self.x <= (-LONGUEUR / 2) + self.m:
            self.vx *= -1
        if self.y >= (HAUTEUR / 2) - self.m or self.y <= (-HAUTEUR / 2) + 2 * self.m:
            self.vy *= -1
            if self.vx <= 1 / 2:
                self.compteur += 1

    def action_frottement(self, frottement=0.005, expo=2):
        v = sqrt((self.vx ** 2) + (self.vy ** 2))
        self.vx = self.vx - (frottement / self.m) * (v ** expo) * (self.vx / v)
        self.vy = self.vy - (frottement / self.m) * (v ** expo) * (self.vy / v)

    def mouvement(self):
        self.action_vitese();
        self.action_gravite(3);
        self.action_frottement();
        self.bord()

    def affiche(self, t=10, arrow="last", trait=True, rond=True):
        while t > 0 and self.compteur < 10:
            old = [axe_i(self.x), axe_j(self.y)]
            if rond:
                can.create_oval(old[0] - 3, old[1] - 3, old[0] + 3, old[1] + 3, fill=self.color)
            self.mouvement()

            if trait:
                can.create_line(old[0], old[1], axe_i(self.x), axe_j(self.y), arrow=arrow, width=2)
            t -= 1
        if self.compteur == 10:
            self.y = -399
            self.vy = 0


class Planete(Particule):

    def __init__(self, x, y, vx, vy, m, color):
        Particule.__init__(self, x, y, vx, vy, m, color)

    def action_attration(self, other):
        x = (other.x - self.x);
        y = (other.y - self.y)
        r = sqrt(x ** 2 + y ** 2)
        gx = ((100 * self.m * other.m) / r ** 2) * x / r
        gy = ((100 * self.m * other.m) / r ** 2) * y / r
        self.vx += gx / self.m
        self.vy += gy / self.m

    def bord(self):
        if self.x >= (LONGUEUR / 2) - self.m or self.x <= (-LONGUEUR / 2) + self.m:
            self.vx *= -1
        if self.y >= (HAUTEUR / 2) - self.m or self.y <= (-HAUTEUR / 2) + 2 * self.m:
            self.vy *= -1

    def mouvement(self):
        self.action_vitese();
        self.bord()


class TkPlanete(Planete):

    def __init__(self, x, y, vx, vy, m, color):
        Planete.__init__(self, x, y, vx, y, m, color)
        rayon = 2 * min(max(2, self.m), 10) // 2
        id = can.create_oval(axe_i(self.x) - rayon, axe_j(self.y) - rayon, axe_i(self.x) + rayon, axe_j(self.y) + rayon,
                             fill=self.color)
        self.id = id

    def affiche(self, trait=False):
        old = [axe_i(self.x), axe_j(self.y)]
        self.mouvement()
        if trait:
            can.create_line(old[0], old[1], axe_i(self.x), axe_j(self.y), arrow=arrow, width=2)
        can.move(self.id, self.vx, self.vy)


def hasard_couleur():
    R, V, B = randint(0, 255), randint(0, 255), randint(0, 255)
    return '#%02x%02x%02x' % (R % 256, V % 256, B % 256)


# Soleil = TkPlanete(-20, 0, 0, 0, 100, "yellow")
# Terre = TkPlanete(200, 5, 0, 0, 20, "blue")
# Mars = TkPlanete(-300, -5, 0, 0, 10, "red")
# for t in range(2000):
#     Terre.action_attration(Soleil)
#     # Terre.action_attration(Mars)
#     Mars.action_attration(Soleil)
#     # Mars.action_attration(Terre)
#     Terre.affiche();
#     Mars.affiche()
#     can.update();
#     sleep(0.0065)
# root.mainloop()
