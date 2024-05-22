class Person:
    def __new__(cls, nom: str, age: int):
        if not isinstance(nom, str):
            raise TypeError
        
        if not isinstance(age, int):
            raise TypeError
        
        if age <= 0:
            raise ValueError("L'âge doit être strictement positif.")
        
        return super().__new__(cls)

    def __init__(self, nom: str, age: int) -> None:
        self._nom = nom
        self._age = age

    def __repr__(self) -> str:
        return f"Nom : {self._nom}, Âge : {self._age}"
    
    def __add__(self, nb_annees: int) -> None:
        if not isinstance(nb_annees, int):
            raise TypeError
        
        if nb_annees <= 0:
            raise ValueError("Le nombre d'années doit être strictement positif.")
        
        self._age += nb_annees
    
    def __sub__(self, nb_annees: int) -> None:
        if not isinstance(nb_annees, int):
            raise TypeError
        
        if nb_annees <= 0:
            raise ValueError("Le nombre d'années doit être strictement positif.")
        
        self._age -= nb_annees

    def __eq__(self, other: "Person") -> bool:
        return self._nom == other._nom and self._age == other._age
    
    def __gt__(self, other: "Person") -> bool:
        return self._age > other._age

    @property
    def nom(self) -> str:
        return self._nom
    
    @nom.setter
    def nom(self, new_nom: str) -> None:
        if not isinstance(new_nom, str):
            raise TypeError
        
        self._nom = new_nom
    
    
antoine = Person("Antoine", 23)
antoine_bis = Person("Antoine", 22)
antoine.nom = "test"
