def solve_equation_lineaire(equation="10*x = 30"):
    splited_equation = equation.split("=")
    membre1 = splited_equation[0]
    if splited_equation[1] != '0':
        membre1 = membre1 + "-" + splited_equation[1]
    membre1 = membre1.replace('x', " 1j")
    z = eval(membre1)
    return -z.real / z.imag


def solve_trinome(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant == 0:
        return [-b / (2 * a), -b / (2 * a)]
    elif discriminant > 0:
        z1 = (-b + discriminant ** 0.5) / 2 * a
        z2 = (-b - discriminant ** 0.5) / 2 * a
        return [z1, z2]
    else:
        z1 = (-b + 1j * (-discriminant) ** 0.5) / 2 * a
        z2 = z1.conjugate()
        return [z1, z2]


def solve_somme_produits(S, P):
    return solve_trinome(1, -S, P)


def solution_bicare(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant >= 0:
        solutions = []
        X1, X2 = solve_trinome(a, b, c)
        for x in [X1, X2]:
            if x >= 0:
                solutions += [x ** 0.5, -x ** 0.5]
            if x < 0:
                solutions += [1j * (-x) ** 0.5, -1j * (-x) ** 0.5]
        return solutions
    else:
        print("impossible")
        return -1
