Le projet est une application web moderne construite avec Python, Flask, et MongoDB.Le backend utilise Flask comme framework web, avec une base de données MongoDB pour stocker les données de manière flexible.

-Architecture:

--Backend (Flask):

---Le backend est construit avec Flask, un framework web minimaliste pour Python.
Deux routes principales sont définies pour les pages d'accueil et génériques.
Flask-PyMongo est utilisé pour interagir avec la base de données MongoDB.

---Base de Données (MongoDB):
MongoDB est choisi comme base de données non relationnelle en raison de sa flexibilité et de sa capacité à gérer des données semi-structurées.
Une seule collection est utilisée pour stocker les données, avec un schéma explicite adapté à l'application.

---Frontend (HTML/JavaScript):

    Les pages HTML sont rendues avec Flask, et les templates sont stockés dans un dossier appelé templates.
    Le frontend utilise HTML et éventuellement JavaScript pour rendre les pages dynamiques.

---Conteneurs Docker:

    Deux Dockerfiles sont utilisés. Un pour le backend (Flask) et un autre pour la base de données (MongoDB).
    Docker Compose est utilisé pour orchestrer les conteneurs, permettant une configuration et un déploiement faciles.

---Technologies Utilisées:

--Backend:
Python (Flask)
Flask-PyMongo pour la connexion à MongoDB
--Base de Données:
MongoDB
--Frontend:
HTML, éventuellement JavaScript
--Conteneurs:
Docker, Docker Compose
