### rot13
##### 5 Kyu

ROT13 est un simple algorithme de substitution de lettre qui remplace une lettre par la lettre 13 lettres après dans l’alphabet. ROT13 est un exemple du chiffre de César.

Créez une fonction qui prend une chaîne et retourne la chaîne chiffrée avec Rot13. S’il y a des nombres ou des caractères spéciaux inclus dans la chaîne, ils doivent être retournés tels quels. Seules les lettres de l’alphabet latin / anglais doivent être décalées, comme dans la "mise en œuvre" originale de Rot13.

#### Solution :
```python
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def rot13(message):
    result= ""
    for l in message:
        if l.lower() in alphabet:
            if l.islower():
                result += alphabet[(alphabet.index(l.lower()) + 13) % len(alphabet)]
            else:
                result += alphabet[(alphabet.index(l.lower()) + 13) % len(alphabet)].upper()
        else:
            result += l
    return result
```

#### Test data :
```python
rot13('test') # -> 'grfg'
rot13('Test') # -> 'Grfg'
rot13('aA bB zZ 1234 *!?%') # -> 'nN oO mM 1234 *!?%'
```