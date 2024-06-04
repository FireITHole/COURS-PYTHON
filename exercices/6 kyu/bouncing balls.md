### Balles rebondissantes
##### 6 Kyu

Un enfant joue avec une balle au n-ième étage d'un grand immeuble. La hauteur de cet étage par rapport au niveau du sol, h, est connue.

Il lâche la balle par la fenêtre. La balle rebondit, par exemple, à deux tiers de sa hauteur (un rebond de 0,66).

Sa mère regarde par une fenêtre à 1,5 mètres du sol.

Combien de fois la mère verra-t-elle la balle passer devant sa fenêtre (y compris quand elle tombe et rebondit) ?

Trois conditions doivent être remplies pour une expérience valide :
- Le paramètre flottant "h" en mètres doit être supérieur à 0
- Le paramètre flottant "rebond" doit être supérieur à 0 et inférieur à 1
- Le paramètre flottant "fenêtre" doit être inférieur à h.
Si les trois conditions ci-dessus sont remplies, retournez un entier positif, sinon retournez -1.

Note :
La balle ne peut être vue que si la hauteur du rebond de la balle est strictement supérieure au paramètre fenêtre.

Exemples :
- h = 3, rebond = 0,66, fenêtre = 1,5, le résultat est 3

- h = 3, rebond = 1, fenêtre = 1,5, le résultat est -1

(Condition 2 non remplie).

#### Solution :
```python
def bouncing_ball(h, bounce, window):
    if h <= 0 or bounce <= 0 or bounce >= 1 or window > h: return -1
    counter = 0
    while h > window:
        h *= bounce
        counter += 2
    return counter - 1
```

#### Test data :
```python
testing(2, 0.5, 1) # -> 1
testing(3, 0.66, 1.5) # -> 3
testing(30, 0.66, 1.5) # -> 15
testing(30, 0.75, 1.5) # -> 21
```