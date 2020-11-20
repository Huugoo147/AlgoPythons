from random import sample

list_trier = sample(range(0, 1000), 10)


def tri_selection(my_array):
    for i in range(0, len(my_array)):
        rg_min = i
        for j in range(i + 1, len(my_array)):
            if my_array[j] < my_array[rg_min]:
                rg_min = j
        my_array[i], my_array[rg_min] = my_array[rg_min], my_array[i]
    return my_array


def tri_insertion(my_array):
    for i in range(0, len(my_array)):
        pivot = my_array[i]
        j = i
        while (j > 0) and (my_array[j - 1] > pivot):
            my_array[j] = my_array[j - 1]
            j -= 1
        my_array[j] = pivot
    print(my_array)
    return my_array


def tri_bulle(my_array):
    n = len(my_array)
    compteur, compteur_change = 0, 0
    for i in reversed(range(0, n)):
        compteur += 1
        for j in range(0, i):
            if my_array[j + 1] < my_array[j]:
                my_array[j], my_array[j + 1] = my_array[j + 1], my_array[j]
                compteur_change += 1
        print("Passage numero {}, {} changements:\n{}".format(compteur, compteur_change, my_array))
        compteur_change = 0
    return my_array


def fusion(my_array_g, my_array_d):
    n, m = len(my_array_g), len(my_array_d)
    i, j = 0, 0
    my_array_fusionne = []
    while (i < n) and (j < m):
        if my_array_g[i] < my_array_d[j]:
            my_array_fusionne.append(my_array_g[i])
            i += 1
        else:
            my_array_fusionne.append(my_array_d[j])
            j += 1
    if len(my_array_fusionne) < n + m:
        while i < n:
            my_array_fusionne.append(my_array_g[i])
            i += 1
        while j < m:
            my_array_fusionne.append(my_array_d[j])
            j += 1
    return my_array_fusionne


def tri_fusion(my_array):
    print(my_array)
    if len(my_array) <= 1:
        return my_array
    else:
        my_array_g = tri_fusion(my_array[:len(my_array) // 2])
        my_array_d = tri_fusion(my_array[len(my_array) // 2:])
        return fusion(my_array_g, my_array_d)


print(tri_fusion(list_trier))
