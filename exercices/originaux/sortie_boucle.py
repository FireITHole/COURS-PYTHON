liste = [1, 2, 3, 4, 5]

print(liste[-2])
print(liste[1:4])
print(liste[::-1])
print(liste[:4:2])


##############################


liste_inc = [1, [2, [[4, 5], [6, 7, 8], [3, [78]]]]]

# print(liste_inc[1][1][2][1][0])


##############################


def fonction_calcul(n: list[int]):
    if n[0] > 5:
        return -1

    if max(n) > 10:
        return -1

    n.sort()

    return n
