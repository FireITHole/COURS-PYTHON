from random import randint, sample
from os import path, makedirs
from time import time
import sys
from datetime import timedelta
from ast import literal_eval
import matplotlib.pyplot as plt

class Cellule:
    show_resolve = True

    def __init__(self, id: int, parent: "Cellule" = None) -> None:
        self._north = True
        self._east = True
        self._south = True
        self._west = True
        self._visited = False
        self._n_cell = None
        self._e_cell = None
        self._s_cell = None
        self._w_cell = None
        self._traverse: str = ""
        self._id: int = id
        self._deep_id: int = id
        self._g_cost = 0
        self._h_cost = 0
        self._f_cost = 0
        self._parent: "Cellule" | None = parent

    @property
    def visited(self) -> bool:
        return self._visited
    
    @visited.setter
    def visited(self, new_value: bool) -> None:
        if not isinstance(new_value, bool):
            raise TypeError

        self._visited = new_value

    @property
    def g_cost(self) -> int:
        return self._g_cost
    
    @g_cost.setter
    def g_cost(self, new_cost: int):
        if not isinstance(new_cost, int):
            raise TypeError
        
        self._g_cost = new_cost
    
    @property
    def h_cost(self) -> int:
        return self._h_cost
    
    @h_cost.setter
    def h_cost(self, new_cost: int):
        if not isinstance(new_cost, int):
            raise TypeError
        
        self._h_cost = new_cost

    @property
    def f_cost(self) -> int:
        return self._f_cost
    
    @f_cost.setter
    def f_cost(self, new_cost: int):
        if not isinstance(new_cost, int):
            raise TypeError
        
        self._f_cost = new_cost

    @property
    def parent(self) -> "Cellule":
        return self._parent
    
    @parent.setter
    def parent(self, new_parent: "Cellule"):
        if not isinstance(new_parent, Cellule):
            raise TypeError
        
        self._parent = new_parent
    
    @property
    def id(self) -> int:
        return self._id
    
    @id.setter
    def id(self, new_id: int):
        if not isinstance(new_id, int):
            raise TypeError

        self._id = new_id
    
    @property
    def traverse(self) -> str:
        return self._traverse
    
    @traverse.setter
    def traverse(self, chemin: str):
        if not isinstance(chemin, str):
            raise TypeError
        
        if chemin not in ['h', 'v', "ne", "es", "sw", "wn"]:
            raise ValueError

        self._traverse = chemin

    @property
    def deep_id(self) -> int:
        return self._deep_id

    @property
    def n_cell(self):
        return self._n_cell

    @property
    def e_cell(self):
        return self._e_cell

    @property
    def s_cell(self):
        return self._s_cell

    @property
    def w_cell(self):
        return self._w_cell
    
    @n_cell.setter
    def n_cell(self, cell: "Cellule") -> None:
        if not isinstance(cell, Cellule):
            raise TypeError
        
        self._n_cell = cell
    
    @e_cell.setter
    def e_cell(self, cell: "Cellule") -> None:
        if not isinstance(cell, Cellule):
            raise TypeError
        
        self._e_cell = cell
    
    @s_cell.setter
    def s_cell(self, cell: "Cellule") -> None:
        if not isinstance(cell, Cellule):
            raise TypeError
        
        self._s_cell = cell
    
    @w_cell.setter
    def w_cell(self, cell: "Cellule") -> None:
        if not isinstance(cell, Cellule):
            raise TypeError
        
        self._w_cell = cell
    
    @property
    def north(self) -> bool:
        return self._north

    @property
    def east(self) -> bool:
        return self._east

    @property
    def south(self):
        return self._south

    @property
    def west(self):
        return self._west
    
    @north.setter
    def north(self, etat: bool) -> None:
        if not isinstance(etat, bool):
            raise TypeError
        
        self._north = etat
        
        if self._n_cell:
            self._n_cell._south = etat
    
    @east.setter
    def east(self, etat: bool) -> None:
        if not isinstance(etat, bool):
            raise TypeError
        
        self._east = etat

        if self._e_cell:
            self._e_cell._west = etat
    
    @south.setter
    def south(self, etat: bool) -> None:
        if not isinstance(etat, bool):
            raise TypeError
        
        self._south = etat

        if self._s_cell:
            self._s_cell._north = etat
    
    @west.setter
    def west(self, etat: bool) -> None:
        if not isinstance(etat, bool):
            raise TypeError
        
        self._west = etat

        if self._w_cell:
            self._w_cell._east = etat
    
    def get_cell(self) -> list[list[str]]:
        result = [[*(" "*4)], [*(" " * 4), ""], [*(" "*4), ""]]

        if not self.e_cell and self.east:
            result[1][4], result[2][4] = '|', '|'

        if not self.n_cell and self.north:
            result[0][1:4] = "___"

        if (self.s_cell and self.s_cell.north and self.south) or (not self.s_cell and self.south):
            result[2][1:4] = "___"

        if (self.w_cell and self.w_cell.east and self.west) or (not self.w_cell and self.west):
            result[1][0], result[2][0] = '|', '|'

        if self.show_resolve:
            if self._traverse == 'h':
                result[1][1:4] = "___"
            elif self._traverse == 'v':
                result[1][2], result[2][2] = '|', '|'
            elif self._traverse == "ne":
                result[1][2], result[1][3] = '|', '_'
            elif self._traverse == "es":
                result[1][3], result[2][2] = '_', '|'
            elif self._traverse == "sw":
                result[1][1], result[2][2] = '_', '|'
            elif self._traverse == "wn":
                result[1][1], result[1][2] = '_', '|'


        result[0] = "".join(result[0])
        result[1] = "".join(result[1])
        result[2] = "".join(result[2])
        return result
    
    def __eq__(self, other: "Cellule") -> bool:
        return self._deep_id == other._deep_id

    def __repr__(self) -> str:
        return f"(id: {self._deep_id} | n: {self._north} | e: {self._east} | s: {self._south} | w: {self._west} | n_c: {self._n_cell._deep_id if self._n_cell else None} | e_c: {self._e_cell._deep_id if self._e_cell else None} | s_c: {self._s_cell._deep_id if self._s_cell else None} | w_c: {self._w_cell._deep_id if self._w_cell else None})"


class Labyrinthe:
    def __new__(cls, lignes: int, colonnes: int, grille: list[list[Cellule]] = []):
        if not isinstance(lignes, int) or not isinstance(colonnes, int):
            raise TypeError
        
        if lignes < 3 or colonnes < 3:
            raise ValueError("Le nombre de lignes ou de colonnes ne peut pas être inférieur à 3")
        
        if not isinstance(grille, list):
            raise TypeError

        return super().__new__(cls)

    def __init__(self, lignes: int, colonnes: int, grille: list[list[Cellule]] = []) -> None:
        self.__lignes: int = lignes
        self.__colonnes: int = colonnes
        self.__scrumbled = False
        self.__resolved = False
        self.__show_resolve = True
        self.__path: list[int] = []

        if not len(grille):
            self.__grille: list[list[Cellule]] = [[Cellule(i_ligne * self.__colonnes + i_colonne) for i_colonne in range(self.__colonnes)] for i_ligne in range(self.__lignes)]
            
            for i_ligne, ligne in enumerate(self.__grille):
                for i_colonne, cell in enumerate(ligne):
                    if i_ligne != 0:
                        cell.n_cell = self.__grille[i_ligne - 1][i_colonne]

                    if i_ligne != self.__lignes - 1:
                        cell.s_cell = self.__grille[i_ligne + 1][i_colonne]

                    if i_colonne != 0:
                        cell.w_cell = ligne[i_colonne - 1]

                    if i_colonne != self.__colonnes - 1:
                        cell.e_cell = ligne[i_colonne + 1]
        else:
            self.__grille = grille
            self.__scrumbled = True

    @classmethod
    def fusion(cls, lignes: int, colonnes: int):
        new_cls = cls(lignes, colonnes)
        new_cls._fusion()
        return new_cls
    
    @classmethod
    def exploration(cls, lignes: int, colonnes: int):
        new_cls = cls(lignes, colonnes)
        new_cls._exhaustive()
        return new_cls


    def __repr__(self) -> str:
        result = []
        for ligne in self.__grille:
            result_ligne = [[], [], []]
            for cell in [cell.get_cell() for cell in ligne]:
                for x in range(3):
                    result_ligne[x].append(cell[x])
            result.append("\n".join("".join(line) for i_line, line in enumerate(result_ligne) if not all(x == " " for x in "".join(line)) or i_line == 1))

        return "\n".join(result) + '\n'
    
    @property
    def show_resolve(self) -> bool:
        return self.__show_resolve
    
    @show_resolve.setter
    def show_resolve(self, etat: bool) -> None:
        if not isinstance(etat, bool):
            raise TypeError
        

        self.__show_resolve = etat
        
        if self.__resolved:
            Cellule.show_resolve = etat


    def _timit(f):
        def wrapper(*args, **kwargs):
            debut = time()
            result = f(*args, **kwargs)
            fin = time()
            print(f"Temps d'execution de '{f.__name__}' : {timedelta(seconds = fin - debut)}")
            return result
        return wrapper
    
    @staticmethod
    def _progress_bar(percent: float, nb_iter_per_sec: int, nb_iters_left: int) -> None:
        bar_length = 50
        if nb_iter_per_sec:
            sys.stdout.write("\033[F") # Monte le curseur
            sys.stdout.flush()
            sys.stdout.write("\rCompleted: [{:{}}] {:>3}%\n({} restant | {:,} ouvertures/s | {:,} ouvertures restantes){}".format('=' * int(percent/(100.0/bar_length)), bar_length, int(percent), timedelta(seconds=round(nb_iters_left / nb_iter_per_sec)), nb_iter_per_sec, nb_iters_left, ' ' * 5))
            sys.stdout.flush()
        else:
            sys.stdout.write("\rCompleted: [{:{}}] {:>3}%".format('=' * int(percent/(100.0/bar_length)), bar_length, int(percent)))
            sys.stdout.flush()


    @_timit
    def _fusion(self) -> None:
        compteur = 0
        time_last_iter = time()
        nb_iter_last = 0
        nb_iter = 0
        already_seen_cells: list[Cellule] = []
        available_cells: list[Cellule] = [cell for ligne in self.__grille for cell in ligne]

        while compteur < self.__lignes * self.__colonnes - 1:
            if self.__lignes * self.__colonnes - 1 >= 2499:
                self._progress_bar(100.0 * compteur / (self.__lignes * self.__colonnes - 1), nb_iter, (self.__lignes * self.__colonnes - 1) - compteur)
            
            cell = available_cells[randint(0, len(available_cells) - 1)]
            available_walls = [i for i, mur in enumerate([cell.north, cell.east, cell.south, cell.west]) if mur]

            if len(available_walls) <= 2:
                available_cells.remove(cell)
                continue

            cell_voisins = [cell.n_cell, cell.e_cell, cell.s_cell, cell.w_cell]

            if all(voisin.id == cell.id for voisin in cell_voisins if voisin):
                available_cells.remove(cell)
                continue

            available_walls_rand = sample(available_walls, len(available_walls))
            selected_wall = 0

            for wall_id in available_walls_rand:
                if not cell_voisins[wall_id]: continue
                if cell_voisins[wall_id].id == cell.id: continue

                selected_wall = wall_id
                break
            else:
                available_cells.remove(cell)
                continue

            compteur += 1
            if cell not in already_seen_cells: already_seen_cells.append(cell)

            match selected_wall:
                case 0:
                    cell.north = False
                    if cell.n_cell not in already_seen_cells: already_seen_cells.append(cell.n_cell)
                case 1:
                    cell.east = False
                    if cell.e_cell not in already_seen_cells: already_seen_cells.append(cell.e_cell)
                case 2:
                    cell.south = False
                    if cell.s_cell not in already_seen_cells: already_seen_cells.append(cell.s_cell)
                case 3:
                    cell.west = False
                    if cell.w_cell not in already_seen_cells: already_seen_cells.append(cell.w_cell)

            if time() >= time_last_iter + 1:
                nb_iter = compteur - nb_iter_last
                nb_iter_last = compteur
                time_last_iter = time()

            cell_voisin_id = cell_voisins[selected_wall].id

            for cellule in already_seen_cells:
                if cellule.id == cell_voisin_id:
                    cellule.id = cell.id

        if self.__lignes * self.__colonnes - 1 >= 2499: print()

        entree = randint(0, self.__lignes - 1), 0
        sortie = randint(0, self.__lignes - 1), self.__colonnes - 1

        self.__grille[entree[0]][entree[1]].west = False
        self.__grille[sortie[0]][sortie[1]].east = False

        self.__scrumbled = True

    
    def save(self, name: str) -> None:
        makedirs(path.join(path.dirname(__file__), "sortie", f"{self.__lignes}x{self.__colonnes}"), exist_ok=True)
        with open(path.join(path.dirname(__file__), "sortie", f"{self.__lignes}x{self.__colonnes}", f"{name}.txt"), 'w+') as file:
            file.write(str(self))

    def save_list(self, name: str) -> None:
        output_grille = [[(cell.north, cell.east, cell.south, cell.west) for cell in ligne] for ligne in self.__grille]
        makedirs(path.join(path.dirname(__file__), "sortie_list", f"{self.__lignes}x{self.__colonnes}"), exist_ok=True)
        with open(path.join(path.dirname(__file__), "sortie_list", f"{self.__lignes}x{self.__colonnes}", f"{name}_list.txt"), 'w+') as file:
            file.write(str(output_grille))


    @_timit
    def _exhaustive(self) -> None:
        visited_cells: list[Cellule] = []
        current_cell = self.__grille[randint(0, self.__lignes - 1)][randint(0, self.__colonnes - 1)]
        multis: list[Cellule] = []

        while (len(multis) and len(visited_cells) != self.__colonnes * self.__lignes) or len(visited_cells) != self.__colonnes * self.__lignes:
            current_cell.visited = True
            if current_cell not in visited_cells: visited_cells.append(current_cell)

            available_voisines_cells = [(i_cell, cell) for i_cell, cell in enumerate([current_cell.n_cell, current_cell.e_cell, current_cell.s_cell, current_cell.w_cell]) if cell and not cell.visited]

            if len(available_voisines_cells):
                choosen_cell_id, choosen_cell = available_voisines_cells[randint(0, len(available_voisines_cells) - 1)]

                match choosen_cell_id:
                    case 0:
                        choosen_cell.south = False
                    case 1:
                        choosen_cell.west = False
                    case 2:
                        choosen_cell.north = False
                    case 3:
                        choosen_cell.east = False
                
                if len(available_voisines_cells) > 1:
                    if current_cell not in multis: multis.append(current_cell)
            else:
                current_cell = multis[-1]
                multis.pop()
                continue
        
            current_cell = choosen_cell

        entree = randint(0, self.__lignes - 1), 0
        sortie = randint(0, self.__lignes - 1), self.__colonnes - 1

        self.__grille[entree[0]][entree[1]].west = False
        self.__grille[sortie[0]][sortie[1]].east = False

        self.__scrumbled = True

    
    @classmethod
    def from_txt(cls, path: str):
        grille = []
        with open(path) as file:
            grille = literal_eval(file.read())

        new_grille: list[list[Cellule]] = []

        for i_ligne, ligne in enumerate(grille):
            new_ligne: list[Cellule] = []
            for i_colonne, cell in enumerate(ligne):
                new_cell = Cellule(i_ligne * len(ligne) + i_colonne)
                new_cell.north = cell[0]
                new_cell.east = cell[1]
                new_cell.south = cell[2]
                new_cell.west = cell[3]
                new_ligne.append(new_cell)
            new_grille.append(new_ligne)

        for i_ligne, ligne in enumerate(new_grille):
            for i_colonne, cell in enumerate(ligne):
                if i_ligne != 0:
                    cell.n_cell = new_grille[i_ligne - 1][i_colonne]

                if i_ligne != len(grille) - 1:
                    cell.s_cell = new_grille[i_ligne + 1][i_colonne]

                if i_colonne != 0:
                    cell.w_cell = ligne[i_colonne - 1]

                if i_colonne != len(ligne) - 1:
                    cell.e_cell = ligne[i_colonne + 1]

        return cls(len(new_grille), len(new_grille[0]), new_grille)
                
    def _set_resolve(self, resolve_path: list[int]) -> None:
        for i_cell, cell_id in enumerate(resolve_path):
            cell = self.__grille[cell_id // self.__colonnes][cell_id % self.__colonnes]
            if i_cell == 0:
                if abs(resolve_path[i_cell + 1] - cell_id) == 1:
                    cell.traverse = 'h'
                elif resolve_path[i_cell + 1] - cell_id == self.__colonnes:
                    cell.traverse = 'sw'
                elif cell_id - resolve_path[i_cell + 1] == self.__colonnes:
                    cell.traverse = 'wn'
            elif i_cell == len(resolve_path) - 1:
                if abs(resolve_path[i_cell - 1] - cell_id) == 1:
                    cell.traverse = 'h'
                elif resolve_path[i_cell - 1] - cell_id == self.__colonnes:
                    cell.traverse = 'es'
                elif cell_id - resolve_path[i_cell - 1] == self.__colonnes:
                    cell.traverse = 'ne'
            else:
                if abs(resolve_path[i_cell + 1] - cell_id) == 1  and abs(resolve_path[i_cell - 1] - cell_id) == 1:
                    cell.traverse = 'h'
                elif not abs(resolve_path[i_cell + 1] - cell_id) % self.__colonnes and not abs(resolve_path[i_cell - 1] - cell_id) % self.__colonnes:
                    cell.traverse = 'v'
                elif (cell_id - resolve_path[i_cell - 1] == self.__colonnes and resolve_path[i_cell + 1] - cell_id == 1) or (resolve_path[i_cell - 1] - cell_id == 1 and cell_id - resolve_path[i_cell + 1] == self.__colonnes):
                    cell.traverse = 'ne'
                elif (resolve_path[i_cell - 1] - cell_id == self.__colonnes and resolve_path[i_cell + 1] - cell_id == 1) or (resolve_path[i_cell - 1] - cell_id == 1 and resolve_path[i_cell + 1] - cell_id == self.__colonnes):
                    cell.traverse = 'es'
                elif (resolve_path[i_cell - 1] - cell_id == self.__colonnes and cell_id - resolve_path[i_cell + 1] == 1) or (cell_id - resolve_path[i_cell - 1] == 1 and resolve_path[i_cell + 1] - cell_id == self.__colonnes):
                    cell.traverse = 'sw'
                elif (cell_id - resolve_path[i_cell - 1] == self.__colonnes and cell_id - resolve_path[i_cell + 1] == 1) or (cell_id - resolve_path[i_cell - 1] == 1 and cell_id - resolve_path[i_cell + 1] == self.__colonnes):
                    cell.traverse = 'wn'

        self.__resolved = True
        self.__path = resolve_path

    @_timit
    def resolve(self) -> list[int]:
        if not self.__scrumbled:
            raise Exception("Le labyrinthe n'a pas encore été généré")
        
        for i_ligne, ligne in enumerate(self.__grille):
            if not ligne[0].west:
                depart: tuple[int] = i_ligne, 0
            if not ligne[-1].east:
                arrivee: tuple[int] = i_ligne, self.__colonnes - 1

        current_cell = self.__grille[depart[0]][depart[1]]
        arrivee_cell = self.__grille[arrivee[0]][arrivee[1]]

        result: list[int] = []
        cells_parcourues: list[Cellule] = []
        multi_dir: list[Cellule] = []

        while current_cell != arrivee_cell:
            available_cells: list[Cellule] = []
            
            if not current_cell.north and current_cell.n_cell and current_cell.n_cell not in cells_parcourues:
                available_cells.append(current_cell.n_cell)
            if not current_cell.east and current_cell.e_cell and current_cell.e_cell not in cells_parcourues:
                available_cells.append(current_cell.e_cell)
            if not current_cell.south and current_cell.s_cell and current_cell.s_cell not in cells_parcourues:
                available_cells.append(current_cell.s_cell)
            if not current_cell.west and current_cell.w_cell and current_cell.w_cell not in cells_parcourues:
                available_cells.append(current_cell.w_cell)

            if current_cell not in cells_parcourues: cells_parcourues.append(current_cell)

            if not len(available_cells):
                if current_cell == multi_dir[-1]:
                    multi_dir.pop()
                try:
                    last_multi_i_in_result = result.index(multi_dir[-1].deep_id)
                    result = result[:last_multi_i_in_result]
                    current_cell = multi_dir[-1]
                except:
                    result.clear()
                    current_cell = self.__grille[depart[0]][depart[1]]
                continue
            elif len(available_cells) > 1 and current_cell not in multi_dir: multi_dir.append(current_cell)

            if current_cell.deep_id not in result: result.append(current_cell.deep_id)
            current_cell = available_cells[0]

        result.append(arrivee_cell.deep_id)

        self._set_resolve(result)

        return result
    
    @_timit
    def resolve_a_star(self) -> list[int]:
        if not self.__scrumbled:
            raise Exception("Le labyrinthe n'a pas encore été généré")
        
        for i_ligne, ligne in enumerate(self.__grille):
            if not ligne[0].west:
                depart: tuple[int] = i_ligne, 0
            if not ligne[-1].east:
                arrivee: tuple[int] = i_ligne, self.__colonnes - 1

        depart_cell = self.__grille[depart[0]][depart[1]]
        arrivee_cell = self.__grille[arrivee[0]][arrivee[1]]

        open_list: list[Cellule] = [depart_cell]
        closed_list: list[Cellule] = []

        while len(open_list) > 0:
            current_cell = min(open_list, key=lambda x: x.f_cost)
            open_list.remove(current_cell)
            closed_list.append(current_cell)
        
            if current_cell == arrivee_cell:
                result: list[int] = []
                while current_cell is not None:
                    result.append(current_cell.deep_id)
                    current_cell = current_cell.parent

                result = result[::-1]

                self._set_resolve(result)

                return result

            for wall, new_cell in zip([current_cell.north, current_cell.east, current_cell.south, current_cell.west], [current_cell.n_cell, current_cell.e_cell, current_cell.s_cell, current_cell.w_cell]): # Adjacent squares
                if not new_cell or wall or new_cell in closed_list: continue

                new_cell.parent = current_cell

                # Create the f, g, and h values
                new_cell.g_cost = current_cell.g_cost + 1
                num_ligne_arrivee, num_ligne_current = arrivee_cell.deep_id // self.__colonnes, new_cell.deep_id // self.__colonnes
                num_colonne_arrivee, num_colonne_current = arrivee_cell.deep_id - num_ligne_arrivee * self.__colonnes, new_cell.deep_id - num_ligne_current * self.__colonnes
                new_cell.h_cost = abs(num_ligne_arrivee - num_ligne_current) + abs(num_colonne_arrivee - num_colonne_current)
                new_cell.f_cost = new_cell.g_cost + new_cell.h_cost

                # new_cell is already in the open list
                if len(open_list) and new_cell in open_list and new_cell.g_cost > min(open_list, key=lambda x: x.g_cost): continue

                # Add the new_cell to the open list
                open_list.append(new_cell)

    def mat(self) -> None:
        maze = []
        for i_line, line in enumerate(self.__grille):
            row = []
            for i_colonne, cellule in enumerate(line):
                row.append(1)
                row.append(1 if cellule.north else 0)
            row.append(1)

            maze.append(row)
            
            row = []
            for i_colonne, cellule in enumerate(line):
                row.append(1 if cellule.west else 0)
                row.append(0)

                if i_colonne == self.__colonnes - 1:
                    row.append(1 if cellule.east else 0)

            maze.append(row)

            if i_line == self.__lignes - 1:
                row = []
                for i_colonne, cellule in enumerate(line):
                    row.append(1)
                    row.append(1 if cellule.south else 0)
                row.append(1)
                maze.append(row)

        _, ax = plt.subplots(figsize=(8,8))

        ax.imshow(maze, cmap=plt.cm.binary, interpolation='nearest')

        if self.__resolved:
            new_x = [0, 1]
            new_y = [self.__path[0] // self.__colonnes * 2 + 1, self.__path[0] // self.__colonnes * 2 + 1]

            for i_cell, cell_id in enumerate(self.__path):
                x_brut = cell_id - (cell_id // self.__colonnes) * self.__colonnes
                x_last_brut = self.__path[i_cell - 1] - (self.__path[i_cell - 1] // self.__colonnes) * self.__colonnes
                current_x = x_brut * 2 + 1

                if i_cell != 0:
                    if x_last_brut == x_brut:
                        new_x.extend([current_x, current_x])
                    else:
                        if x_last_brut - x_brut == 1:
                            new_x.extend([current_x + 1, current_x])
                        else:
                            new_x.extend([current_x - 1, current_x])

                y_brut = cell_id // self.__colonnes
                y_last_brut = self.__path[i_cell - 1] // self.__colonnes
                current_y = y_brut * 2 + 1

                if i_cell != 0:
                    if y_last_brut == y_brut:
                        new_y.extend([current_y, current_y])
                    else:
                        if y_last_brut - y_brut == 1:
                            new_y.extend([current_y + 1, current_y])
                        else:
                            new_y.extend([current_y - 1, current_y])
            
            new_x.append(new_x[-1] + 1)
            new_y.append(new_y[-1])

            ax.plot(new_x, new_y, color='red', linewidth=2)
        
        ax.set_xticks([])
        ax.set_yticks([])
        
        plt.show()


if __name__ == "__main__":
    while True:
        lab = Labyrinthe.exploration(100, 100)
        lab.resolve_a_star()
        lab.mat()
        input()