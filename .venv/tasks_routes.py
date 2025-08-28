from fastapi import APIRouter

tasks_router = APIRouter(prefix="/tasks", tags=["tasks"])

@tasks_router.get("/tarefas")
def get_tasks():
    return {"tasks": ["Tarefa 1", "Tarefa 2", "Tarefa 3"]}