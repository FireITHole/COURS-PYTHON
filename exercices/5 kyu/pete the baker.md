### Pete, le boulanger
##### 5 Kyu

Pete aime faire des gâteaux. Il a quelques recettes et ingrédients. Malheureusement, il n'est pas bon en maths. Pouvez-vous l'aider à savoir combien de gâteaux il pourrait faire au maximum en tenant compte de ses recettes ?

Écrivez une fonction `cakes()`, qui prend la recette (dictionnaire) et les ingrédients disponibles (également un dictionnaire) et retourne le nombre maximum de gâteaux que Pete peut faire (entier). Pour simplifier, il n'y a pas d'unités pour les quantités (par exemple, 1 kg de farine ou 200 g de sucre sont simplement 1 ou 200). Les ingrédients qui ne sont pas présents dans les objets, peuvent être considérés comme 0.

Exemples:
```python
# must return 2
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
# must return 0
cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})
```

#### Solution :
```python
def cakes(recipe, available):
    result = []
    for ingredient, needed in recipe.items():
        if ingredient not in available.keys():
            return 0
        result.append(available[ingredient] // needed)
    
    return min(result)
```

#### Test data :
```python
recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
cakes(recipe, available) # -> 2

recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available = {"sugar": 500, "flour": 2000, "milk": 2000}
cakes(recipe, available) # -> 0
```