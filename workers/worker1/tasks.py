from celery import Celery
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)

# create app
app = Celery('tasks')
# load config
app.config_from_object('config')

@app.task(name='worker1.add')
def add(x, y):
    return x + y