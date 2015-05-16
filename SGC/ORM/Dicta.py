
from MasterTeacher import MasterTeacher
from sqlalchemy import (create_engine, Column, Date, Integer, ForeignKey, ForeignKeyConstraint, String, Table)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Curso import Curso
from Cohorte import Cohorte
from basetest import *


class Dicta (Base):
    __tablename__ = 'dicta'
    cedula_mt = Column(String(40),ForeignKey('masterteacher.cedula'),primary_key=True)
    id_curso = Column(Integer,primary_key=True)
    id_cohorte = Column(Integer, primary_key=True)
    __table_args__ = (ForeignKeyConstraint([id_curso, id_cohorte],['cohorte.id_curso','cohorte.id_cohorte']),{})



Base.metadata.create_all(engine)