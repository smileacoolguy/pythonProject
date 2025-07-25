from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional

from fastApi_model.routes import fastapi_sample, jwt_token


# Secret key to encode/decode JWT
version = "v1"
app = FastAPI()
#app.include_router(fastapi_sample.router, prefix=f"/api/{version}")
app.include_router(jwt_token.router, prefix=f"/jwt/{version}")
app.include_router(fastapi_sample.router, prefix=f"/jwt/{version}")

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}