__author__ = 'family'

from sqlalchemy import (create_engine, Column, Date, Integer, ForeignKey, String, Table)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#engine = create_engine('postgresql://brayanrod:bryan1112@localhost:5432/sgc', echo=True)
#engine = create_engine('postgresql://braymrr:braymrr@pgsql/braymrr', echo=True)
#engine = create_engine('sqlite:///usuario.db', echo=True)
#Base = declarative_base()


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

