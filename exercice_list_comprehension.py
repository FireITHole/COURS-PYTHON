# Exercice 1
# Écrire une liste de compréhension qui génère les carrés des nombres de 1 à 10.
# Méthode standard
resultat = []
for i in range(1, 11):
    resultat.append(i**2)
print(resultat)

# Equivalent en compréhension de liste
print([i**2 for i in range(1, 11)])

# Résultat devrait être : [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Exercice 2
# Créer une liste de compréhension qui filtre les nombres pairs dans une liste donnée de nombres.
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 16, 18, 20, 23]
# Méthode standard
resultat = []
for nombre in data:
    if nombre % 2 == 0:
        resultat.append(nombre)
print(resultat)

# Equivalent en compréhension de liste :
print([nombre for nombre in data if not nombre % 2])
# Résultat devrait être : [2, 4, 6, 8, 10, 16, 18, 20]

# Compréhension de liste pour condition au moment de la définition de l'élément à ajouter à la liste
print(
    [
        nombre
        if nombre % 2 == 0
        else "le chiffre est 3"
        if nombre == 3
        else "autre impaire"
        for nombre in data
    ]
)


# Exercice 3
# Utiliser une liste de compréhension pour créer une nouvelle liste contenant la longueur de chaque mot dans une phrase. Par exemple, pour la phrase "Hello World", la liste résultante serait [5, 5].
# Méthode standard
data = "Bonjour comment ça va ?"
resultat = []
for mot in data.split():
    resultat.append(len(mot))
print(resultat)

# Equivalent en compréhension de liste :
print([len(mot) for mot in data.split()])

# Résultat devrait être : [7, 7, 2, 2, 1]

# Exercice 4
# Utiliser une liste de compréhension pour décomposer les niveaux d'une liste de profondeur 2. Par exemple, la liste [[1, 2, 3], [4, 5, 6]] deviendra [1, 2, 3, 4, 5, 6]
data = [[1, 2, 3], [4, 5, 6]]
# Méthode standard
resultat = []
for liste in data:
    for nombre in liste:
        resultat.append(nombre)
print(resultat)

# Méthode compréhension de liste
print([nombre for liste in data for nombre in liste])

# Résultat devrait être : [1, 2, 3, 4, 5, 6]

# Exercice 5
# Créer une liste de compréhension qui extrait tous les chiffres d'une chaîne de caractères. Par exemple, pour la chaîne "Il y a 3 pommes et 5 oranges", la liste résultante serait [3, 5].
data = "Il y a 3 pommes et 5 oranges"

# Méthode standard
resultat = []
for character in data:
    if character.isdigit():
        resultat.append(int(character))
print(resultat)

# Méthode compréhension de liste
print([int(character) for character in data if character.isdigit()])

# Résultat devrait être : [3, 5]


# Exercice 6
# Écrire une liste de compréhension qui génère tous les nombres premiers jusqu'à 50.
def est_premier(nombre):
    for i in range(2, int(nombre**0.5) + 1):
        if nombre % i == 0:
            return False
    return True


# Méthode standard
resultat = []
for nombre in range(1, 51):
    if est_premier(nombre):
        resultat.append(nombre)
print(resultat)

# Méthode par compréhension de liste
print([nombre for nombre in range(1, 51) if est_premier(nombre)])

# Résultat devrait être : [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

# Exercice 7
# Utiliser une liste de compréhension pour créer une liste de toutes les voyelles dans une chaîne de caractères donnée.
data = "Les listes de comprehension sont tres utiles"

# Méthode standard
voyelles = "aeiouy"
resultat = []
for char in data:
    if char in voyelles:
        resultat.append(char)
print(resultat)

# Méthode par liste de compréhension
print([char for char in data if char in voyelles])

# Si on veut trouver le nombre de voyelle dans data :
print(len([char for char in data if char in voyelles]))

# Résultat devrait être : ['e', 'i', 'e', 'e', 'o', 'e', 'e', 'i', 'o', 'o', 'e', 'u', 'i', 'e']

# Exercice 8
# Utiliser une liste de compréhension pour créer une liste de tuples, où chaque tuple contient un nombre et son carré, pour les nombres de 1 à 5.
# Méthode standard
resultat = []
for x in range(1, 6):
    resultat.append((x, x**2))
print(resultat)

# Compréhension de liste :
print([(x, x**2) for x in range(1, 6)])

# Compréhension de liste peut s'appliquer à tout type d'itérateur. Exemple : tuple, set.

# Résultat devrait être : [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

# Création d'un dictionnaire avec une compréhension de liste
# cles = [str(x) for x in range(1, 11)]
# valeurs = list(range(1, 11))
cles = ["1", "2", "3"]
valeurs = [1, 2, 3]

# Méthode standard
resultat = {}
for cle, valeur in zip(cles, valeurs):
    resultat[cle] = valeur
print(resultat)

# Méthode compréhension de liste
print({cle: valeur for cle, valeur in zip(cles, valeurs)})


# Exercice 9
# Écrire une liste de compréhension qui supprime les doublons d'une liste.
data = [1, 2, 3, 4, 4, 5, 8, 6, 5, 2, 9]
liste_vide = []
# Compréhension de liste pas seulement utile pour créer une liste mais également pour éxecuter du code dans une boucle for
[liste_vide.append(nombre) for nombre in data if nombre not in liste_vide]
print(liste_vide)

# Même résultat qu'au dessus via l'utilisation de la fonction set
print(list(set(data)))

# Résultat devrait être : [1, 2, 3, 4, 5, 8, 6, 9]

# Exercice 10
# Créer une liste de compréhension qui fusionne les éléments de deux listes de manière alternative. Par exemple, pour les listes [1, 2, 3] et ['a', 'b', 'c'], le résultat devrait être [1, 'a', 2, 'b', 3, 'c'].
data = ([1, 2, 3], ["a", "b", "c"])

# Méthode standard
resultat = []
for pair in zip(data[0], data[1]):
    for element in pair:
        resultat.append(element)
print(resultat)

# Compréhension de liste
print([element for pair in zip(data[0], data[1]) for element in pair])

# Résultat devrait être : [1, 'a', 2, 'b', 3, 'c']
