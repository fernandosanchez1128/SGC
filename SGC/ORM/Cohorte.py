__author__ = 'family'

from sqlalchemy import (Sequence, UniqueConstraint, Index,Date)

from basetest import *


Column(Integer, Sequence('sec_cohorte'), primary_key=True)


class Cohorte(Base):
    __tablename__ = 'cohorte'

    id_curso = Column(Integer, ForeignKey('curso.id'), primary_key=True)
    id_cohorte = Column(Integer, Sequence('sec_cohorte'), primary_key=True, unique=True)
    ano = Column(Integer, primary_key=True)
    semestre = Column(Integer, primary_key=True)
<<<<<<< .merge_file_YWEsMJ
    fecha_inicio = Column(Date)
    fecha_fin = Column(Date)

=======
    fecha_inicio = Column(Date,nullable=True)
    fecha_fin = Column(Date,nullable=True)
    __table_args__ = (UniqueConstraint('id_curso', 'id_cohorte', name='unique'),)
>>>>>>> .merge_file_8WZOTJ
    def __repr__(self):
        codigo = str(self.id_cohorte)
        return codigo

Base.metadata.create_all(engine)


'''
Session = sessionmaker(bind=engine)
session = Session()
#~ curso = Curso (nombre = "espanol")
cohorte1 = Cohorte (id_curso=122,id_cohorte =1,ano = 2015,semestre = 2)
#~ cohorte2 = Cohorte (ano = 2015,semestre = 1)
#~ curso.cohortes.append (cohorte1)
#~ curso.cohortes.append (cohorte2)
session.add(cohorte1)
session.commit()
session.close()
#~ print ("consulta")
#~ curso2 = session.query(Curso).filter_by (nombre = "espanol").first()
#~ print curso2
#~ print curso2.cohortes
'''