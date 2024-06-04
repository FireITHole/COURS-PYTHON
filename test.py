PATH = "path/to/test.txt"

""" # Lecture dans un fichier
with open(PATH, encoding="UTF-8") as file:
    print(file.readlines())

# Ecriture dans un fichier (attention destruction du contenu)
with open(PATH, "w") as file:
    file.write("coucou")

# Append dans un fichier
with open(PATH, "a", encoding="UTF-8") as file:
    file.write('\n'.join(["Coucou!", "Comment ça va ?"]))
 """

from os import path as ospath


def get_nom_fichier(path: str) -> str:
    path_uniform = path.replace('\\', '/')
    fichier = path_uniform.split('/')[-1]
    resultat = fichier.split('.')[0]
    return resultat

def get_arborescence(path: str, nom_fichier: str) -> str:
    path_uniform = path.replace('\\', '/')
    arbo = path_uniform.split('/')[:-1]
    nouvelle_arbo = ospath.join(*arbo, nom_fichier)
    return nouvelle_arbo

def ecrit_list_str_file(path: str) -> None:
    nouvelles_lignes: list[str] = []

    with open(path, encoding="UTF-8") as file:
        lignes = file.readlines()

    for ligne in lignes:
        new_ligne = ""
        for car in ligne:
            if car.lower() not in "aeiouy":
                new_ligne += car
        nouvelles_lignes.append(new_ligne)

    nouveau_nom_fichier = get_nom_fichier(path) + "_filtre.txt"
    nouveau_fichier = get_arborescence(path, nouveau_nom_fichier)
    
    with open(nouveau_fichier, "+w", encoding="UTF-8") as file:
        file.writelines(nouvelles_lignes)

ecrit_list_str_file(PATH)