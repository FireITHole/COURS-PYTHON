liste_1: list[int] = [1, 2, 3]
liste_2: list[str] = ['a', 'b', 'c']
liste_3: list[float] = [1.2, 3.4, 5.6]

resultat = []

for nb, car, fl in zip(liste_1, liste_2, liste_3):
    resultat.append([nb, car, fl])

print(resultat)