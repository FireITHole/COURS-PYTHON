### Poids pour poids
##### 5 Kyu

Mon ami John et moi sommes membres du "De gros à musclé club (GMC)". John est inquiet car chaque mois une liste avec les poids des membres est publiée et chaque mois il est le dernier de la liste, ce qui signifie qu'il est le plus lourd.

Je suis celui qui établit la liste, alors je lui ai dit : "Ne t'inquiète plus, je vais modifier l'ordre de la liste". Il a été décidé d'attribuer un "poids" aux nombres. Le poids d'un nombre sera désormais la somme de ses chiffres.

Par exemple, 99 aura un "poids" de 18, 100 aura un "poids" de 1, donc dans la liste, 100 viendra avant 99.

Étant donné une chaîne avec les poids des membres du FFC dans l'ordre normal, pouvez-vous donner cette chaîne ordonnée par les "poids" de ces nombres ?

Exemple :
"56 65 74 100 99 68 86 180 90" ordonné par poids des nombres devient :

"100 180 90 56 65 74 68 86 99"
Quand deux nombres ont le même "poids", classons-les comme s'ils étaient des chaînes (ordre alphabétique) et non des nombres :

180 vient avant 90 car, ayant le même "poids" (9), il vient avant en tant que chaîne.

Tous les nombres de la liste sont des nombres positifs et la liste peut être vide.

Notes :
Il peut arriver que la chaîne d'entrée ait des espaces avant, après et plus d'un espace unique entre deux nombres consécutifs.

#### Solution :
```python
def order_weight(_str):
    return ' '.join(sorted(sorted(_str.split(' ')), key=lambda x: sum(int(c) for c in x)))
```

#### Test data :
```python
order_weight("103 123 4444 99 2000") # -> "2000 103 123 4444 99"
order_weight("2000 10003 1234000 44444444 9999 11 11 22 123") # -> "11 11 2000 10003 22 123 1234000 44444444 9999"
order_weight("") # -> ""
```