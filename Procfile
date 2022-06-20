release: python manage.py loaddata data.json
release: python manage.py migrate
web: gunicorn walletcreatures.wsgi --log-file -
