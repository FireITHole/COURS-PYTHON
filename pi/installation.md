### Version

Dernière LTS : Ubuntu Server 22.04.3 LTS (64-BIT)

### Installation

-   Programmer wifi / ssh si besoin (raccourci ctrl + shift + x sur Pi imager)
-   Une fois Pi démarré et connecté au réseau, passage de l'ip en static

### Commandes

-   Update la Pi : `sudo apt-get update && sudo apt-get upgrade -y`
-   Redémarrer la Pi : `sudo reboot`

### gpiozero

-   La librairie pour contrôler les pins de la Pi avec Python : [Lien tutorial](https://projects.raspberrypi.org/en/projects/physical-computing)

### RPi.GPIO

-   Une autre librairie pour gérer les pins de la Pi (plus de contrôle mais plus complexe) : `pip3 install rpi.gpio`
