# Écrire une fonction "somme" qui prend une liste de nombres en entrée et retourne la somme de tous les éléments de la liste.
def somme(*nombres):
    resultat = 0
    for nb in nombres:
        resultat += nb
    return resultat
    # Equivalent de sum(nombres)

print(somme(1, 2, 3, 4, 5))
# Résultat : 15

# Créer une fonction "inverse" qui prend une liste en entrée et renvoie une nouvelle liste qui est l'inverse de la liste d'origine.
def inverse(liste):
    nouvelle_liste = []
    for i in range(len(liste)-1, -1, -1): # Ittération de la liste à l'envers
        nouvelle_liste.append(liste[i])
    return nouvelle_liste
    # Autre façon de faire : return liste[::-1]

    # Voir fichier range.py

print(inverse([1, 2, 3, 4, 5]))
# Résultat : [5, 4, 3, 2, 1]

# Écrire une fonction "unique" qui prend une liste en entrée et retourne une nouvelle liste contenant uniquement les éléments uniques de la liste d'origine, dans l'ordre de leur première apparition.
def unique(liste):
    liste_vide = []
    for element in liste:
        if liste.count(element) == 1:
            liste_vide.append(element)
    return liste_vide
    # Voir range pour la fonction "set"

print(unique([2, 3, 4, 4, 5, 7, 8, 5, 9, 1, 8]))
# Résultat : [2, 3, 7, 9, 1]
# count permet de récupérer le nombre d'apparation d'un élément dans une liste

# Implémenter une fonction "paires" qui prend une liste de nombres et retourne une nouvelle liste contenant uniquement les nombres pairs.
def paires(nombres):
    resultat = []

    for element in nombres:
        if element % 2 == 0:
            resultat.append(element)
    return resultat

print(paires([1, 2, 3, 4, 56, 77, 88, 90, 76, 23, 25]))
# Résultat : [2, 4, 56, 88, 90, 76]