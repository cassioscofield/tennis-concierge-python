Criar projeto
```
python3 -m venv venv
django-admin startproject tennisconcierge
pip freeze > requirements.txt
```

Instanciar banco de dados
```
python3 manage.py migrate
python3 manage.py createsuperuser
```

Criar modulos
```
python3 manage.py startapp reservas
python3 manage.py makemigrations
```

Rodar projeto
````
pip install
python3 manage.py runserver
```
