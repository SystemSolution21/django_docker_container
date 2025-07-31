# Django Docker Container

## Django application run in Docker container

<br>

## Requirements

- Docker
- Python 3.13
- uv

<br>

## Create Virtual Environment and Activate

```pwsh
uv venv
or uv venv --python 3.13
.venv\Scripts\activate
```

<br>

## Dependencies Installation

```pwsh
uv sync
```

<br>

## Run Docker Container

- Build image:

```pwsh
docker build -t django-docker-container-image:v0.1.0 .
```

- Run container:

```pwsh
docker compose up -d
```

- Rebuild and run container:

```pwsh
docker compose up -d --build
```

<br>

## Generate secret key(if required)

```pwsh
uv run manage.py shell
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
exit()
```

<br>

## Database Migrations

```pwsh
uv run manage.py makemigrations
uv run manage.py migrate
```

<br>

## Run Django Application locally

```pwsh
uv run manage.py runserver
```
