from fastapi import FastAPI

from routers import tasks

app = FastAPI(title='Celery Simple Examples')

app.include_router(tasks.router, prefix="/tasks")
