from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.post("/login")
async def login(username: str, password: str): 
    """
    Simples endpoint de login que verifica se o nome de usuário e a senha são corretos.
    """  
    if username == "admin" and password == "password":
        return {"message": "Login successful"}
    return {"message": "Invalid credentials"}




