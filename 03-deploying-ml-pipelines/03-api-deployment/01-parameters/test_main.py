# -*- coding: utf-8 -*-
"""Local API Testing.

Created on: 4/15/2022
@author: Heber Trujillo <heber.trj.urt@gmail.com> 
Licence,
"""
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

def test_order_item():
    response = client.get("/items/42?quantity=1")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "quantity": 1}
