from datetime import date

class Titre():
    def __init__(self, nom: str, duree_secondes: int, album: "Album") -> None:
        self.nom = nom
        self.duree_secondes = duree_secondes
        self.album = album

    def __repr__(self) -> str:
        pass


class Album():
    def __init__(self, nom: str, release_date: date, titres: list[Titre], artist: "Artist") -> None:
        self.nom = nom
        self.release_date = release_date
        self.titres = titres
        self.artist = artist

    def __repr__(self) -> str:
        pass

class Artist():
    def __init__(self, nom: str, type: str, origine: str, date_naissance: date, genre_musical: str) -> None:
        self.nom = nom
