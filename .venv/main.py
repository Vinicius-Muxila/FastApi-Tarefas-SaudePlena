from fastapi import FastAPI

app = FastAPI()

from auth_routes import auth_router
from tasks_routes import tasks_router

app.include_router(auth_router)
app.include_router(tasks_router)

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


# Para executar o servidor, use o comando:
# uvicorn main:app --reload
