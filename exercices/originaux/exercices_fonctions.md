### Exercice 1 : Fonction sans `return`
Écrivez une fonction `afficher_message` qui prend un argument `message` et l'affiche à l'écran sans utiliser `return`.

```python
def afficher_message(message):
    print(message)

# Test
afficher_message("Bonjour, ceci est un message.")
```

### Exercice 2 : Fonction avec `return`
Écrivez une fonction `addition` qui prend deux nombres en paramètres et retourne leur somme.

```python
def addition(a, b):
    return a + b

# Test
resultat = addition(5, 3)
print(resultat)  # Devrait afficher 8
```

### Exercice 3 : Fonction avec plusieurs paramètres
Écrivez une fonction `calculer_surface_rectangle` qui prend deux paramètres `longueur` et `largeur` et retourne la surface du rectangle.

```python
def calculer_surface_rectangle(longueur, largeur):
    return longueur * largeur

# Test
surface = calculer_surface_rectangle(5, 3)
print(surface)  # Devrait afficher 15
```

### Exercice 4 : Fonction avec des valeurs par défaut
Écrivez une fonction `saluer` qui prend deux paramètres : `nom` et `message`. Le paramètre `message` doit avoir une valeur par défaut de `"Bonjour"`.

```python
def saluer(nom, message="Bonjour"):
    return f"{message}, {nom}!"

# Test
print(saluer("Alice"))  # Devrait afficher "Bonjour, Alice!"
print(saluer("Bob", "Salut"))  # Devrait afficher "Salut, Bob!"
```

### Exercice 5 : Fonction avec des paramètres nommés
Écrivez une fonction `creer_compte` qui prend trois paramètres : `nom`, `email`, et `mot_de_passe`. Le paramètre `mot_de_passe` doit avoir une valeur par défaut de `"1234"`.

```python
def creer_compte(nom, email, mot_de_passe="1234"):
    return f"Compte créé pour {nom} avec l'email {email} et le mot de passe {mot_de_passe}"

# Test
print(creer_compte("Alice", "alice@example.com"))  # Mot de passe par défaut
print(creer_compte("Bob", "bob@example.com", "securepassword"))  # Mot de passe personnalisé
```

### Exercice 6 : Fonction avec un nombre variable de paramètres
Écrivez une fonction `additionner_tous` qui prend un nombre variable de paramètres et retourne leur somme.

```python
def additionner_tous(*nombres):
    return sum(nombres)

# Test
print(additionner_tous(1, 2, 3, 4))  # Devrait afficher 10
print(additionner_tous(5, 10))  # Devrait afficher 15
```

### Exercice 7 : Fonction avec des paramètres nommés variables
Écrivez une fonction `afficher_informations` qui prend un nombre variable de paramètres nommés et les affiche sous forme de clé-valeur.

```python
def afficher_informations(**informations):
    for cle, valeur in informations.items():
        print(f"{cle}: {valeur}")

# Test
afficher_informations(nom="Alice", age=25, ville="Paris")
# Devrait afficher :
# nom: Alice
# age: 25
# ville: Paris
```

### Exercice 8 : Fonction avec des paramètres obligatoires et optionnels
Écrivez une fonction `creer_profil` qui prend un paramètre obligatoire `nom` et deux paramètres optionnels `age` et `ville` avec des valeurs par défaut de `None`.

```python
def creer_profil(nom, age=None, ville=None):
    profil = f"Nom: {nom}"
    if age:
        profil += f", Age: {age}"
    if ville:
        profil += f", Ville: {ville}"
    return profil

# Test
print(creer_profil("Alice", 25, "Paris"))  # Devrait afficher "Nom: Alice, Age: 25, Ville: Paris"
print(creer_profil("Bob"))  # Devrait afficher "Nom: Bob"
```

### Exercice 9 : Fonction avec des types annotés
Écrivez une fonction `multiplier` qui prend deux nombres en paramètres et retourne leur produit. Utilisez les annotations de type pour indiquer que les paramètres et le retour sont des `int`.

```python
def multiplier(a: int, b: int) -> int:
    return a * b

# Test
print(multiplier(4, 5))  # Devrait afficher 20
```

### Exercice 10 : Fonction récursive
Écrivez une fonction récursive `factorielle` qui prend un nombre entier `n` et retourne sa factorielle.

```python
def factorielle(n: int) -> int:
    if n == 0:
        return 1
    return n * factorielle(n - 1)

# Test
print(factorielle(5))  # Devrait afficher 120
