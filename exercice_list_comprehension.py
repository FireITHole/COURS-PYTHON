# Exercice 1
# Écrire une liste de compréhension qui génère les carrés des nombres de 1 à 10.


# Résultat devrait être : [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Exercice 2
# Créer une liste de compréhension qui filtre les nombres pairs dans une liste donnée de nombres.
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 16, 18, 20, 23]


# Résultat devrait être : [2, 4, 6, 8, 10, 16, 18, 20]

# Exercice 3
# Utiliser une liste de compréhension pour créer une nouvelle liste contenant la longueur de chaque mot dans une phrase. Par exemple, pour la phrase "Hello World", la liste résultante serait [5, 5].
data = "Bonjour comment ça va ?"


# Résultat devrait être : [7, 7, 2, 2, 1]

# Exercice 4
# Utiliser une liste de compréhension pour décomposer les niveaux d'une liste de profondeur 2. Par exemple, la liste [[1, 2, 3], [4, 5, 6]] deviendra [1, 2, 3, 4, 5, 6]
data = [[1, 2, 3], [4, 5, 6]]


# Résultat devrait être : [1, 2, 3, 4, 5, 6]

# Exercice 5
# Créer une liste de compréhension qui extrait tous les chiffres d'une chaîne de caractères. Par exemple, pour la chaîne "Il y a 3 pommes et 5 oranges", la liste résultante serait [3, 5].
data = "Il y a 3 pommes et 5 oranges"


# Résultat devrait être : [3, 5]

# Exercice 6
# Écrire une liste de compréhension qui génère tous les nombres premiers jusqu'à 50.
def est_premier(nombre):
    if nombre < 2:
        return False
    for i in range(2, int(nombre**0.5) + 1):
        if nombre % i == 0:
            return False
    return True




# Résultat devrait être : [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

# Exercice 7
# Utiliser une liste de compréhension pour créer une liste de toutes les voyelles dans une chaîne de caractères donnée.
data = "Les listes de comprehension sont tres utiles"


# Résultat devrait être : ['e', 'i', 'e', 'e', 'o', 'e', 'e', 'i', 'o', 'o', 'e', 'u', 'i', 'e']

# Exercice 8
# Utiliser une liste de compréhension pour créer une liste de tuples, où chaque tuple contient un nombre et son carré, pour les nombres de 1 à 5.


# Résultat devrait être : [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

# Exercice 9
# Écrire une liste de compréhension qui supprime les doublons d'une liste.
data = [1, 2, 3, 4, 4, 5, 8, 6, 5, 2, 9]


# Résultat devrait être : [1, 2, 3, 4, 5, 8, 6, 9]

# Exercice 10
# Créer une liste de compréhension qui fusionne les éléments de deux listes de manière alternative. Par exemple, pour les listes [1, 2, 3] et ['a', 'b', 'c'], le résultat devrait être [1, 'a', 2, 'b', 3, 'c'].
data = ([1, 2, 3], ['a', 'b', 'c'])


# Résultat devrait être : [1, 'a', 2, 'b', 3, 'c']