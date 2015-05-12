__author__ = 'family'

from sqlalchemy import (create_engine, Column, Date, Integer, ForeignKey,ForeignKeyConstraint, String, Table,Sequence)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from basetest import *
from MasterTeacher import MasterTeacher
Column(Integer, Sequence('sec_cohorte'), primary_key=True)

class Cohorte (Base):
    __tablename__ = 'cohorte'

    id_curso = Column(Integer, ForeignKey('curso.id'), primary_key=True)
    id_cohorte = Column(Integer, Sequence('sec_cohorte') , primary_key=True)
    ano = Column(Integer, primary_key=True)
    semestre = Column(Integer, primary_key=True)
    
    def __repr__(self):
		codigo = str (self.id_cohorte)
		return codigo



Base.metadata.create_all(engine)
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
