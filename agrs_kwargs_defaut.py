# *args permet de recevoir un nombre non connu d'arguments
def somme(*args):
    return sum(args)


liste: list = [2, 3, 4, 5]
liste_2: list = [6, 7, 8, 9]

# le caractère * permet de sortir les éléments d'une liste
# print([liste, liste_2])
# [[2, 3, 4, 5], [6, 7, 8, 9]]
# print([*liste, *liste_2])
# [2, 3, 4, 5, 6, 7, 8, 9]


# ** permet de décomposer un dictionnaire (ensemble clé -> valeur)
def print_values(**kwargs):
    for key, val in kwargs.items():
        print(f"{key} : {val}")


# Possible d'utiliser *args et **kwargs simultanement dans une même définition de méthode
def afficher_arguments(*args, **kwargs):
    print("Arguments positionnels (*args):")
    for arg in args:
        print(arg)

    print("\nArguments clé-valeur (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# On peut définir une valeur par défaut pour un paramètre d'une méthode, tous les paramètres par défaut doivent être à la fin
def test(param_1: int, param_2=2, param_3="test"):
    print(param_1)
    print(param_2)
    print(param_3)


test(1)
# 1
# 2
# test


# afficher_arguments(1, 2, 3, nom="Alice", age=25, ville="Paris")
# print_values(test=1, test_2=2)
# print(somme(2, 3, 4, 5, 6, 9, 10, 11))
