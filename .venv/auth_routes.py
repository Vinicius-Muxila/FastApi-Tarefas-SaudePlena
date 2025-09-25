from fastapi import APIRouter, Depends, HTTPException
from models import Usuario, db
from dependencies import pegar_sessao
from main import bcrypt_context 
from schemas import UsuarioSchema
from sqlalchemy.orm import sessionmaker

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def home(): 
    """
    Essa é a rota padrão de autenticação do nosso sistema.
    """  
    return {"message": "você acessou a rota padrão de autenticação", "autenticado": False}

@auth_router.post("/criar_conta")
async def criar_conta(nome: str, email: str, senha: str, session = Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email == email).first()
    if usuario:
        return {"mensagem": "já existe um usuário com esse email"}
    else:
        novo_usuario = Usuario(nome, email, senha)
        session.add(novo_usuario)
        session.commit()
        return {"mensagem": f"Usuário cadastrado com sucesso! {email}"}
    


# @auth_router.post("/criar_conta")
# async def criar_conta(usuario_schema: UsuarioSchema, session = Depends(pegar_sessao)):
#     usuario_existente = session.query(Usuario).filter(Usuario.email == usuario_schema.email).first()
#     if Usuario:
#         # ja existe usuario com esse email
#         raise HTTPException(status_code=400, detail="já existe um usuário com esse email")
#     else:
#         senha_criptografada = bcrypt_context.hash(usuario_schema.senha)
#         novo_usuario = Usuario(usuario_schema.nome, usuario_schema.email, senha_criptografada, usuario_schema.ativo, usuario_schema.admin)
#         session.add(novo_usuario)
#         session.commit()
#         return {"mensagem": f"usuario cadastrado com sucesso!{usuario_schema.email}"}




