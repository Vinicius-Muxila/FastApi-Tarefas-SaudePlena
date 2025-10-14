from pydantic import BaseModel
from typing import Optional

class UsuarioSchema(BaseModel):
    nome: str
    email: str
    senha: str
    ativo: Optional[bool] 
    admin: Optional[bool]

    class Config:
        from_attributes = True
    
class TarefaSchema(BaseModel):
    usuario: int
    nome: str
    frequencia: str
    periodo: str
    descricao: Optional[str]
    status: Optional[str] = "PENDENTE"

    class Config:
        from_attributes = True
