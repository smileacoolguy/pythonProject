from fastapi import FastAPI, APIRouter, Query
from pydantic import BaseModel
from fastapi import  Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional
from fastApi_model.routes import jwt_token

router = APIRouter()


# app = FastAPI()
#
# # Pydantic model for request body
# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None
#
# # Root endpoint
# @app.get("/")
# def read_root():
#     return {"message": "Welcome to FastAPI!"}
#
# # Path parameter example
# @app.get("/hello/{name}")
# def say_hello(name: str):
#     return {"message": f"Hello, {name}!"}
#
# # POST endpoint to create an item
# @app.post("/items/")
# def create_item(item: Item):
#     total_price = item.price + (item.tax if item.tax else 0)
#     return {
#         "item_name": item.name,
#         "description": item.description,
#         "total_price": total_price
#     }
#
# # GET endpoint with path parameter
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "query": q}
#
#

##token




#############router


# Pydantic model for request body
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

# Root endpoint
@router.get("/")
async def read_root():
    return {"message": "Welcome to FastAPI!"}

# Path parameter example
@router.get("/hello/")
async def say_hello(name: str | None = Query(None, max_length=50, description="Search query for names"), optional: int = 10, token: str = Depends(jwt_token.oauth2_scheme)):
    username = jwt_token.verify_token(token)
    return {"message": f"Hello, {name}!"}

# POST endpoint to create an item
@router.post("/items/")
async def create_item(item: Item, token: str = Depends(jwt_token.oauth2_scheme)):
    username = jwt_token.verify_token(token)
    total_price = item.price + (item.tax if item.tax else 0)
    return {
        "item_name": item.name,
        "description": item.description,
        "total_price": total_price
    }

# GET endpoint with path parameter
@router.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None, token: str = Depends(jwt_token.oauth2_scheme)):
    username = jwt_token.verify_token(token)
    return {"item_id": item_id, "query": q}

"""
pip install fastapi uvicorn flask pinggy
uvicorn fastapi_sample:app --reload
http://127.0.0.1:8000/docs
uvicorn fastapi_sample:app --reload
ssh -p 443 -R0:localhost:8000 qr@a.pinggy.io
"""