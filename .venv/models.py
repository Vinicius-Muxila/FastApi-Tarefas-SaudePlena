from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base

# cria a conexão com o banco de dados 
db = create_engine("sqlite:///banco.db")

# cria a base do banco de dados
Base = declarative_base()

# cria todas as classes/tabelas do banco de dados
class Usuario(Base):
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
    
class Tarefa(Base):
    __tablename__ = "tarefas"

    # STATUS_TAREFAS = (
    #     ('PENDENTE', 'Pendente'),
    #     ('EM_ANDAMENTO', 'Em Andamento'),
    #     ('CONCLUIDA', 'Concluída'),
    # )

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column("status", String, default="PENDENTE")
    usuario = Column("usuario", ForeignKey("usuarios.id"))
    nome = Column("Nome", String(100))
    frequencia = Column("frequencia", String(20))
    periodo = Column("periodo", String(20))
    descricao = Column("descricao", String(200))

    def __init__(self, status="PENDENTE", usuario, nome, frequencia, periodo, descricao):
        self.status = status
        self.usuario = usuario
        self.nome = nome
        self.frequencia = frequencia
        self.periodo = periodo
        self.descricao = descricao
# descrição das tarefas

# executa a criação dos metadados do seu banco (cria efetivamente o banco de dados)


