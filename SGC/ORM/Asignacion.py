__author__ = 'family'

from sqlalchemy import (Date)

from sqlalchemy.orm import sessionmaker



from basetest import *


Session = sessionmaker(bind=engine)

class Asignacion (Base):
    __tablename__ = 'asignacion'

    id_curso = Column(Integer, index=True, ForeignKey('cohorte.id_curso'), primary_key=True)
    id_cohorte = Column(Integer, index=True, ForeignKey('cohorte.id_cohorte'), primary_key=True)
    id_actividad =  Column(Integer, index=True, ForeignKey('actividades.id_actividad'), primary_key=True)
    fecha_hora  = Column (Date)
    
    


Base.metadata.create_all(engine)


'''session = Session()


session.add(user)
session.commit()'''

