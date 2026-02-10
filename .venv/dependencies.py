from fastapi import Depends
from models import db
from sqlalchemy.orm import sessionmaker, Session
from models import Usuario

def pegar_sessao():
    try:
        session = sessionmaker(bind=db)
        session = session()
        yield session
    finally:
        session.close()


def verificar_token(token, session: Session = Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.id==1).first()
    return usuario