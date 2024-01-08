### Création d'un service pour l'API (ou l'app Web)

Nous allons utiliser les services systemd d'Ubuntu afin de faire tourner notre application et la lancer au démarrage du système.

### Création du fichier service

Dans un premier temps nous devons créer le fichier _service_ contenant les options relatives à notre application. Nous allons l'appeler `flask.service` et l'éditer au chemin `/etc/systemd/system/` :

```
[Unit]
Description=Flask App
After=network.target

[Service]
User=fireithole
WorkingDirectory=/home/fireithole/python/api
ExecStart=/usr/bin/python3 /home/fireithole/python/api/web.py
Restart=always

[Install]
WantedBy=multi-user.target
```

### Installation et démarrage

Nous allons ensuite lancer ces différentes commandes :

```
sudo systemctl daemon-reload
sudo systemctl enable flask.service
sudo systemctl start flask.service
```

Ces commandes vont :

1. Recharger les services disponibles
2. Activer notre service au démarrage
3. Lancer notre service

### Vérifier le déploiement

Nous allons maintenant vérifier le bon fonctionnement de notre App en lançant la commande suivante :
`sudo systemctl status flask.service`
Si `active (running)` apparaît à côté de `Active :`, l'application s'est alors bien lancé.

### Commandes utiles

Voici quelques commandes à connaître pour gérer un service systemd :

-   `sudo systemctl start [service]` : Permet de lancer un service
-   `sudo systemctl stop [service]` : Permet d'arrêter un service
-   `sudo systemctl restart [service]` : Permet de relancer un service
-   `sudo systemctl status [service]` : Permet de vérifier l'état du service
-   `sudo systemctl enable [service]` : Permet de lancer le service au démarrage du système
-   `sudo systemctl disable [service]` : Permet de ne pas lancer le service au démarrage du système
