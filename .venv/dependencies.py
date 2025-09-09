from models import db
from sqlalchemy.orm import sessionmaker

def pegar_sessao():
    try:
        session = sessionmaker(bind=db)
        session = session()
        yield session
    finally:
        session.close()