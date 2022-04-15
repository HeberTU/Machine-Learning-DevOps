# -*- coding: utf-8 -*-
"""Parameters and Input in FastAPI.

Created on: 4/14/2022
@author: Heber Trujillo <heber.trj.urt@gmail.com> 
Licence,
"""
from typing import Optional
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


class Message(BaseModel):
    message: str


app = FastAPI()


@app.post("/items/")
async def create_item(
        item: Item):
    return item


@app.get("/items/{item_id}", responses={404: {"model": Message}})
async def order_item(
        item_id: int,
        quantity: int
):
    if item_id == 27:
        return JSONResponse(
            status_code=404,
            content={"message": "Forbidden Item."})

    return {'item_id': item_id, 'quantity': quantity}
