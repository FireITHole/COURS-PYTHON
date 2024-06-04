# structure = {"nom" : "blabla", "annee": 2020, "auteur": "JKR"}

bibliotheque: list[dict] = []

while True:
    choix = input("Ajouter un livre (a) ou voir les livres (v) : ")

    match choix:
        case 'a':
            nom = input("Nom : ")
            annee = input("Année : ")
            auteur = input("Auteur : ")

            livre = {"nom": nom, "annee": annee, "auteur": auteur}
            bibliotheque.append(livre)
            print("Livre ajouté !")
        case 'v':
            print(bibliotheque)
        case _:
            print("Choix non valide !")


""" 
dictionnaire = dict()

while True:
    cle = input("clé : ")
    valeur = input("valeur : ")
    dictionnaire[cle] = valeur
    print(dictionnaire) """