PATH = "test.txt"

# Lecture dans un fichier
with open(PATH, encoding="UTF-8") as file:
    print(file.readlines())

# Ecriture dans un fichier (attention destruction du contenu)
with open(PATH, "w") as file:
    file.write("coucou")

# Append dans un fichier
with open(PATH, "a", encoding="UTF-8") as file:
    file.write('\n'.join(["Coucou!", "Comment ça va ?"]))



def ecrit_list_str_file(lignes: list[str]) -> None:
    nouvelles_lignes: list[str] = []

    for ligne in lignes:
        nouvelles_lignes.append(f"{ligne} ({len(ligne)})")

    # nouvelles_lignes: list[str] = [f"{ligne} ({len(ligne)})" for ligne in lignes]

    with open(PATH, "+w", encoding="UTF-8") as file:
        file.write('\n'.join(nouvelles_lignes))

PHRASES = ["Bonjour", "comment", "ça", "va ?", "qkjsdhjjkqshdjkhqsjkdhqjkshdkjqshsjkh"]

ecrit_list_str_file(PHRASES)