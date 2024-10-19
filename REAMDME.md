# MyApp

Ce projet utilise plusieurs technologies modernes pour la création d'une application web, notamment Django, PostgreSQL, React, Docker, et plus encore. Ce document fournit une liste de commandes utiles pour interagir avec ces outils.

## Prérequis

Avant de commencer, assurez-vous que les éléments suivants sont installés sur votre machine :
- Python 3.x
- Docker
- Node.js & npm
- PostgreSQL
- pgAdmin (via Docker ou installé localement)

## Structure du Projet
/backend        # Django backend
/frontend       # React frontend
## Installation

### 1. Backend (Django)

- Créer et activer un environnement virtuel Python :
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate  # Sur macOS/Linux
  .venv\Scripts\activate     # Sur Windows

  	•	Installer les dépendances du projet Django :
    pip install -r backend/requirements.txt
    	•	Migrer la base de données :
        python backend/manage.py migrate
        	•	Démarrer le serveur Django :
            python backend/manage.py runserver

    •	Naviguer vers le dossier frontend et installer les dépendances :
        cd frontend
        npm install
    	•	Lancer l’application React en mode développement :
        npm start
    
Utilisation de PostgreSQL

1. Démarrer PostgreSQL avec Docker

    •	Créer et lancer un container PostgreSQL :
docker run --name my_postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres
	•	Lister les containers Docker pour vérifier que PostgreSQL fonctionne :    
docker ps
	•	Se connecter au shell PostgreSQL à l’intérieur du container :
    docker exec -it my_postgres psql -U postgres

2. pgAdmin via Docker

	•	Créer un container Docker pour pgAdmin :
    docker run -p 80:80 \
  -e 'PGADMIN_DEFAULT_EMAIL=admin@example.com' \
  -e 'PGADMIN_DEFAULT_PASSWORD=admin' \
  --name pgadmin \
  -d dpage/pgadmin4
  	•	Accéder à pgAdmin via http://localhost:80 et ajouter votre serveur PostgreSQL.

Gestion des containers Docker

	•	Construire l’image Docker :
    docker build -t mon_projet .
    •	Démarrer un container :
    docker-compose up
    •	Arrêter un container :
    docker-compose down
    •	Supprimer tous les containers (attention, cela supprime tous les containers actifs et inactifs) :
    docker rm $(docker ps -a -q)

Autres commandes utiles

Django

	•	Créer une nouvelle migration après avoir modifié les modèles :
    python backend/manage.py makemigrations
    	•	Appliquer les migrations à la base de données :
        python backend/manage.py migrate
        	•	Créer un super utilisateur pour accéder à l’admin de Django :
            python backend/manage.py createsuperuser
React

	•	Compiler l’application pour la production :
    npm run build
    •	Tester l’application avec Jest (ou tout autre framework de test) :
    npm test

Déploiement

	•	Le projet utilise Docker pour simplifier le déploiement. Vous pouvez créer et lancer vos services avec Docker Compose :
    docker-compose up --build