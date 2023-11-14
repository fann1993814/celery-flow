from celery import Celery, chain, Signature

app = Celery('tasks')

# load config
app.config_from_object('celeryconfig')

chained_tasks = chain([
    Signature('worker1.add', kwargs={"x": 2, 'y': 3}, queue='worker'),
    Signature('worker2.mul', kwargs={'y': 5}, queue='worker'),
])


res = chained_tasks.apply_async()

print(res.get())
