FILE_CONTENT: str = ""
NEW_CONTENT:str = ""

with open("raw.txt") as file:
    FILE_CONTENT = file.read()

CONST: str = "abcdefghijklmnopqrstuvwxyz"

i = 0
while i < len(FILE_CONTENT) - len(CONST):
    if FILE_CONTENT[i:i+len(CONST)] == CONST:
        NEW_CONTENT += '\n' + CONST + '\n'
        i += len(CONST)
    else:
        NEW_CONTENT += FILE_CONTENT[i]
        i += 1

with open("render.txt", "w") as file:
    file.write(NEW_CONTENT)