from sqlalchemy import (create_engine, Column, Date, Integer, ForeignKey,
    String, Table)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

#engine = create_engine('mysql://fernando:fernando1128@localhost/test', echo=True)
engine = create_engine('sqlite:///cursos.db', echo=True)
Base = declarative_base()


class Curso(Base):
    __tablename__ = 'curso'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(40), index=True, nullable=False)
    descripcion = Column(String(120), index=True)
 

    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion= descripcion
        
Base.metadata.create_all(engine)
