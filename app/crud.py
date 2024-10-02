from sqlalchemy.orm import Session
from . import models, schemas

def criar_usuario(db: Session, usuario: schemas.UsuarioCreate):
    db_usuario = models.Usuario(nome=usuario.nome, idade=usuario.idade)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def listar_usuarios(db: Session):
    return db.query(models.Usuario).all()

def obter_usuario(db: Session, usuario_id: int):
    return db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()
