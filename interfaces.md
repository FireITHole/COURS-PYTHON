# Les Interfaces et les Méthodes Abstraites
![Image](https://miro.medium.com/v2/resize:fit:756/1*vjsWf2kTrZyT_oRvk8ph3w.png "titre")
## Introduction

En Python, les interfaces et les méthodes abstraites sont des concepts essentiels pour la programmation orientée objet. Ils permettent de définir des contrats que les classes dérivées doivent respecter, assurant ainsi une structure et une cohérence dans le code.

## Les Classes Abstraites

Une classe abstraite est une classe qui ne peut pas être instanciée directement. Elle sert de modèle pour d'autres classes. Les classes abstraites peuvent contenir des méthodes abstraites, qui sont des méthodes déclarées mais non implémentées.

### Définir une Classe Abstraite

Pour définir une classe abstraite en Python, nous utilisons le module `abc` (Abstract Base Classes).

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
```

Dans cet exemple, `Animal` est une classe abstraite avec une méthode abstraite `make_sound`.

### Hériter d'une Classe Abstraite

Une classe qui hérite d'une classe abstraite doit implémenter toutes les méthodes abstraites de la classe parente.

```python
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"
```

Ici, `Dog` et `Cat` héritent de `Animal` et implémentent la méthode `make_sound`.

## Les Interfaces

En Python, il n'y a pas de concept d'interface comme dans certains autres langages (par exemple, Java). Cependant, les classes abstraites peuvent être utilisées pour simuler des interfaces.

### Définir une Interface

Une interface peut être définie en utilisant une classe abstraite avec uniquement des méthodes abstraites.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
```

### Implémenter une Interface

Les classes qui implémentent cette interface doivent fournir des implémentations pour toutes les méthodes abstraites.

```python
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius
```

## Avantages des Classes Abstraites et Interfaces

1. **Encapsulation**: Elles permettent de cacher les détails d'implémentation et de ne montrer que les fonctionnalités essentielles.
2. **Réutilisabilité**: Elles encouragent la réutilisation du code en définissant des comportements communs.
3. **Flexibilité**: Elles permettent de changer les implémentations sans affecter le code qui utilise les interfaces/classes abstraites.
4. **Maintenabilité**: Elles facilitent la maintenance du code en imposant une structure claire.

## Conclusion

Les classes abstraites et les interfaces sont des outils puissants pour structurer le code en Python. Elles permettent de définir des contrats clairs et de s'assurer que les classes dérivées respectent ces contrats, ce qui conduit à un code plus propre et plus maintenable.

## Exercice Pratique

1. Créez une classe abstraite `Vehicle` avec des méthodes abstraites `start_engine` et `stop_engine`.
2. Implémentez deux classes `Car` et `Truck` qui héritent de `Vehicle` et fournissent des implémentations pour les méthodes abstraites.

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"

    def stop_engine(self):
        return "Car engine stopped"

class Truck(Vehicle):
    def start_engine(self):
        return "Truck engine started"

    def stop_engine(self):
        return "Truck engine stopped"
```
