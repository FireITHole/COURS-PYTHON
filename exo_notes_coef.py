notes = [{"note": 10, "coef": 2}, {"note": 12, "coef": 3}, {"note": 16, "coef": 4}]
# Trouver la moyenne de ces notes en prenant en compte leur coéfficient (moyenne pondérée)

nombre_notes = 0
total_notes = 0

for note in notes:
    nombre_notes += note["coef"]
    total_notes += note["note"]*note["coef"]

print(total_notes/nombre_notes)