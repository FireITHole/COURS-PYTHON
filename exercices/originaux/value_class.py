class Parent:
    Y = 70
    W = 100


class Parent2:
    Y = 50


class Personne(Parent, Parent2):
    W = 80

    def __init__(self, nom: str, poid: float) -> None:
        self.nom = nom
        self.poid = poid


antoine = Personne("antoine", 90)
print(antoine.W)  # 80
print(Personne.Y)  # 70
print(antoine.poid)  # 90
print(Personne.W)  # 80
print(Personne.poid)  # ERREUR
