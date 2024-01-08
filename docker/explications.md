# Docker

### Définitions
**Docker** est un outil de **contenarisation d'applications** permettant de faire tourner des processus de façon dynamique et légère (similaire à une VM, mais sans besoin d'utiliser un hyperviseur).

### Cas pratiques
L'utilisation de **Docker** est utile dans de nombreuses situations. Autant en environnement de développement qu'en production, comme dans ces cas par exemple : 
- En environnement de développement afin de lancer rapidement une base de donnée, un serveur de fichier, un programme python...
- En production en tant que serveur de fichier, de base de donnée, de serveur back-end...

### Fonctionnement
**Docker** rend la gestion de processus et d'application relativement simple et dynamique via un **système d'image** et de **conteneurs**.
- **Une image** est un fichier contenant l'ensemble des variables, fichiers, processus devant être utilisés ou lancés dans le **conteneur** (un grand nombre d'images déjà créées sont disponibles en ligne ou directement via le client Windows/Mac ou via les lignes de commandes).
- **Un conteneur** est un environnement isolé géré par **Docker**. C'est dans un conteneur qu'une image est utilisée, et où un processus tourne (similaire à une VM en beaucoup moins lourd en terme de taille et de ressources utilisées).
- **Un réseau** est un environnement reliant plusieurs conteneurs via un protocole TCP/IP.
Par défaut, un conteneur ne retient pas les données créées après un redémarrage de conteneur. Autrement dit : **attention à ne pas éteindre un conteneur de base de donnée si celui-ci n'as pas un volume définit**
- **Un Volume** est une association de stockage entre le conteneur et un espace de stockage réel (sur le disque de l'ordinateur host). On peut par exemple associer un fichier *DB* sur l'ordinateur host qui contiendra tout les fichiers du conteneur à son point d'accès *./DB*.

Chaque conteneur est **isolé** des autres conteneurs. Cependant, un **réseau privé** peut établir une connexion entre ces derniers permettant l'échange de données (cas pratique : échanges de données entre un serveur et une base de donnée).

### Documentation
Disponible sur le support de [Docker](https://docs.docker.com/?_gl=1*16b3y1f*_ga*ODQzMTM5NTEzLjE3MDE0NDYxODg.*_ga_XJWPQMJYHQ*MTcwMTc4NDE1My4zLjEuMTcwMTc4NDMwNC4yMC4wLjA.)

### Installation
- Windows/Mac/Linux : Suivre instructions sur le site de [Docker](https://www.docker.com/products/docker-desktop/)
- Ubuntu server via script d'installation :
    ```
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
    ```

### Docker Compose
**Docker Compose** est un plugin de **Docker** permettant de créer des fichiers de configuration pour lancer plusieurs conteneurs en même temps, ainsi que définir des variables d'environnements dans un fichier et non via des commandes. Cet outil est particulièrement puissant car il permet de lancer plusieurs applications en même temps via 1 commande, et les arrêter via une autre. Docker compose permet également la gestion des **réseaux Docker** et des **Volumes**. Docker Compose est inclut dans l'installation de *Docker Desktop* par défaut. Les commandes docker-compose commencent toujours par `docker-compose` ou `docker compose` (en fonction de l'installation)

### Création d'image Docker
Pour créer facilement une image **Docker**, on utilise la commande : `docker init`

### Création d'un fichier docker-compose
Un fichier docker-compose est un fichier yaml devant s'appeler `docker-compose.yaml` (Docker s'attend à ce nom de fichier). Ce fichier définit les application ainsi que les options à utiliser pour chacunes d'entres elles. Docker utilisera ce fichier pour créer des conteneurs, des volumes, des réseaux, et attribuer les variables d'environnement aux différentes applications (nommés *services* dans le fichier).

### Commandes utiles
- `docker ps` => liste les conteneurs créés ou en cours de fonctionnement
- `docker init` => lance le script de création d'images
- `docker-compose up --build -d` => créer et démarre les conteneurs listés dans un fichier `docker-compose.yaml`. Le flag `--build` indique à Docker qu'il faut construire (ou re-construire) l'image avant de la lancer. Le flag `-d` permet de lancer les applications en mode *détaché*. Les flags `--build` et `-d` sont optionnels
- `docker-compose down` => arrête et supprime les conteneurs défini par un fichier `docker-compose.yaml`
