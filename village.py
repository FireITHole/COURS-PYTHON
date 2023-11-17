# Créer une classe Personne qui a pour attributs :
# Un nom
# Un prénom
# Une date de naissance
# Un quotat d'énergie

# Créer des fonctions en rapport avec l'énergie :
# manger -> gagner de l'énergie
# nager -> dépenser de l'énergie

# print manger -> "La personne {prenom} a mangé ! Elle a maintenant {energie} énergies."

from datetime import date


class Personne():
    def __init__(
        self, nom: str, prenom: str, date_de_naissance: date, energie=1000
    ) -> None:
        self.nom = nom
        self.prenom = prenom
        self.date_de_naissance = date_de_naissance
        self.energie = energie

    def __repr__(self) -> str:
        return f"Info sur la personne {self.prenom} :\n\
    - Nom : {self.nom}\n\
    - Prénom : {self.prenom}\n\
    - Date de naissance : {self.date_de_naissance.strftime('%d/%m/%Y')}\n\
    - Âge : {int((date.today() - self.date_de_naissance).days // 365.25)}\n\
    - Énergie : {self.energie}"

    def manger(self):
        self.energie = self.energie + 50
        print(
            f"La personne {self.prenom} a mangé ! Elle a maintenant {self.energie} énergies."
        )

    def nager(self):
        self.energie = self.energie - 50
        print(
            f"La personne {self.prenom} a nagé ! Elle a maintenant {self.energie} énergies."
        )


antoine = Personne("arnoux", "antoine", date(2002, 6, 11))
antoine.manger()
antoine.nager()
print(antoine)
