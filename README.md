# Celery-Flow Example

- This Repo apply simple task-queue cases with [Celery](https://docs.celeryq.dev/en/stable/).
- The Celery Queue Backend use [Redis](https://redis.io).

## Install
```sh
cd manager
pip install -r requirements.txt
```

## Run the app

### Run Redis and Workers in Docker
```sh
docker-compose -d up
```

### Run manager
```sh
cd manager
uvicorn main:app --reload
```

## Development
### Check Redis
  - [Medis](https://getmedis.com)
### Local Swagger API
  - http://127.0.0.1:8000/docs/