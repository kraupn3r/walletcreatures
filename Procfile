
release: python manage.py makemigrations && python manage.py migrate && python manage.py loaddata data.json
web: gunicorn walletcreatures.wsgi --log-file -
