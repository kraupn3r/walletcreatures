
release: python manage.py migrate
release: python manage.py loaddata data.json
web: gunicorn walletcreatures.wsgi --log-file -
