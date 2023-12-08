requete = "test"

if len(requete) == 4:
    if requete[0] == "t":
        if requete[-1] == "t":
            print("ok")

if len(requete) != 4:
    exit(1)

if requete[0] != "t":
    exit(1)

if requete[-1] != "t":
    exit(1)

print("ok")