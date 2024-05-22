def fonction_tres_importante(prenom: str, age: int, nom = "Antoine") -> str | None:
    """Cette fonction est utilisé à titre d'exemple !"""
    if age < 10:
        return f"{nom}, {prenom}, {age + 1}"
    else:
        return None

#print(fonction_tres_importante('A"B', 9))







