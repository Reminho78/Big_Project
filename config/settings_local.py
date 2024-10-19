# settings_local.py

from .settings_base import *

# Activer le mode DEBUG en développement
DEBUG = True

# Hôtes autorisés (pour éviter les erreurs en développement)
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Utiliser la base de données locale (par exemple avec Docker)
DATABASES['default'].update({
    'HOST': 'db',  # Nom du service Docker pour la base de données
})

# Fichiers statiques en développement
STATIC_URL = '/static/'

# Clé secrète pour le développement
SECRET_KEY = 'dev-secret-key'

# Autres configurations spécifiques au développement...