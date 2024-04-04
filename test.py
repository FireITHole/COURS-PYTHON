class Moteur:
    def __init__(self, nb_cylindres: int, puissance: int, nom: str, voitures: list["Voiture"] = []) -> None:
        self._nb_cylindres = nb_cylindres
        self._puissance = puissance
        self._nom = nom
        self._voitures = voitures

    def __repr__(self) -> str:
        return f"[Nom : {self._nom}, Nb cylindres : {self._nb_cylindres}, Voitures : {" - ".join([voiture.modele for voiture in self._voitures])}]"
    
    def ajouter_voiture(self, voiture: "Voiture") -> None:
        if voiture not in self._voitures:
            self._voitures.append(voiture)

class Voiture:
    def __init__(self, nom: str, marque: str, modele: str, annee: int, kms: int, moteur: Moteur) -> None:
        self._nom = nom
        self._marque = marque
        self._modele = modele
        self._annee = annee
        self._kms = kms
        self._moteur = moteur
        self._moteur.ajouter_voiture(self)

    def __repr__(self) -> str:
        return f"Nom : {self._nom}, Année : {self._annee}, Moteur : {self._moteur}"
    
    @property
    def modele(self) -> str:
        return self._modele.upper() 

if __name__ == "__main__":
    moteur_1 = Moteur(12, 300, "Ford Kent X-Flow")
    voiture_1 = Voiture("Titine", "Caterham", "Super 7", 1988, 50000, moteur_1)
    voiture_2 = Voiture("Titinette", "Caterham2", "Super 8", 1989, 50001, moteur_1)
#print(voiture_1)


# Héritage

""" 
class OutOfEnergyError(Exception):
    def __init__(self, message) -> None:
        self.message = message
        super().__init__(self.message)


class Animale:
    def __init__(self, nom: str, nbr_pattes: int, domestique: bool, energie = 100) -> None:
        self._nom = nom
        self._nbr_pattes = nbr_pattes
        self._domestique = domestique
        self._energie = energie

    @property
    def nom(self):
        return self._nom
    
    @nom.setter
    def nom(self, nouveau_nom: str):
        if not isinstance(nouveau_nom, str):
            raise TypeError
        
        if len(nouveau_nom) > 20:
            raise ValueError("Le nom est trop long")
        
        self._nom = nouveau_nom
        

    def run(self) -> int:
        if self._energie <= 10:
            raise OutOfEnergyError(f"{self._nom} n'a plus assez d'energie pour courir.")

        self._energie -= 10
        return self._energie
    
    def eat(self) -> int:
        self._energie += 15
        return self._energie
    
    def __repr__(self) -> str:
        return f"{self._nom} a {self._energie} d'énergie."


class Vache(Animale):
    def __init__(self, nom: str) -> None:
        super().__init__(nom, 4, False, 200)

class Chien(Animale):
    def __init__(self, nom: str) -> None:
        super().__init__(nom, 4, True)

class Chat(Animale):
    def __init__(self, nom: str) -> None:
        super().__init__(nom, 4, True, 50)

    def sleep(self) -> int:
        self._energie += 20
        return self._energie
    
cow = Vache("Marie")
dog = Chien("Sunny")
cat = Chat("Charli")

cow.eat()
cow.run()
cow.eat()
cow.run()
cow.run()
cow.run()
cow.run()
cow.nom = "qskld"
print(cow)
cat.run()
cat.run()
cat.run()
print(cat)



#

class Titre:
    def __init__(self, nom: str, artiste: "Artiste", album: "Album") -> None:
        self._nom = nom
        self._artiste = artiste
        self._album = album
        self._artiste.ajouter_titre(self)
        self._album.ajouter_titre(self)

    def __repr__(self) -> str:
        return self._nom

class Album:
    def __init__(self, titre: str, artiste: "Artiste") -> None:
        self._titre = titre
        self._artiste = artiste
        self._artiste.ajouter_album(self)
        self._titres: list[Titre] = []

    def ajouter_titre(self, titre: Titre) -> None:
        self._titres.append(titre)

    def __repr__(self) -> str:
        return self._titre


class Artiste:
    def __init__(self, titre: str) -> None:
        self._titre = titre
        self._albums: list[Album] = []
        self._titres:list[Titre] = []

    def ajouter_album(self, album: Album) -> None:
        self._albums.append(album)

    def ajouter_titre(self, titre: Titre) -> None:
        self._titres.append(titre)

    def __repr__(self) -> str:
        return self._titre

acdc = Artiste("ACDC")
hth = Album("Highway To Hell", acdc)
hellsbells = Titre("Hell's Bells", acdc, hth)

print(hellsbells._album)
print(hellsbells._artiste)
print(acdc._titres)
print(acdc._albums) """