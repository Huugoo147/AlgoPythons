from cmath import *
import matplotlib.pyplot as plt

plt.clf()
plt.axhline(y=0, color='r', linestyle='-')
plt.axvline(x=0, color='r', linestyle='-')
plt.axes().set_aspect('equal')


def draw_polygone(n):
    i = 0
    array = []
    while i <= n:
        val = (rect(1, (2 * pi) / n)) ** i
        array.append(val)
        plt.scatter(val.real, val.imag, color='red', s=10)
        if i > 0:
            plt.plot([array[i - 1].real, array[i].real], [array[i - 1].imag, array[i].imag], color="blue")
        i += 1


# draw_polygone(4)
z = 2 - 4j
z2 = 2 * z
w = (-1 / 2) + ((3 ** 0.5) / 2) * 1j


def draw_triangle(z1, z2, z3):
    plt.clf()
    plt.scatter(z1.real, z1.imag, color='red', s=50)
    plt.scatter(z2.real, z2.imag, color='red', s=50)
    plt.scatter(z3.real, z3.imag, color='red', s=50)

    plt.plot([z1.real, z2.real], [z1.imag, z2.imag], color='black')
    plt.plot([z2.real, z3.real], [z2.imag, z3.imag], color='black')
    plt.plot([z3.real, z1.real], [z3.imag, z1.imag], color='black')


# exemple de triangles:
# draw_triangle(z,z2,(1+2j)*z)
# draw_triangle(z, w*z, (w**2)*z)

plt.show()
