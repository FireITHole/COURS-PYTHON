from re import findall

FILE_CONTENT = ""

with open("raw.txt") as file:
    FILE_CONTENT = file.read()

CONST = "abcdefghijklmnopqrstuvwxyz"
RESULT = 0

i = 0
while i < len(FILE_CONTENT) - len(CONST):
    if FILE_CONTENT[i:i+len(CONST)] == CONST:
        RESULT += 1
        i += len(CONST) - 1
    i += 1

FINDALL_RESULT = len(findall(CONST, FILE_CONTENT))

try:
    assert RESULT == FINDALL_RESULT
    print(f"Test passed! RESULT={RESULT}, FINDALL_RESULT={FINDALL_RESULT}")
except AssertionError:
    print(f"Test failed : {RESULT} != {FINDALL_RESULT}")