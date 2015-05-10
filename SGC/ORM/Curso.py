from sqlalchemy import (create_engine, Column, Date, Integer, ForeignKey, String, Table,Sequence)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


from basetest import *
Column(Integer, Sequence('sec_curso'), primary_key=True)


class Curso(Base):
    __tablename__ = 'curso'
    id = Column(Integer,Sequence('sec_curso'), primary_key=True)
    nombre = Column(String(40), index=True, nullable=False,unique = True)
    descripcion = Column(String(120), index=True)
    cohortes = relationship("Cohorte", backref='curso',cascade="all, delete, delete-orphan")
    
 

        
Base.metadata.create_all(engine)
