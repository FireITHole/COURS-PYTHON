liste_brut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
liste_resultat = []

for element in liste_brut:
    liste_resultat.append(element * 2)

for element_2 in liste_resultat:
    print(f"L'élément actuel est : {element_2}")