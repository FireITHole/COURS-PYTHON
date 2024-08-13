# Les Générateurs

## Introduction

Les générateurs en Python sont une manière efficace de créer des itérateurs. Contrairement aux listes, les générateurs ne stockent pas tous les éléments en mémoire, mais les génèrent à la volée. Cela permet de gérer des séquences de données potentiellement infinies ou très grandes de manière plus efficace en termes de mémoire.

## Création de Générateurs

### Utilisation de la Fonction `yield`

La manière la plus courante de créer un générateur est d'utiliser la fonction `yield` dans une fonction. Lorsque la fonction est appelée, elle retourne un objet générateur sans exécuter le corps de la fonction. Chaque appel à la méthode `__next__()` de l'objet générateur exécute la fonction jusqu'à ce qu'elle atteigne une instruction `yield`, qui retourne la valeur et suspend l'exécution de la fonction.

```python
def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()

print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3
# print(next(gen))  # Raises StopIteration
```

### Générateurs avec des Boucles

Les générateurs sont souvent utilisés avec des boucles pour produire une séquence de valeurs.

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for number in countdown(5):
    print(number)
# Output:
# 5
# 4
# 3
# 2
# 1
```

## Avantages des Générateurs

1. **Efficacité Mémoire**: Les générateurs ne stockent pas tous les éléments en mémoire, ce qui est utile pour les grandes séquences de données.
2. **Paresseux**: Les générateurs produisent des éléments à la demande, ce qui peut améliorer les performances.
3. **Lisibilité**: Les générateurs peuvent rendre le code plus lisible et plus facile à comprendre.

## Générateurs avec des Expressions Génératrices

Les expressions génératrices sont une manière concise de créer des générateurs. Elles ressemblent aux compréhensions de liste, mais utilisent des parenthèses au lieu de crochets.

```python
gen = (x * x for x in range(5))

for value in gen:
    print(value)
# Output:
# 0
# 1
# 4
# 9
# 16
```

## Comparaison avec les Listes

### Liste

```python
squares = [x * x for x in range(5)]
print(squares)
# Output: [0, 1, 4, 9, 16]
```

### Générateur

```python
squares_gen = (x * x for x in range(5))
print(list(squares_gen))
# Output: [0, 1, 4, 9, 16]
```

## Utilisation Avancée des Générateurs

### Générateurs Infini

Les générateurs peuvent produire une séquence infinie de valeurs.

```python
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

gen = infinite_sequence()

for i in range(5):
    print(next(gen))
# Output:
# 0
# 1
# 2
# 3
# 4
```

### Générateurs et `send()`

Les générateurs peuvent recevoir des valeurs via la méthode `send()`. Cela permet de communiquer avec le générateur pendant son exécution.

```python
def echo():
    while True:
        received = yield
        print(f'Received: {received}')

gen = echo()
next(gen)  # Prime the generator
gen.send('Hello')  # Output: Received: Hello
gen.send('World')  # Output: Received: World
```

### Générateurs et `close()`

La méthode `close()` arrête le générateur et lève une exception `GeneratorExit` à l'intérieur du générateur.

```python
def simple_generator():
    try:
        yield 1
        yield 2
        yield 3
    except GeneratorExit:
        print("Generator closed")

gen = simple_generator()
print(next(gen))  # Output: 1
gen.close()  # Output: Generator closed
```

## Conclusion

Les générateurs sont un outil puissant en Python pour créer des itérateurs de manière efficace et paresseuse. Ils permettent de gérer des séquences de données de manière plus efficace en termes de mémoire et de performances. Les générateurs peuvent être créés à l'aide de la fonction `yield` ou d'expressions génératrices, et offrent des fonctionnalités avancées comme la communication bidirectionnelle avec `send()` et la gestion de la fermeture avec `close()`.

## Exercice Pratique

1. Créez un générateur `fibonacci` qui génère les nombres de la séquence de Fibonacci.
2. Utilisez ce générateur pour imprimer les 10 premiers nombres de la séquence de Fibonacci.

```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = fibonacci()

for _ in range(10):
    print(next(fib_gen))
# Output:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
```
