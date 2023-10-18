liste: list = [1, 2, 3, 4, 5]

for i, valeur in enumerate(liste[1:]):
    liste[i+1] = valeur + liste[i]

print(liste)