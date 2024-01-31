liste = ["banane", "orange", "pomme", "framboise", "fraise"]
print(liste[2]) # Sélection par index (base 0)
print(liste[-1]) # Sélection du dernier élément de la liste

print(len(liste)) # Récupérer longueur de la liste

print(liste[0:3]) # Extraction d'une plage d'éléments via index (dernier index non-inclus)
print(liste[::-1]) # Inverser liste

liste_brut = []
liste_brut.append("banane") # Ajouter un élément à une liste
print(liste_brut)
liste_brut.append("orange")
print(liste_brut)
liste_brut[1] = "framboise" # Altérer valeur d'un élément de la liste par son index
print(liste_brut)

liste_brut.pop(0) # Supprime le dernier élément de la liste (par défaut), paramètre index dispo pour supprimer un élément précis
print(liste_brut)

liste_brut.remove("framboise") # Supprime un élément par sa valeur (renvoi une erreur si le paramètre de la fonction remove n'est aps un élément de la liste)
print(liste_brut)

phrase_liste = ["il", "fait", "beau", "dehors"]
phrase = " ".join(phrase_liste) # Inverse de .split(), permet de créer un str à partir d'une liste
print(phrase)