entree = input("Entree votre calcul : ")

liste_brut = entree.split()

if len(liste_brut) != 3:
    print("Il n'y a pas trois éléments dans cette liste !")
    exit(1)

num_1, operateur, num_2 = liste_brut[0], liste_brut[1], liste_brut[2]

if not num_1.isnumeric() and not num_2.isnumeric():
    print("Les nombres ne sont pas des nombres !")
    exit(1)

num_1, num_2 = float(num_1), float(num_2)

operateurs = ['+', '-', 'x', '/', '^']

if operateur not in operateurs:
    print("Cet opérateur n'est pas connu !")
    exit(1)

result: float

match operateur:
    case '+':
        result = num_1 + num_2
    case '-':
        result = num_1 - num_2
    case 'x':
        result = num_1 * num_2
    case '/':
        result = num_1 / num_2
    case '^':
        result = num_1 ** num_2

print(result)