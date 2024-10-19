# settings_prod.py

from .settings_base import *

# Désactiver DEBUG en production pour éviter les fuites d'informations
DEBUG = False

# Hôtes autorisés en production
ALLOWED_HOSTS = ['myapp.com', 'www.myapp.com']

# Clé secrète tirée des variables d'environnement pour la production
SECRET_KEY = config('SECRET_KEY')

# Sécurisation SSL en production
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Paramètres de la base de données en production (configurés via .env)
DATABASES['default'].update({
    'HOST': config('DB_HOST'),
})

# Paramètres spécifiques à la production (logs, sécurité, etc.)...