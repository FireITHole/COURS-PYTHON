from random import choices

CONST = "abcdefghijklmnopqrstuvwxyz"
RESULT = ""

for _ in range(10000):
    rand = ''.join(choices(population=CONST, k=26))
    RESULT += ''.join(choices(population=[rand, CONST], weights=[250, 1]))

with open("raw.txt", "w") as f:
    f.write(RESULT)