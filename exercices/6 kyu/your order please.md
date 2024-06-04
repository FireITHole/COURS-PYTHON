### Votre commande, svp
##### 6 Kyu

Votre tâche est de trier une chaîne donnée. Chaque mot de la chaîne contiendra un seul chiffre. Ce chiffre est la position que le mot doit avoir dans le résultat.

Note : Les chiffres peuvent aller de 1 à 9. Donc 1 sera le premier mot (pas 0).

Si la chaîne d'entrée est vide, retournez une chaîne vide. Les mots dans la chaîne d'entrée ne contiendront que des chiffres consécutifs valides.

Exemples :
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""

#### Solution :
```python
def extract_number(word):
    for l in word: 
        if l.isdigit(): return int(l)
    return None

def order(sentence):
    return ' '.join(sorted(sentence.split(), key=extract_number))
```
#### Test data :
```python
order("is2 Thi1s T4est 3a") # -> "Thi1s is2 3a T4est"
order("4of Fo1r pe6ople g3ood th5e the2") # -> "Fo1r the2 g3ood 4of th5e pe6ople"
order("e2st cec1 tes4t u3n") # -> "cec1 e2st u3n tes4t"
```