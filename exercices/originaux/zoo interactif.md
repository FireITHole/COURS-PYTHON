# Exercice : Gestion d'un Zoo Interactif

## Contexte
Vous allez créer un programme pour gérer un zoo interactif. Le zoo aura différents types d'animaux, et chaque type d'animal pourra effectuer des actions spécifiques. Vous utiliserez les concepts de classes, d'héritage et de polymorphisme en Python pour accomplir cette tâche.

## Objectifs
L'exercice vise à vous familiariser avec :
- La création de classes en Python.
- L'utilisation de l'héritage pour structurer les classes.
- L'implémentation de méthodes redéfinies dans les classes enfants.
- La gestion des collections d'objets (listes d'animaux dans ce cas).
- L'application des principes de polymorphisme.

## Détails de l'exercice

### 1. Classe Animal
- Créez une classe `Animal` qui aura les attributs suivants :
  - `nom` : le nom de l'animal (str)
  - `espèce` : l'espèce de l'animal (str)
  - `age` : l'âge de l'animal (int)
- La classe `Animal` aura une méthode `parler` qui sera redéfinie dans les classes enfants mais qui sera définie dans la classe `Animal` simplement par un `pass`.



```python
class Animal:
    def __init__(self, nom, espèce, age):
        self.nom = nom
        self.espèce = espèce
        self.age = age

    def parler(self):
        pass
```

### 2. Classes Enfants
Créez des classes enfants (Lion, Oiseau, Serpent) qui héritent de la classe Animal.
Chaque classe enfant doit redéfinir la méthode parler pour afficher un son spécifique :
La classe Lion doit afficher un rugissement.
La classe Oiseau doit afficher un chant.
La classe Serpent doit afficher un sifflement.

```python
class Lion(Animal):
    def parler(self):
        print(f"{self.nom} le {self.espèce} rugit.")

class Oiseau(Animal):
    def parler(self):
        print(f"{self.nom} le {self.espèce} chante.")

class Serpent(Animal):
    def parler(self):
        print(f"{self.nom} le {self.espèce} siffle.")
```

### 3. Classe Zoo
Créez une classe Zoo avec un attribut animaux qui est une liste d'animaux.
La classe Zoo doit inclure les méthodes suivantes :
ajouter_animal : ajoute un animal à la liste animaux.
afficher_animaux : affiche tous les animaux du zoo.
parler_tous : appelle la méthode parler pour chaque animal du zoo.

```python
class Zoo:
    def __init__(self):
        self.animaux = []

    def ajouter_animal(self, animal):
        self.animaux.append(animal)
        print(f"{animal.nom} le {animal.espèce} a été ajouté au zoo.")

    def afficher_animaux(self):
        for animal in self.animaux:
            print(f"{animal.nom} le {animal.espèce}, âge {animal.age} ans")

    def parler_tous(self):
        for animal in self.animaux:
            animal.parler()
```

### 4. Tester le programme
Créez une instance de Zoo et ajoutez-y plusieurs animaux de différentes espèces.
Utilisez les méthodes afficher_animaux et parler_tous pour vérifier que votre programme fonctionne correctement.
Voici un exemple de script pour tester votre programme :

```python
if __name__ == "__main__":
    zoo = Zoo()

    simba = Lion("Simba", "lion", 5)
    tweety = Oiseau("Tweety", "oiseau", 2)
    kaa = Serpent("Kaa", "serpent", 3)

    zoo.ajouter_animal(simba)
    zoo.ajouter_animal(tweety)
    zoo.ajouter_animal(kaa)

    zoo.afficher_animaux()
    zoo.parler_tous()
```

#### Consignes supplémentaires
Testez le programme avec différents animaux et vérifiez qu'ils sont ajoutés correctement au zoo et qu'ils parlent comme prévu.
Vous pouvez ajouter d'autres types d'animaux pour diversifier le zoo et enrichir l'exercice.

Bonne chance !