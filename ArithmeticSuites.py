def aritmetique_1(n, u0, r):
    for x in range(0, n):
        u0 += r
    return u0


def aritmetique_2(n, u0, r):
    return u0 + n * r


def liste_arithmetique(n, u0, r):
    return [u0 + r * x for x in range(0, n)]


def est_arithmetique(liste):
    raison = liste[1] - liste[0]
    i = 1
    while i < len(liste):
        if liste[i] - liste[i - 1] != raison:
            return False
        i += 1
    return True


def somme_arithmetique_1(n, u0, r):
    somme = 0
    for i in range(0, n + 1):
        somme += u0
        u0 += r
    return somme


def somme_arithmetique_2(n, u0, r):
    Sn = ((n + 1) * (u0 + aritmetique_2(n, u0, r)) / 2)
    return Sn