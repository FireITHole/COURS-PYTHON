print(*range(0, 6))
# Résultat : 0 1 2 3 4 5

print(range(1, 5))
# Résultat : range(1, 5) (Objet range)

print(*range(5))
# Résultat : 0 1 2 3 4

print(*range(0, 10, 2))
# Résultat : 0 2 4 6 8
# Attention : 0 = start, 10 = stop, 2 = range

print(*range(5, 0, -1))
# Résultat : 5 4 3 2 1

liste = [1, 2, 3, 4, 5]

for i in range(len(liste)):
    print(liste[i])
# Itération de liste à l'endroit 1 2 3 4 5

for i in range(len(liste)-1, -1, -1):
    print(liste[i])
# Itération de liste à l'envers 5 4 3 2 1

# Autre façon d'inverser une liste :
print(liste[::-1])

# Récupérer dernière élément d'une liste :
print(liste[-1])

liste_profonde = [[1, 2], [3, 4]]

# Récupération de 2
print(liste_profonde[0][1])

liste_count = [1, 2, 2, 2, 3, 5, 5, 4, 4, 1]
print(liste_count.count(4))
# count permet de récupérer le nombre d'apparition d'un élément dans une liste

# Enlever les doublons d'une liste
liste_doublons = [1, 2, 2, 2, 3, 5, 5, 4, 4, 1]

print(set(liste_doublons))
# un set est un type de variable proche du dictionnaire où les élements du set ne peuvent pas apparaître en doublons
print(list(set(liste_doublons)))
# Rajouter un list devant le set permet de caster le set en une nouvelle liste