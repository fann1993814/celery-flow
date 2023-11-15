from fastapi import APIRouter

from celery import Celery, chain, Signature
from .schemas import AddItem, MulItem, AddMulItem
from . import celeryconfig

router = APIRouter()

app = Celery('tasks')
app.config_from_object(celeryconfig)


@router.post("/add", tags=["task"])
async def add(item: AddItem) -> int:
    res = Signature('worker1.add', kwargs={
        "x": item.x, 'y': item.y}, queue='worker1').apply_async()
    return res.get()


@router.post("/mul", tags=["task"])
async def mul(item: MulItem) -> int:
    res = Signature('worker2.mul', kwargs={
        'x': item.x, 'y': item.y}, queue='worker2').apply_async()
    return res.get()


@router.post("/add-then-mul", tags=["task"])
async def add_then_mul(item: AddMulItem) -> int:
    res = chain([
        Signature('worker1.add', kwargs={
                  "x": item.x, 'y': item.y}, queue='worker1'),
        Signature('worker2.mul', kwargs={'y': item.z}, queue='worker2')]).apply_async()
    return res.get()
