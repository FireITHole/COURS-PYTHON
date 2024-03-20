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
print(acdc._albums)