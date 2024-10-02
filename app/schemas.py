from pydantic import BaseModel

class UsuarioBase(BaseModel):
    nome: str
    idade: int

class UsuarioCreate(UsuarioBase):
    pass

class Usuario(UsuarioBase):
    id: int

    class Config:
        orm_mode = True
