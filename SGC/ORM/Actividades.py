__author__ = 'family'

from sqlalchemy import (create_engine, Column, Date, Integer, ForeignKey,ForeignKeyConstraint, String, Table,Sequence,
                        Float)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from basetest import *
from MasterTeacher import MasterTeacher

Column(Integer, Sequence('sec_actividad'), primary_key=True)


class Actividades (Base):
    __tablename__ = 'actividades'

    id_curso = Column(Integer, ForeignKey('curso.id'), primary_key=True)
    id_actividad =  Column(Integer,Sequence('sec_actividad'), primary_key=True)
    nombre = Column(String(20), unique=True)
    ponderado = Column(Float)
#~ Session = sessionmaker(bind=engine)
#~ session = Session()
#~ curso = Curso (nombre = "espanol")
#~ cohorte1 = Cohorte (ano = 2015,semestre = 1)
#~ cohorte2 = Cohorte (ano = 2015,semestre = 1)
#~ curso.cohortes.append (cohorte1)
#~ curso.cohortes.append (cohorte2)
#~ session.add(curso)
#~ session.commit()
#~ session.close()
#~ print ("consulta")
#~ curso2 = session.query(Curso).filter_by (nombre = "espanol").first()
#~ print curso2
#~ print curso2.cohortes

Base.metadata.create_all(engine)


'''session = Session()


session.add(user)
session.commit()'''

