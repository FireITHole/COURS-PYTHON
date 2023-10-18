import sys

try:
    file_name = sys.argv[1]
except IndexError:
    print("Pas de fichier fourni.")
    exit(1)

def analyze(file_name: str) -> None:
    try:
        with open(file_name) as file:
            file_content = file.read()
    except IOError:
        print(f"Le fichier '{file_name}' n'a pas été trouvé.")
        exit(1)

    nombre_de_lignes = len(file_content.split('\n'))
    nombre_de_characteres = len(file_content)
    nombre_de_mots = len(file_content.split())
    mots_uniques = len(set(file_content.split()))
    nombre_de_majuscules = len([char for char in file_content if char.isupper()])

    print(f"Nombre de lignes : {nombre_de_lignes}")
    print(f"Nombre de charactères : {nombre_de_characteres}")
    print(f"Nombre de mots : {nombre_de_mots}")
    print(f"Nombre de mots uniques : {mots_uniques}")
    print(f"Nombre de majuscules : {nombre_de_majuscules}")

analyze(file_name)