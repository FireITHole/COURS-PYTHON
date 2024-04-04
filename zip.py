liste_cles = ["Nom", "Prénom", "Age"]
liste_valeurs = ["Adam", "Thierry", 62]

result = {}
for cle, valeur in zip(liste_cles, liste_valeurs):
    result[cle] = valeur

print(result)

print(result.keys())
print(result.values())
print(result.items())

liste = [["cle", "valeur"], ["test1", "test2"]]

for x1, x2 in liste:
    print(x1, x2)