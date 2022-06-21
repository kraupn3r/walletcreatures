# Wallet Creatures Django project
This project is a portfolio stylized as a Gameboy game.

Preview:

https://walletcreatures.herokuapp.com



Requirements:

```
asgiref==3.5.2
Django==4.0.4
djangorestframework==3.13.1
pytz==2022.1
sqlparse==0.4.2
tzdata==2022.1

```

Setup Django project :

```
git clone https://github.com/kraupn3r/walletcreatures

sudo apt install python3-venv

cd intranet-project

mkdir venv

python3 -m venv venv/walletcreatures

source venv/walletcreatures/bin/activate

pip install -r requirements.txt

```
Perform database migration :

```
python manage.py makemigrations

python manage.py migrate

python manage.py loaddata data.json

```

Start the development server :

```
python manage.py runserver
```

Visit the local development server at `127.0.0.1:8000` to test the site.
