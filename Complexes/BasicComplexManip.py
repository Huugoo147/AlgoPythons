z1 = 1 + 2j
z2 = 3 - 1j
somme = z1 + z2
mul = z1 * z2
pow = z1 * z1
module = abs(z1)
inv = 1 / z1

z3 = ((3 - 4j) ** 2) * (2 + 1j)
reel = z3.real
img = z3.imag
conj = z3.conjugate()


def addition(a, b, aa, bb):
    real = a + aa
    imag = b + bb
    return "{} + {}i".format(real, imag)


def multiplication(a, b, aa, bb):
    real = a * aa + -(b * bb)
    imag = a * bb + b * aa
    return [real, imag]


def my_conjugate(a, b):
    return "{}+{}i".format(a, -b)


def my_module(a, b):
    return (a ** 2 + b ** 2) ** 0.5


def my_reverse(a, b):
    denom = a ** 2 + b ** 2
    num = my_conjugate(a, b)
    return "{} / {}".format(num, denom)


def my_pow(a, b, n):
    initial_a = a
    initial_b = b
    while n > 1:
        new = multiplication(a, b, initial_a, initial_b)
        a = new[0];
        b = new[1]
        n -= 1
    return "{}+{}i".format(a, b)
