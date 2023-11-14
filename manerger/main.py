from celery import Celery, chain, Signature

app = Celery('tasks')

# load config
app.config_from_object('celeryconfig')


task_add = Signature('worker1.add', kwargs={"x": 2, 'y': 3}, queue='worker1')
res = task_add.apply_async()

print(res.get())

task_mul = Signature('worker2.mul', kwargs={
                     'x': 5, 'y': 10}, queue='worker2')
res = task_mul.apply_async()

print(res.get())

chained_tasks = chain([
    Signature('worker1.add', kwargs={"x": 2, 'y': 3}, queue='worker1'),
    Signature('worker2.mul', kwargs={'y': 5}, queue='worker2'),
])

res = chained_tasks.apply_async()

print(res.get())
