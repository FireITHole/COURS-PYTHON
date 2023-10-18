valeur = input("Valeur : ")

match valeur:
    case "test":
        print("Ceci est un test !")
    case "stop":
        exit(0)
    case "bonjour":
        print("Bonjour !")
    case _:
        print("Defaut!")