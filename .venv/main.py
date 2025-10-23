from fastapi import FastAPI
from passlib.context import CryptContext 
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = OS.getenv("ALGORITHM")

app = FastAPI()

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

from auth_routes import auth_router
from tasks_routes import tasks_router

app.include_router(auth_router)
app.include_router(tasks_router)

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


# Para executar o servidor, use o comando:
# uvicorn main:app --reload
