__author__ = 'family'
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
    cohortes = relationship("Cohorte",cascade="all, delete, delete-orphan", primaryjoin="and_(Curso.id==Cohorte.id_curso) ")
    actividades = relationship("Actividades",cascade="all, delete, delete-orphan", primaryjoin="and_(Curso.id==Actividades.id_curso) ")
    
 
from Cohorte import Cohorte
from Actividades import Actividades

Base.metadata.create_all(engine)
#~ Session = sessionmaker(bind=engine)
#~ session = Session()
#~ curso = Curso (nombre = "curso2")
#~ cohorte1 = Actividades (nombre = 'act',ponderado= 0.5)
#~ cohorte2 = Actividades (nombre = 'act',ponderado= 0.5)
#~ curso.actividades.append (cohorte1)
#~ curso.actividades.append (cohorte2)
#~ session.add(curso)
#~ session.commit()
#~ session.close()
#~ print ("consulta")
#~ curso2 = session.query(Curso).filter_by (nombre = "espanol").first()
#~ print curso2
#~ print curso2.cohortes
