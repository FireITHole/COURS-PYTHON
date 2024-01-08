from gpiozero import LED, Button
from signal import pause

led = LED(23)
button = Button(24)

while True:
    button.wait_for_active() # Méthode permettant d'attendre l'appui sur un boutton pour exécuter le reste du code (synchrone)
    print("Le bouton est pressé")    
    led.blink(.5, .5)
    button.wait_for_inactive()
    print("Le bouton est relaché")
    led.off()

""" button.when_activated = lambda: led.blink(.2, .2)
button.when_deactivated = led.off
 """

""" def button_press():
    led.blink(.2, .2)
    print("Le bouton est pressé")    

def button_release():
    led.off()
    print("Le bouton est relaché")

button.when_activated = button_press
button.when_deactivated = button_release """

pause()