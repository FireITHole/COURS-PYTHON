phrase = "Il fait très beau aujourd'hui. J'espère qu'il fera ce temps demain !"

result = {}

for lettre in phrase:
    if lettre.lower() in "abcdefghijklmnopqrstuvwxyz":
        result[lettre.lower()] = phrase.count(lettre)

print(result)
