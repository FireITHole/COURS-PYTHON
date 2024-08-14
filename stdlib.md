# la Bibliothèque Standard : Modules `sys`, `os` et `os.path`

## Introduction

La bibliothèque standard de Python (stdLib) est une collection de modules et de packages qui sont inclus avec l'installation de Python. Elle fournit des fonctionnalités de base pour la manipulation des fichiers, des systèmes d'exploitation, des processus, des dates, des mathématiques, et bien plus encore. Dans ce cours, nous allons nous concentrer sur trois modules essentiels : `sys`, `os`, et `os.path`.

## Module `sys`

Le module `sys` fournit des fonctions et des variables utilisées pour manipuler différentes parties de l'environnement d'exécution Python.

### Accéder aux Arguments de la Ligne de Commande

Le module `sys` permet d'accéder aux arguments passés à un script Python depuis la ligne de commande via `sys.argv`.

```python
# script.py
import sys

print("Arguments:", sys.argv)
```

Exécution :

```sh
$ python script.py arg1 arg2
Arguments: ['script.py', 'arg1', 'arg2']
```

### Sortie et Erreur Standard

Le module `sys` permet de rediriger la sortie standard et l'erreur standard.

```python
import sys

sys.stdout.write("This is standard output\n")
sys.stderr.write("This is standard error\n")
```

### Terminer un Programme

Le module `sys` permet de terminer un programme avec `sys.exit()`.

```python
import sys

if len(sys.argv) < 2:
    print("Usage: script.py <arg>")
    sys.exit(1)
```

### Informations sur la Version de Python

Le module `sys` fournit des informations sur la version de Python en cours d'utilisation.

```python
import sys

print("Python version:", sys.version)
print("Version info:", sys.version_info)
```

## Module `os`

Le module `os` fournit une manière d'interagir avec le système d'exploitation. Il permet de manipuler les fichiers, les répertoires, et les processus.

### Manipulation des Répertoires

#### Changer le Répertoire Courant

```python
import os

os.chdir('/path/to/directory')
print("Current directory:", os.getcwd())
```

#### Lister les Fichiers dans un Répertoire

```python
import os

files = os.listdir('.')
print("Files in current directory:", files)
```

### Manipulation des Fichiers

#### Créer et Supprimer des Fichiers

```python
import os

# Créer un fichier
with open('example.txt', 'w') as f:
    f.write("Hello, World!")

# Supprimer un fichier
os.remove('example.txt')
```

#### Renommer et Déplacer des Fichiers

```python
import os

# Renommer un fichier
os.rename('old_name.txt', 'new_name.txt')

# Déplacer un fichier
os.rename('new_name.txt', '/path/to/new_directory/new_name.txt')
```

### Exécution de Commandes Système

```python
import os

os.system('echo "Hello from the shell"')
```

## Module `os.path`

Le module `os.path` fournit des fonctions pour manipuler les chemins de fichiers et de répertoires de manière portable.

### Joindre des Chemins

```python
import os.path

path = os.path.join('/path', 'to', 'directory', 'file.txt')
print("Joined path:", path)
```

### Vérifier l'Existence d'un Chemin

```python
import os.path

exists = os.path.exists('/path/to/file.txt')
print("Path exists:", exists)
```

### Obtenir le Nom de Base et le Répertoire

```python
import os.path

path = '/path/to/directory/file.txt'
basename = os.path.basename(path)
dirname = os.path.dirname(path)

print("Basename:", basename)
print("Dirname:", dirname)
```

### Diviser l'Extension de Fichier

```python
import os.path

path = '/path/to/directory/file.txt'
root, ext = os.path.splitext(path)

print("Root:", root)
print("Extension:", ext)
```

### Vérifier si un Chemin est un Fichier ou un Répertoire

```python
import os.path

PATH_1 = '/path/to/file.txt'
PATH_2 = '/path/to/directory'

print("PATH_1 is file:", os.path.isfile(PATH_1))
print("PATH_1 is directory:", os.path.isdir(PATH_1))

print("PATH_2 is file:", os.path.isfile(PATH_2))
print("PATH_2 is directory:", os.path.isdir(PATH_2))
```

## Conclusion

Les modules `sys`, `os`, et `os.path` de la bibliothèque standard de Python sont des outils puissants pour interagir avec le système d'exploitation et l'environnement d'exécution. Ils permettent de manipuler les fichiers, les répertoires, les processus, et les arguments de la ligne de commande de manière portable et efficace.

## Exercice Pratique

1. Écrivez un script Python qui prend un chemin de répertoire en argument de la ligne de commande et affiche tous les fichiers dans ce répertoire.
2. Pour chaque fichier, affichez son nom, sa taille en octets, et son extension.

```python
import sys
import os
import os.path

def list_files(directory):
    if not os.path.isdir(directory):
        print(f"{directory} is not a valid directory")
        return

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            size = os.path.getsize(filepath)
            _, ext = os.path.splitext(filename)
            print(f"File: {filename}, Size: {size} bytes, Extension: {ext}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    list_files(directory)
```

## Exercice avancé

1. Écrivez un script Python qui prend un chemin de répertoire en argument de la ligne de commande et affiche tous les fichiers et dossiers dans ce répertoire.
2. Pour chaque dossier, rentrez dans son arborescence et affichez les fichiers qu'il contient. Si celui-ci contient également des dossiers, rentrez dans son arborescence jusqu'à afficher le dernier fichier du dernier dossier.

```python
import sys
import os
import os.path

def list_files(directory, level=0):
    if not os.path.isdir(directory):
        print(f"{directory} is not a valid directory")
        return

    print(f"{"----" * level + "> " if level else ""}{os.path.split(directory)[1]}\\")

    items = os.listdir(directory)
    files = [item for item in items if os.path.isfile(os.path.join(directory, item))]
    dirs = [item for item in items if os.path.isdir(os.path.join(directory, item))]

    for filename in files:
        print(f"{"----" * (level+1) + "> " if (level+1) else ""}{filename}")

    for dirname in dirs:
        list_files(os.path.join(directory, dirname), level + 1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    list_files(directory)
```
