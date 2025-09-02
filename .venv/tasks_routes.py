from fastapi import APIRouter

tasks_router = APIRouter(prefix="/tarefas", tags=["tarefas"])

@tasks_router.get("/tarefas")
async def mostrar_tarefas():
    return {"tasks": ["Tarefa 1", "Tarefa 2", "Tarefa 3"]}