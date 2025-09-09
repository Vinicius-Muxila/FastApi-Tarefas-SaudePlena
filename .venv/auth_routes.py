from fastapi import APIRouter, Depends
from models import User, db
from dependencies import pegar_sessao

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def home(): 
    """
    Essa é a rota padrão de autenticação do nosso sistema.
    """  
    return {"message": "você acessou a rota padrão de autenticação", "autenticado": False}

@auth_router.post("/criar_conta")
async def criar_conta(nome: str, email: str, senha: str, session = Depends(pegar_sessao)):
    User = session.query(User).filter(User=email == email).first()
    if User:
        # ja existe usuario com esse email
        return {"mensagem": "ja existe um usuario com esse email"}
    else:
        novo_usuario = User(nome, email, senha)
        session.add(novo_usuario)
        session.comit()
        return {"mensagem": "usuario cadastrado com sucesso!"}




