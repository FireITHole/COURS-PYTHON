### Décoder le code morse
##### 6 Kyu

Dans ce kata, vous devez écrire un simple décodeur de code Morse. Bien que le code Morse soit maintenant principalement supplanté par les canaux de communication vocale et de données numériques, il a encore son utilité dans certaines applications à travers le monde.
Le code Morse encode chaque caractère comme une séquence de "points" et de "tirets". Par exemple, la lettre A est codée comme ·−, la lettre Q est codée comme −−·−, et le chiffre 1 est codé comme ·−−−−. Le code Morse ne distingue pas les majuscules des minuscules, les lettres majuscules sont traditionnellement utilisées. Lorsque le message est écrit en code Morse, un espace simple est utilisé pour séparer les codes des caractères et 3 espaces sont utilisés pour séparer les mots. Par exemple, le message HEY JUDE en code Morse est codé comme ···· · −·−−   ·−−− ··− −·· ·.

NOTE : Les espaces supplémentaires avant ou après le code n'ont pas de signification et doivent être ignorés.

En plus des lettres, des chiffres et de la ponctuation, il existe certains codes de service spéciaux, le plus célèbre étant le signal de détresse international SOS (qui a été émis pour la première fois par le Titanic), qui est codé comme ···−−−···. Ces codes spéciaux sont traités comme des caractères spéciaux uniques et sont généralement transmis comme des mots séparés.

Votre tâche est de mettre en œuvre une fonction qui prendrait le code Morse en entrée et retournerait une chaîne lisible par un humain.

Par exemple :

decode_morse('.... . -.--   .--- ..- -.. .') devrait retourner "HEY JUDE"
NOTE : À des fins de codage, vous devez utiliser les caractères ASCII . et -, et non les caractères Unicode.

```python
MORSE_CODE = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_', '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'}
```

#### Solution :
```python
def decode_morse(morse_code):
    res = ""
    for w in morse_code.strip().split("   "):
        for l in w.split():
            res += MORSE_CODE[l]
        res += " "
    return res[:-1]
```

#### Test data :
```python
decode_morse('.... . -.--   .--- ..- -.. .') # -> 'HEY JUDE'
decode_morse('.-') # -> 'A'
decode_morse('.   .') # -> 'E E'
decode_morse('      ...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-  ') # -> 'SOS! THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.'
```