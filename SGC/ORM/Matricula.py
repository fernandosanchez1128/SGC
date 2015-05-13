from LeaderTeacher import *
from sqlalchemy import (ForeignKeyConstraint, Float)
from basetest import *


class Matricula(Base):
    __tablename__ = 'matricula'
    cedula_lt = Column(String(40), primary_key=True)
    id_curso = Column(Integer, primary_key=True)
    id_cohorte = Column(Integer, primary_key=True)
    ForeignKeyConstraint(['cedula_lt', 'id_curso', 'id_cohorte'],
                         ['leaderteacher.cedula', 'cohorte.id_curso', 'cohorte.id_cohorte'])
    nota_definitiva = Column(Float)


Base.metadata.create_all(engine)
