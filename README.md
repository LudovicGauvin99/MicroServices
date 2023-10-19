Le projet est une application web moderne construite avec Python, Flask, et MongoDB.Le backend utilise Flask comme framework web, avec une base de données MySQL pour structuré les données.

-Architecture:

--Backend (Flask):

---Le backend est construit avec Flask, un framework web minimaliste pour Python.
Deux routes principales sont définies pour les pages d'accueil et génériques.

---Base de Données (MySQL):

---Frontend (HTML/JavaScript):

    Les pages HTML sont rendues avec Flask, et les templates sont stockés dans un dossier appelé templates.
    Le frontend utilise HTML et éventuellement JavaScript pour rendre les pages dynamiques.

---Conteneurs Docker:

    Deux Dockerfiles sont utilisés. Un pour le backend (Flask) et un autre pour la base de données (MySQL).
    Docker Compose est utilisé pour orchestrer les conteneurs, permettant une configuration et un déploiement faciles.

---Technologies Utilisées:

--Backend:
Python (Flask)
Flask-PyMongo pour la connexion à MySQL
--Base de Données:
MySQL
--Frontend:
HTML, éventuellement JavaScript
--Conteneurs:
Docker, Docker Compose
