"""
WSGI config for walletcreatures project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
if os.getenv("ENV") == "Heroku":
    print('prodsettings enabled')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'walletcreatures.settings.prod')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'walletcreatures.settings.dev')

application = get_wsgi_application()
