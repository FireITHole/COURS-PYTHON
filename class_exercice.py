# Gestionnaire de Bibliothèque :
# Objectif : Créez une application de gestion de bibliothèque permettant d'ajouter des livres, de les afficher, et de marquer s'ils sont empruntés ou non.

# Exigences :
    # Livre :
        # Définissez une classe Livre avec les attributs : titre, auteur, et emprunté (booléen).
    # Bibliothèque :
        # Créez une classe Bibliotheque qui peut contenir plusieurs livres. La bibliothèque doit avoir des méthodes pour ajouter un livre, afficher tous les livres, et marquer un livre comme emprunté ou non.

class Livre:
    def __init__(self, titre: str, auteur: str, emprunte = False):
        self.titre = titre
        self.auteur = auteur
        self.emprunte = emprunte

    def __repr__(self) -> str:
        return f"Voici le livre {self.titre} de l'auteur {self.auteur}. Il est actuellement {'pas ' if not self.emprunte else ''}emprunté."
    
    def get_titre(self) -> str:
        return self.titre
    
    def get_auteur(self) -> str:
        return self.auteur
    
    def est_emprunte(self) -> bool:
        return self.emprunte
    
    def toggle_emprunte(self) -> None:
        self.emprunte = not self.emprunte
    
    def get_tout(self) -> dict:
        return {"titre": self.titre, "auteur": self.auteur, "emprunte": self.emprunte}
    

class Bibliotheque:
    def __init__(self, nom: str):
        self.nom = nom
        self.livres: list[Livre] = []

    def ajouter_livre(self, livre: Livre) -> None:
        self.livres.append(livre)
        print(f"Le livre {livre.get_titre()} a été ajouté à la bibliothèque {self.nom}.")

    def emprunter_livre(self, livre: Livre) -> None:
        if livre not in self.livres or livre.est_emprunte():
            print(f"Le livre {livre.get_titre()} n'est pas disponible dans la biliothèque {self.nom} ou il est déjà emprunté")
            return
        
        livre.toggle_emprunte()
        print(f"Le livre {livre.get_titre()} a été emprunté.")
        
    def rendre_livre(self, livre: Livre) -> None:
        if livre not in self.livres or not livre.est_emprunte():
            print(f"Le livre {livre.get_titre()} n'est pas disponible dans la biliothèque {self.nom} ou il n'est pas emprunté")
            return
        
        livre.toggle_emprunte()
        print(f"Le livre {livre.get_titre()} a été rendu.")

    def get_livres(self) -> list[Livre]:
        return self.livres
        
    def __repr__(self) -> str:
    #   Méthode standard
    #     livres = []
    #     for livre in self.livres:
    #         livres.append(f"   - {livre.get_titre()} de {livre.get_auteur()} ({'emprunté' if livre.est_emprunte() else 'disponible'})")
    #     livres_str = "\n".join(livres)
        livres_str = "\n".join([f"   - {livre.get_titre()} de {livre.get_auteur()} ({'emprunté' if livre.est_emprunte() else 'disponible'})" for livre in self.livres])
        return f"Voici les livres de notre bibliothèque {self.nom} : \n{livres_str}"


""" bibliotheque = Bibliotheque("Maison")


while True:
    choix = input("Ajouter ou voir les livres (a/v) : ")

    match choix:
        case "a":
            titre = input("Titre : ")
            auteur = input("Auteur : ")
            livre = Livre(titre, auteur)
            bibliotheque.ajouter_livre(livre)
        case "v":
            print(bibliotheque) """

if __name__ == "__main__":
    liste_livre: list[Livre] = []
    
    while True:
        choix = input("Ajouter ou voir les livres (a/v) : ")

        match choix:
            case "a":
                titre = input("Titre : ")
                auteur = input("Auteur : ")
                liste_livre.append(Livre(titre, auteur))
            case "v":
                for livre in liste_livre:
                    print(livre.get_titre())
    """
    harry_potter_1 = Livre("Harry Potter 1", "J.K.R")
    seigneur_des_anneaux = Livre("Le seigneur des anneaux", "Tolkien")
    
     print(harry_potter_1)
    print(seigneur_des_anneaux)
    biblio = Bibliotheque("Malraux")
    biblio.ajouter_livre(harry_potter_1)
    biblio.ajouter_livre(seigneur_des_anneaux)
    biblio.emprunter_livre(harry_potter_1)
    print(harry_potter_1)
    print(biblio) """