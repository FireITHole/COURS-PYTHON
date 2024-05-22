liste_nb_entier: list[int] = [2, 3, 4, 5, 6, 7, 8, 9]
racines_carres: list[float] = []

for nb_entier in liste_nb_entier:
    racines_carres.append(nb_entier**.5)

resultat: list[int] = []

for racine in racines_carres:
    if racine == round(racine, 0):
        resultat.append(int(racine))

print(resultat)

