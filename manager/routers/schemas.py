from pydantic import BaseModel


class AddItem(BaseModel):
    x: int
    y: int


class MulItem(BaseModel):
    x: int
    y: int


class AddMulItem(BaseModel):
    x: int
    y: int
    z: int
