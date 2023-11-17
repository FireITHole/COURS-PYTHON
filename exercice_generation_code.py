# XXXXX-XXXXX-XXXXX-XXXXX
# doit pouvoir varier nombre de X dans une chaine
# Doit pouvoir varier nombre de chaînes de x
# Doit pouvoir changer le séparateur entre les chaînes de X
# Doit pouvoir générer x nombre de code d'activation
# Charactères utilisés : lettre majuscules et chiffres

from random import choices

population = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
aleatoire = "".join(choices(population, k=5))
