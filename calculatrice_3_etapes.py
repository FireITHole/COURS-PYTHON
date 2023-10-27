# Attention faille sécurité avec eval()

num_1 = input("Entrez nombre 1 : ")
try:
    num_1 = float(num_1)
except ValueError:
    print("Num 1 n'est pas un nombre !")
    exit(1)

operation = input("Que voulez vous faire (+, -, *, /) : ")
list_operateurs = ['+', '-', '*', '/']

if operation not in list_operateurs:
    print("Votre opérateur n'est pas bon !")
    exit(1)

num_2 = input("Entrez nombre 2 : ")
try:
    num_2 = float(num_2)
except ValueError:
    print("Num 2 n'est pas un nombre !")
    exit(1)

# eval(operation) -> Attention! Faille sécurité car éxecution de l'entrée utilisateur
result = eval(f"{num_1}{operation}{num_2}")
print(result)


""" match operation:
    case '+':
        result = num_1 + num_2
    case '-':
        result = num_1 - num_2
    case 'x':
        result = num_1 * num_2
    case '/':
        result = num_1 / num_2 """

""" print(result) """