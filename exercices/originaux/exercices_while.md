### Exercice 1 : Compter jusqu'à 10
Écrivez un programme qui utilise une boucle `while` pour afficher les nombres de 1 à 10.

```python
# Exercice 1
i = 1
while i <= 10:
    print(i)
    i += 1
```

### Exercice 2 : Somme des nombres de 1 à 100
Écrivez un programme qui utilise une boucle `while` pour calculer la somme des nombres de 1 à 100.

```python
# Exercice 2
somme = 0
i = 1

while i <= 100:
    somme += i
    i += 1

print("La somme des nombres de 1 à 100 est :", somme)
```

### Exercice 3 : Afficher les nombres pairs de 1 à 20
Écrivez un programme qui utilise une boucle `while` pour afficher tous les nombres pairs entre 1 et 20.

```python
# Exercice 3
i = 1

while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1
```

### Exercice 4 : Compter les multiples de 3 jusqu'à 30
Écrivez un programme qui utilise une boucle `while` pour compter combien de nombres entre 1 et 30 sont des multiples de 3.

```python
# Exercice 4
i = 1
compteur = 0

while i <= 30:
    if i % 3 == 0:
        compteur += 1
    i += 1

print("Il y a", compteur, "multiples de 3 entre 1 et 30.")
```

### Exercice 5 : Factorielle d'un nombre
Écrivez un programme qui utilise une boucle `while` pour calculer la factorielle de 5 (5!).

```python
# Exercice 5
n = 5
factorielle = 1
i = 1

while i <= n:
    factorielle *= i
    i += 1

print("La factorielle de 5 est :", factorielle)
