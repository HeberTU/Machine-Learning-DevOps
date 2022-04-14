# -*- coding: utf-8 -*-
"""Parameters and Input in FastAPI.

Created on: 4/14/2022
@author: Heber Trujillo <heber.trj.urt@gmail.com> 
Licence,
"""
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()


@app.post("/items/")
async def create_item(
        item: Item):
    return item


@app.get("/items/{item_id}")
async def order_item(
        item_id: int, quantity: int):
    return {'item_id': item_id, 'quantity': quantity}