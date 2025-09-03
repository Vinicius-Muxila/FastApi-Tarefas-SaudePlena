from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base

# cria a conexão com o banco de dados 
db = create_engine("sqlite:///banco.db")

# cria a base do banco de dados
Base = declarative_base()

# cria todas as tabelas do banco de dados

class User(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String(50))
    email = Column("email", String(100), nullable=False)
    senha = Column("senha", String(100))
    ativo = Column("ativo", Boolean)
    admin = Column("admin", Boolean, default=False)

    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin
    
# tarefas
# descrição das tarefas

# executa a criação dos metadados do seu banco (cria efetivamente o banco de dados)


