# Gestionnaire de Mediathèque d'albums musicaux :
# Objectif : Créez une application Médiathèque permettant d'ajouter des Artistes, des Albums, des titres de les afficher, et de marquer s'ils sont empruntés ou non.
# lister les artistes, les albums, les titres

# Création des classes Titre, Album, Artiste et Propriétaire
# classe proprietaire = moi mais j'ai besoin d'une classe racine qui liste les instance de la classe Artiste
# classe artiste qui liste les instances de la classe Album
# classre album qui liste les instances de la classe Titre
# et enfin classe Titre

from liste_musique import titres


class Titre:
    # création des instances titres
    # count_titre = 0  # c'est une valeur de classe qui permet de compter le nombre de titre à travers toutes les instances titre
    TITRES: list["Titre"] = []

    def __init__(self, titre: str):
        self._titre = (
            titre.capitalize()
        )  # je formate les titres en premiere lettre majuscule le reste en minuscule
        # Titre.count_titre += 1
        Titre.TITRES.append(self)

    def __repr__(
        self,
    ) -> str:  # c'est ce que renvoi l'instance comme information / format
        return f"\n     - Titre {self._titre}"

    @property
    def titre(self) -> str:
        return self._titre

    """ def get_titre(self) -> str:
        return self.titre """

    # def get_plage(self) -> str: # la notion de plage n'est pas utiisée
    #     return self.plage


class Album:
    # création des instances album qui contiennent chacune la liste des instances titres de l'album
    ALBUMS: list["Album"] = (
        []
    )  # Une façon de lister les noms des Album "sans derouler via l'OO"
    # count_albums = 0  # on compte les instances album

    def __init__(self, titre_album: str):
        self._titre_album = (
            titre_album.capitalize()
        )  # On fdormate les albums premiere lettre en captiale
        self._titres: list[Titre] = (
            []
        )  # Album contient la liste des titres ??A revoir la formulation self titres: pas tout compris ??????????
        Album.ALBUMS.append(
            self
        )  # J'ajoute l'album à la liste de la classe Album.liste_globale_album
        # Album.count_albums += 1  # on compte les instances de la classe Album pour avoir le nombre d'albums

    def ajouter_titre(self, titre: Titre) -> None:
        self._titres.append(
            titre
        )  # ajout d'une instance titre à la liste de l'instance album
        print(f"Le titre {titre.titre} a été ajouté à l'album {self._titre_album}.")

    @property
    def titre_album(self) -> str:
        return self._titre_album

    def __repr__(self) -> str:
        titres_str = "\n".join([f"   - {titre.titre}" for titre in self._titres])
        return f"Voici les titres de l'album {self._titre_album} : \n{titres_str}"


class Artiste:
    ARTISTES: list["Artiste"] = []

    # création des instances artistes qui contiennent chacune la liste des instances album de l'artiste
    def __init__(self, nom_artiste: str):  # le constructeur
        self._nom_artiste = nom_artiste.title()
        self._albums: list[Album] = []
        Artiste.ARTISTES.append(self)

    def ajouter_album(self, album: Album) -> None:
        self._albums.append(album)
        print(f"L'album {album.titre_album} a été ajouté à l'artiste {self._nom_artiste}.")

    def lister_album(self) -> str:
        for album in self._albums:
            print(album)

    @property
    def nom_artiste(self) -> str:
        return self._nom_artiste

    def __repr__(self) -> str:
        album_str = "\n".join([f"   - {album.titre_album} " for album in self._albums])
        return f"\n Voici les albums de l'artiste {self._nom_artiste} : \n{album_str}"


class Bibliotheque:
    # creation de l'instance unique propriétaire 'moi' qui contient la liste des instances de tous les artistes
    def __init__(self, nom: str):
        self._nom = nom
        self.artistes: list[Artiste] = []

    def ajouter_artiste(self, artiste: Artiste) -> None:
        self.artistes.append(artiste)
        print(f"L'artiste {artiste.get_artiste()} a été ajouté à ma bibliothèque")

    def get_artiste(self) -> str:
        return self.artistes

    def checkandadd_artiste(self, nom_artiste) -> str:
        if len(self.artistes) == 0:  # je regarde si la liste est vide
            tag = False  # existe pas falg =False

        for item in self.artistes:  # je parcours les artistes
            if nom_artiste.title() in item.artiste:
                recupitem = item  # si l'objet artiste existe déja le falg est à True on récupère l'objet artiste correspondant
                tag = True
                break

            else:
                tag = False

        if tag == True:
            return recupitem  # si l'objet existe déja on l'affecte à artistobj

        else:
            # si l'artiste n'est pas dans la liste on créé l'objet et on l'ajoute dans la liste
            artistobj = Artiste(nom_artiste.title())
            #   /!\ Ajouter l'objet artistobj dans la liste artistes de l'objet propobj /!\
            self.ajouter_artiste(artistobj)
            print(f"l'artiste {nom_artiste} a été créé ")

            return artistobj

    def liste_artiste(self) -> str:
        count = 0
        liste_artistes = []
        for artiste in self.artistes:
            liste_artistes.append(artiste.artiste)
        list.sort(liste_artistes)
        print(liste_artistes)

    # lister les albums d'un artiste
    def liste_album_artiste(self) -> str:
        count = 0
        nom_artiste = input("Entrez le nom de l'artiste: ")
        for artiste in self.artistes:
            print(artiste.artiste, nom_artiste.title())
            if artiste.artiste == nom_artiste.title():
                tag = True
                break
            else:
                tag = False
        if tag == False:
            print("Artiste inconnu !!")
        else:
            print(artiste.albums)

    def __repr__(self) -> str:
        # je liste les instances artiste et pour chaque instance je recupère ls variables de l'instance artiste nom et liste album
        artiste_str = "\n".join(
            [f"   - {artiste.get_artiste()} " for artiste in self.artistes]
        )
        return f"Voici liste des aristes de ma biblothèque : \n{artiste_str}"


# INTEGRATION DE LA LISTE DES MUSIQUES DE MA BILBLIOTHEQUE VIA LE FICHIER LISTE.TXT
# la fonction "import_fichier_music" importe et fait le ménage dans la liste.txt et renvoi dans une liste
#


# INTEGRATION DE LA LISTE TITRES DANS LES INSTANCES
# je traite à présent cette nouvelle liste pour identifier les albums et les titres
# count_album = 0
# count_titre = 0
nom_album = ""
propobj = Proprietaire()  # il n'y a qu'un seul objet proprietaire


# On parcours les lignes de titres pour identifier les lignes album, artiste et titres
for items in titres:
    # print(items)
    # 1 ) identification d'un album et création de l'instance
    if "Music Recorder" in items:
        nom_album = items.replace(
            "Music Recorder\\music\\", ""
        )  # pour avoir que le nom de l'album je prends le nom et supprime le chemin
        nom_album = nom_album.replace("\n", "")

        # /!\ création de l'objet Album albumobj /!\
        albumobj = Album(nom_album)  # OOOO création d'un objet Album
        print("\n ____Nom de l'album_____", nom_album)
        continue

    # 2 ) identification de l'artiste verification si l'artiste existe déja ou pas (checkandadd) ajout de l'album à la liste de l'instance artiste

    if "<<artiste>>" in items:  # identification de l'artiste
        nom_artiste = items[13:]

        # appele à la méthode pour vérifier l'existance de l'artiste dans la liste et le créer le cas echeant sil n'existe pas
        artistobj = propobj.checkandadd_artiste(nom_artiste)

        #   /!\ Ajouter l'objet albumobj dans la liste albums de l'objet artistobj /!\
        artistobj.ajouter_album(albumobj)  # ajout de l'objet album à l'artiste
        continue

    # 3) ajout des titres dans l'album

    # identification des titres
    #    /!\ Création d'un objet Titre (une ligne) titreobj /!\
    #    /!\ Intégration de l'objet dans la liste titres de l'objet albumobj /!\
    if items != "":
        titreobj = Titre(items)
        albumobj.ajouter_titre(titreobj)


while True:
    #  MENU
    print(
        f"-------------------Veuillez choisr l'option désirée--------------------------"
    )
    print(
        f"Lister tous les artistes/albums/titres (objet propriétaire)               1   "
    )
    print(
        f"Lister tous les artiste (liste artistes de l'objet propriétaire)          2   "
    )
    print(
        f"Lister tous les albums (variable de classe Album)                         3   "
    )
    print(
        f"Lister tous les albums/titres d'un artiste (print de l'instance artiste)  4   "
    )
    print(
        f"                  Ajouter un album                                        5   "
    )
    print(
        f"                     Statistiques                                         6   "
    )
    print(
        f"               Sortir de l'application                                    9   "
    )
    print(
        f"-----------------------Veuillez choisr l'option désirée----------------------"
    )
    choix = input("=> : ")

    match choix:
        case "1":
            print("voici la liste de tous les artistes, album et titres")
            print(propobj)

        case "2":
            print("voici la liste des artistes")
            propobj.liste_artiste()

        case "3":
            print(Album.liste_globale_album)

        case "4":
            propobj.liste_album_artiste()

        case "5":

            #   /!\ Check si l'artiste existe ou s'il faut le créer, récupère l'objet artiste
            #   /!\ le mets dans la liste des artistes
            nom_artiste = input("Entrez le nom d'un artiste : ")  #
            artistobj = propobj.checkandadd_artiste(nom_artiste.title())

            #   /!\ Ajouter l'objet albumobj dans la liste albums de l'objet artistobj /!\
            nom_album = input("Entrez le nom de l'album : ")
            albumobj = Album(nom_album)  # OOOO création d'un objet Album
            artistobj.ajouter_album(albumobj)  # ajout de l'objet album à l'artiste

            #   /!\ Ajoute les titres à l'album
            while True:
                nom_titre = input("Entrez le titre ou x pour arréter : ")
                if nom_titre.lower() == "x":
                    break
                titreobj = Titre(nom_titre)
                albumobj.ajouter_titre(titreobj)

        case "6":
            print(f"Il y a {len(propobj.artistes)} artistes dans la base")
            print(f"Il y a {Album.count_albums} albums dans la base")
            print(f"Il y a {Titre.count_titre} titres dans la base")

        case "9":
            break
