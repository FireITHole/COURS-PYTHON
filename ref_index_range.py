liste = [1, 2, 3, 4, 5]

print(*liste)

def somme(*nombres) -> int:
    result = 0
    for nombre in nombres:
        result += nombre
    return result

print(somme(1, 2, 3, 4, 5, 6, 7))