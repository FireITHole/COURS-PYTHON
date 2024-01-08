from gpiozero import LED # On importe la méthode LED de la librairie gpiozero
from time import sleep # On importe la méthode sleep de la librairie time
from signal import pause

led = LED(23) # On initialise une instance d'objet LED nommée led et on lui passe l'argument 23 qui est le numéro GPIO du pin de la LED

while True: # Pour toujours
    led.on() # On allume la LED
    sleep(1) # On attend 1 seconde
    led.off() # On éteint la LED
    sleep(1) # On attend 1 seconde

# Autre méthodes :
""" while True: # Pour toujours
    led.toggle() # On change l'état de la LED en !LED
    sleep(1) # On attend 1 seconde
 """

""" led.blink(.5, .5) # On utilise la fonction blink pour faire clignoter la LED (premier argument -> Durée d'allumage, deuxième -> Durée éteinte)
pause() """