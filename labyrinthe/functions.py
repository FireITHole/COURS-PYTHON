from random import randint
from os import path, makedirs
from time import time
import sys

class Cellule:
    def __init__(self, id: int) -> None:
        self._north = True
        self._east = True
        self._south = True
        self._west = True
        self._n_cell = None
        self._e_cell = None
        self._s_cell = None
        self._w_cell = None
        self._traverse: str = ""
        self._id: int = id
        self._deep_id: int = id

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
    def __new__(cls, lignes: int, colonnes: int):
        if not isinstance(lignes, int) or not isinstance(colonnes, int):
            raise TypeError
        
        if lignes < 3 or colonnes < 3:
            raise ValueError("Le nombre de lignes ou de colonnes ne peut pas être inférieur à 3")

        return super().__new__(cls)

    def __init__(self, lignes: int, colonnes: int) -> None:
        self.__lignes: int = lignes
        self.__colonnes: int = colonnes
        self.__grille: list[list[Cellule]] = [[Cellule(i_ligne * self.__colonnes + i_colonne) for i_colonne in range(self.__colonnes)] for i_ligne in range(self.__lignes)]
        self.__scrumbled = False

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


    def __repr__(self) -> str:
        result = []
        for ligne in self.__grille:
            result_ligne = [[], [], []]
            for cell in [cell.get_cell() for cell in ligne]:
                for x in range(3):
                    result_ligne[x].append(cell[x])
            result.append("\n".join("".join(line) for i_line, line in enumerate(result_ligne) if not all(x == " " for x in "".join(line)) or i_line == 1))

        return "\n".join(result) + '\n'
    

    def _timit(f):
        def wrapper(*args, **kwargs):
            debut = time()
            result = f(*args, **kwargs)
            fin = time()
            print(f"Temps d'execution : {fin - debut} secondes.")
            return result
        return wrapper
    
    @staticmethod
    def _progress_bar(percent: float, total: int) -> None:
        bar_length = 50
        sys.stdout.write('\r')
        sys.stdout.write("Completed: [{:{}}] {:>3}%".format('=' * int(percent/(100.0/bar_length)), bar_length, int(percent)))
        sys.stdout.flush()
    
    @_timit
    def generate(self) -> None:
        print("Génération en cours...")
        compteur = 0
        while compteur < self.__lignes * self.__colonnes - 1:
            self._progress_bar(100.0 * compteur / (self.__lignes * self.__colonnes - 1), self.__lignes * self.__colonnes - 1)
            
            rand_cell_id: int = randint(0, self.__lignes * self.__colonnes - 1)
            rand_wall: int = randint(0, 3) # 0: n, 1: e, 2: s, 3: w
            cell = self.__grille[rand_cell_id // self.__colonnes][rand_cell_id % self.__colonnes]
            cell_walls = [cell.north, cell.east, cell.south, cell.west]
            cell_voisins = [cell.n_cell, cell.e_cell, cell.s_cell, cell.w_cell]

            if not cell_voisins[rand_wall]: continue
            if not cell_walls[rand_wall]: continue
            if cell_voisins[rand_wall].id == cell.id: continue

            match rand_wall:
                case 0:
                    cell.north = False
                case 1:
                    cell.east = False
                case 2:
                    cell.south = False
                case 3:
                    cell.west = False

            compteur += 1
            cell_voisin_id = cell_voisins[rand_wall].id

            for ligne in self.__grille:
                for cellule in ligne:
                    if cellule.id == cell_voisin_id:
                        cellule.id = cell.id
            
        entree = randint(0, self.__lignes - 1), 0
        sortie = randint(0, self.__lignes - 1), self.__colonnes - 1

        self.__grille[entree[0]][entree[1]].west = False
        self.__grille[sortie[0]][sortie[1]].east = False

        self.__scrumbled = True
        print("Done !")

    
    def save(self, name: str) -> None:
        makedirs(path.join('.', "sortie", f"{self.__lignes}x{self.__colonnes}"), exist_ok=True)
        with open(path.join('.', "sortie", f"{self.__lignes}x{self.__colonnes}", f"{name}.txt"), 'w+') as file:
            file.write(str(self))

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
            #print(f"Current cell : {current_cell}")
            available_cells: list[Cellule] = []
            
            if not current_cell.north and current_cell.n_cell and current_cell.n_cell not in cells_parcourues:
                available_cells.append(current_cell.n_cell)
            if not current_cell.east and current_cell.e_cell and current_cell.e_cell not in cells_parcourues:
                available_cells.append(current_cell.e_cell)
            if not current_cell.south and current_cell.s_cell and current_cell.s_cell not in cells_parcourues:
                available_cells.append(current_cell.s_cell)
            if not current_cell.west and current_cell.w_cell and current_cell.w_cell not in cells_parcourues:
                available_cells.append(current_cell.w_cell)

            #print(f"Available cells : {[cell.deep_id for cell in available_cells]}")

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
                #print(f"Parcoured cells : [{", ".join([str(cell.deep_id) for cell in cells_parcourues])}]")
                #print(result)
                #print("Plus de chemins dispos...")
                continue
            elif len(available_cells) > 1 and current_cell not in multi_dir: multi_dir.append(current_cell)

            #if len(multi_dir): print(f"LMD: {[cell.deep_id for cell in multi_dir]}")

            if current_cell.deep_id not in result: result.append(current_cell.deep_id)
            #print(f"Parcoured cells : [{", ".join([str(cell.deep_id) for cell in cells_parcourues])}]")
            #print(result)
            current_cell = available_cells[0]

        result.append(arrivee_cell.deep_id)

        for i_cell, cell_id in enumerate(result):
            cell = self.__grille[cell_id // self.__colonnes][cell_id % self.__colonnes]
            if i_cell == 0:
                if abs(result[i_cell + 1] - cell_id) == 1:
                    cell.traverse = 'h'
                elif result[i_cell + 1] - cell_id == self.__colonnes:
                    cell.traverse = 'sw'
                elif cell_id - result[i_cell + 1] == self.__colonnes:
                    cell.traverse = 'wn'
            elif i_cell == len(result) - 1:
                if abs(result[i_cell - 1] - cell_id) == 1:
                    cell.traverse = 'h'
                elif result[i_cell - 1] - cell_id == self.__colonnes:
                    cell.traverse = 'es'
                elif cell_id - result[i_cell - 1] == self.__colonnes:
                    cell.traverse = 'ne'
            else:
                if abs(result[i_cell + 1] - cell_id) == 1  and abs(result[i_cell - 1] - cell_id) == 1:
                    cell.traverse = 'h'
                elif not abs(result[i_cell + 1] - cell_id) % self.__colonnes and not abs(result[i_cell - 1] - cell_id) % self.__colonnes:
                    cell.traverse = 'v'
                elif (cell_id - result[i_cell - 1] == self.__colonnes and result[i_cell + 1] - cell_id == 1) or (result[i_cell - 1] - cell_id == 1 and cell_id - result[i_cell + 1] == self.__colonnes):
                    cell.traverse = 'ne'
                elif (result[i_cell - 1] - cell_id == self.__colonnes and result[i_cell + 1] - cell_id == 1) or (result[i_cell - 1] - cell_id == 1 and result[i_cell + 1] - cell_id == self.__colonnes):
                    cell.traverse = 'es'
                elif (result[i_cell - 1] - cell_id == self.__colonnes and cell_id - result[i_cell + 1] == 1) or (cell_id - result[i_cell - 1] == 1 and result[i_cell + 1] - cell_id == self.__colonnes):
                    cell.traverse = 'sw'
                elif (cell_id - result[i_cell - 1] == self.__colonnes and cell_id - result[i_cell + 1] == 1) or (cell_id - result[i_cell - 1] == 1 and cell_id - result[i_cell + 1] == self.__colonnes):
                    cell.traverse = 'wn'

        return result


if __name__ == "__main__":
    lab = Labyrinthe(15, 15)
    lab.generate()
    print(lab.resolve())
    print(lab)
