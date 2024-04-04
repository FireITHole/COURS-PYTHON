choix = input("Faites un choix (y/n) : ")

if choix == "y":
    print("Yes")
    print("test")
elif choix == "n":
    print("No")
else:
    print("Votre choix ne correspond à aucun choix prédéfini")
    print("C'est fini !")

match choix:
    case "y":
        print("yes")
    case "n":
        print("No")
    case _:
        print("Autre")

fruits = ["banane", "pomme", "fraise", "framboise"]

choix = input("Citez moi un fruit : ")

if choix in fruits:
    print("Oui, ce fruit est dans la liste")
else:
    print("Non, ce fruit n'est pas dans la liste")
