from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session  
from dependencies import pegar_sessao
from schemas import TarefaSchema


tasks_router = APIRouter(prefix="/tarefas", tags=["tarefas"])

@tasks_router.get("/tarefas")
async def mostrar_tarefas():
    return {"tasks": ["Tarefa 1", "Tarefa 2", "Tarefa 3"]}

@tasks_router.post("/tarefa")
async def criar_tarefa(tarefa_schema: TarefaSchema, session: Session = Depends(pegar_sessao)):
    nova_tarefa = Tarefa(usuario=tarefa_schema.id_usuario, nome=tarefa_schema.nome, frequencia=tarefa_schema.frequencia, periodo=tarefa_schema.periodo, descricao=tarefa_schema.descricao)
    session.add(nova_tarefa)
    session.commit()
    return {"mensagem": "tarefa criada com sucesso!"}      