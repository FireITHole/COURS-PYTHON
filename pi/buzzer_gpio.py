from gpiozero import Buzzer, Button

button = Button(24) # Brancher le boutton sur le pin 24 (input Pullup)
buzzer = Buzzer(23) # Brancher le buzzer sur le pin 23

while True:
    button.wait_for_active()
    buzzer.on()
    button.wait_for_inactive()
    buzzer.off()