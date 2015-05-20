__author__ = 'family'

from sqlalchemy import (create_engine, Column, Date, Integer, ForeignKey, String, ForeignKeyConstraint, Table)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import DateTime

#engine = create_engine('postgresql://brayanrod:bryan1112@localhost:5432/sgc', echo=True)
#engine = create_engine('postgresql://braymrr:braymrr@pgsql/braymrr', echo=True)
#engine = create_engine('sqlite:///usuario.db', echo=True)
#Base = declarative_base()
from Curso import Curso
from Actividades import Actividades
from basetest import *


Session = sessionmaker(bind=engine)

class Asignacion (Base):
    __tablename__ = 'asignacion'

    id_curso = Column(Integer, index=True, primary_key=True)
    id_cohorte = Column(Integer, index=True, primary_key=True)
    id_actividad =  Column(Integer, index=True, primary_key=True)
    fecha_hora  = Column (DateTime)
    __table_args__ = (ForeignKeyConstraint([id_actividad, id_curso],['actividades.id_actividad','actividades.id_curso']),{})
    __table_args__ = (ForeignKeyConstraint([id_curso, id_cohorte],['cohorte.id_curso','cohorte.id_cohorte']),{})

    
    


Base.metadata.create_all(engine)


'''session = Session()


session.add(user)
session.commit()'''

