# Django-CRM

## Create a python virtual environment

```bash
python3 -m venv venv
```

## Activate the virtual environment

```bash
source venv/bin/activate
```

## Install requirements

```bash
python3 -m pip install -r requirements.txt
```

## Configure Environment variables

Create a .env file in the root dir of the project and set the following env variables.

```bash
SECRET_KEY = your-secret-key
DEBUG = True
```

### Run DB migrations

```bash
python3 manage.py migrate --settings=config.settings.local
```

### Run project server on local

```bash
python3 manage.py runserver --settings=config.settings.local
```

On your browser, go to <http://localhost:8000>
