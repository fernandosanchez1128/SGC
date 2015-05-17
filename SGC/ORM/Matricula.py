from LeaderTeacher import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Float, ForeignKeyConstraint
from Curso import *
from Cohorte import *
from basetest import *


class Matricula(Base):
    __tablename__ = 'matricula'
    cedula_lt = Column(String(40), ForeignKey('leaderteacher.cedula'), primary_key=True)
    id_curso = Column(Integer, primary_key=True)
    id_cohorte = Column(Integer, primary_key=True)
    nota_definitiva = Column(Float)
    __table_args__ = (ForeignKeyConstraint([id_curso, id_cohorte], ['cohorte.id_curso', 'cohorte.id_cohorte']), {})


Base.metadata.create_all(engine)
'''
Session = sessionmaker(bind=engine)
session = Session()
mat = Matricula(cedula_lt = '1144123', id_curso=78, id_cohorte = 654)
session.add(mat)
session.commit()
'''