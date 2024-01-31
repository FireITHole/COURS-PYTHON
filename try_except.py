try:
    choix = int(input("Veuillez rentrer un nombre : "))
    print(choix)
except ValueError as error:
    print(f"Une erreur est survenue : {error}")
except KeyError as kerror:
    print(f'Une erreur de type kerror est survenue : {kerror}')

print("La fin !")