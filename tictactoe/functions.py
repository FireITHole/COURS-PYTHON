class CaseDejaRemplie(Exception):
    def __init__(self) -> None:
        self.message = "La case est déjà occupée !"
        super().__init__(self.message)


class PartieEncoreEnCours(Exception):
    def __init__(self) -> None:
        self.message = "Aucun vainqueur pour le moment, la partie est encore en cours."
        super().__init__(self.message)

class Player:
    """Classe permettant de tenir compte des points des joueurs au fur et à mesure des parties"""
    def __init__(self, name: str) -> None:
        self.__name: str = name
        self.__points = 0

    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def points(self) -> str:
        return self.__points
    
    def __add__(self, points: int) -> int:
        if not isinstance(points, int):
            raise TypeError("Le nombre de points ajoutés doit être un entier")
        
        self.__points += points


class TicTacToe:
    """Jeu du Tic Tac Toe
\nMéthodes publiques :
- jouer (permet de jouer un coup, le coup sera jouer pour le joueur correspondant au tour actuel)
\nPropriétés :
- vainqueur (Renvoi le nom du joueur gagnant s'il y en a un, sinon renvoie une Exception 'PartieEncoreEnCours')
- prochain_joueur (Renvoi le nom du joueur qui doit jouer le coup actuel)
\nExceptions :
- CaseDejaRemplie (Invoquée quand un joueur essaye de remplir une case déjà remplie)
- PartieEncoreEnCours (Invoquée quand la propriété 'vainqueur' est accédée mais qu'il n'y a pas encore de vainqueur)
    """
    SYMBOLES: str = "X", "O"
    SYMBOLE_VIDE: str = " "

    def __init__(self, player_1: Player, player_2: Player) -> None:
        self.__grille: list[list[str]] = [[self.SYMBOLE_VIDE for _ in range(3)] for _ in range(3)]
        self.__players: tuple[Player] = player_1, player_2
        self.__vainqueur: Player | None = None
        self.__etat = 0
        self.__turn = 0

    def _verifinputgrille(f):
        """Décorateur de vérification des entrées du joueur au moment de jouer"""
        def wrapper(*args):
            if not all([isinstance(x, int) for x in args[1:]]):
                raise TypeError("Les coordonnées doivent-être des entiers")

            if not all([3 > x >= 0 for x in args[1:]]):
                raise IndexError(
                    "Les coordonées ne sont pas dans les limites de la grille de jeu."
                )

            if args[0].__grille[args[1]][args[2]] != args[0].SYMBOLE_VIDE:
                raise CaseDejaRemplie

            return f(*args)

        return wrapper

    def __repr__(self) -> str:
        data_lines: list[str] = ["  " + "  |  ".join(cell for cell in ligne) + "  " for ligne in self.__grille]
        empty_line = "\n-----|-----|-----\n"
        return "\n" + empty_line.join(data_lines) + "\n"

    @property
    def prochain_joueur(self) -> str:
        """Renvoi le nom du joueur qui doit jouer le coup actuel"""
        return self.__players[self.__turn % 2].name
    
    @property
    def etat(self) -> int:
        """Renvoi l'état de la partie en cours :
- 0 (la partie n'est pas terminée)
- 1 (la partie est gagnée)
- 2 (la partie est PAT)"""
        return self.__etat

    @property
    def vainqueur(self) -> str:
        """Renvoi le nom du vainqueur si la partie est gagnée, sinon invoque l'exception 'PartieEncoreEnCours'"""
        if not self.__vainqueur:
            raise PartieEncoreEnCours

        return self.__vainqueur.name

    def _check_etat_partie(self) -> None:
        """Change la valeur de l'état de la partie en cours :
        - 0 si la partie n'est pas terminée
        - 1 si il y a un gagnant
        - 2 si la partie est PAT
        """
        for ligne in self.__grille:
            if all(cell == self.SYMBOLES[self.__turn % 2] for cell in ligne):
                self.__vainqueur = self.__players[self.__turn % 2]
                self.__vainqueur + 1
                self.__etat = 1
                return
            
        colonnes: list[list[str]] = [[ligne[col_i] for ligne in self.__grille] for col_i in range(len(self.__grille))]
        for colonne in colonnes:
            if all(cell == self.SYMBOLES[self.__turn % 2] for cell in colonne):
                self.__vainqueur = self.__players[self.__turn % 2]
                self.__vainqueur + 1
                self.__etat = 1
                return
            
        diags: list[list[str]] = [[self.__grille[x][x] for x in range(len(self.__grille))], [self.__grille[x][y] for x, y in zip(range(len(self.__grille)), range(len(self.__grille) - 1, -1, -1))]]
        for diag in diags:
            if all(cell == self.SYMBOLES[self.__turn % 2] for cell in diag):
                self.__vainqueur = self.__players[self.__turn % 2]
                self.__vainqueur + 1
                self.__etat = 1
                return
            
        if self.__turn == len(self.__grille) ** 2 - 1:
            self.__etat = 2
            return
            
        self.__etat = 0

    @_verifinputgrille
    def jouer(self, x: int, y: int) -> None:
        """Permet de joueur un coup. Le coup sera automatiquement attribué au joueur correspondant au tour actuel"""
        self.__grille[x][y] = self.SYMBOLES[self.__turn % 2]
        print(f"{self.__players[self.__turn % 2].name} vient de jouer :\n{self}")
        self._check_etat_partie()
        self.__turn += 1
    
    def __bool__(self) -> bool:
        """Renvoi l'état de la partie en cours :
        - False si la partie n'est pas terminée
        - True si la partie est gagnée ou est PAT
        """
        return True if self.__etat else False
    
    def __eq__(self, etat: int | bool) -> bool:
        """Compare l'état de la partie à un entier ou un boolean"""
        if not isinstance(etat, bool) and not isinstance(etat, int):
            raise TypeError("La valeur de l'état doit être un entier ou un boolean")

        if isinstance(etat, bool):
            return True if self.__etat else False
        
        if isinstance(etat, int):
            if not 0 <= etat <= 2:
                raise ValueError("L'état ne peut avoir que 0, 1 ou 2 comme valeur")
            
            return self.__etat == etat


if __name__ == "__main__":
    from os import name as os_name, system

    def clear_screen() -> None:
        if os_name == 'nt':
            system("cls")
        else:
            system('clear')

    def jouer_partie(player_1: Player, player_2: Player) -> None:
        jeu = TicTacToe(player_1, player_2)
        
        clear_screen()
        print("Que la partie commence !")
        print(jeu)

        while not jeu:
            try:
                coup: list[int] = map(lambda x: int(x), input(f"Que veux-tu jouer {jeu.prochain_joueur} ? (ligne, colonne) : ").replace(' ', '').split(","))
                clear_screen()
                jeu.jouer(*coup)
            except Exception as error:
                clear_screen()
                print(f"Attention : {error}")
                print(jeu)
                continue
        
        if jeu == 1: # "if jeu.etat == 1:" fonctionne également
            print(f"{jeu.vainqueur} a gagné !")
        else:
            print("PAT !")
        
        center_text = lambda text, long: ((long - len(text)) // 2) * " " + text + ((long - len(text)) // 2) * " "
        scores = f"{player_1.name} | {player_2.name}"
        scores_points = f"{center_text(str(player_1.points), len(player_1.name) + 1)}   {center_text(str(player_2.points), len(player_2.name) + 1)}"
        scores = f"\n{'-' * len(scores)}\n{scores}\n{scores_points}\n{'-' * len(scores)}"
        print(scores)

        choix = input("\nQue faire ? (r : recommencer, q : quitter) : ")
        if choix != 'r':
            clear_screen()
            print('A bientôt !')
            exit(0)
    
        del jeu
        jouer_partie(player_1, player_2)

    def main() -> None:
        clear_screen()
        bienvenue_msg = "Bienvenue au jeu du Tic Tac Toe !"
        bienvenue_msg = f"{"-"*len(bienvenue_msg)}\n{bienvenue_msg}\n{"-"*len(bienvenue_msg)}"
        print(bienvenue_msg)

        player_1: Player = Player(input("\nQuels sont les noms des joueurs ?\nJoueur 1 : "))
        player_2: Player = Player(input("Joueur 2 : "))

        jouer_partie(player_1, player_2)
    
    main()