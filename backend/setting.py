# backend/settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'DB_USER',
        'USER': 'DB_USER',
        'PASSWORD': 'DB_PASSWORD',
        'HOST': 'db',
        'PORT': '5432',
    }
}

# Ajouter Django Allauth dans les applications installées
INSTALLED_APPS = [
    # Autres applications
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # Pour GraphQL
    'graphene_django',
    # Pour l'API REST
    'rest_framework',
    'api',  # Ton application
]

# Configuration GraphQL
GRAPHENE = {
    'SCHEMA': 'backend.schema.schema'  # L'emplacement de ton schéma GraphQL
}

SITE_ID = 1  # Pour allauth