DICT = {
    "A": ".-", 
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.", 
    "H": "....", 
    "I": "..", 
    "J": ".---", 
    "K": "-.-", 
    "L": ".-..", 
    "M": "--", 
    "N": "-.", 
    "O": "---", 
    "P": ".--.", 
    "Q": "--.-", 
    "R": ".-.", 
    "S": "...", 
    "T": "-", 
    "U": "..-", 
    "V": "...-", 
    "W": ".--", 
    "X": "-..-", 
    "Y": "-.--", 
    "Z": "--..", 
    "0": "-----", 
    "1": ".----", 
    "2": "..---", 
    "3": "...--", 
    "4": "....-", 
    "5": ".....", 
    "6": "-....", 
    "7": "--...", 
    "8": "---..", 
    "9": "----.",
    " ": "   "
}

DECODE_DICT = {value: key for key, value in DICT.items()}

def encode(text: str) -> str:
    # return ' '.join([DICT[char.upper()] for char in text])
    result: list = []
    for char in text:
        result.append(DICT[char.upper()])
    return ' '.join(result)

def decode(morse: str) -> str:
    result = []
    words = morse.split("   ")
    for word in words:
        word = word.lstrip()
        temp_word = ""
        letters = word.split(' ')
        for letter in letters:
            temp_word += DECODE_DICT[letter]
        result.append(temp_word)
    return ' '.join(result)


entree = input("Message à encoder : ")

morse = encode(entree)
print(morse)
#print(decode(morse))