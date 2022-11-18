# Começando com Django
Acesse a pasta do projeto em um terminal, e ative venv:
source venv/bin/activate


# Rode migrations para criar um banco.
python manage.py migrate


## Iniciar o projeto
python manage.py runserver

## na Web
Para visualizar no navegador, acesse [http://localhost:8000/api/items/]

## modo Admin
Crie um usuario:
./manage.py createsuperuser

Para utilizar o modo Admin, acesse [http://localhost:8000/admin/]

