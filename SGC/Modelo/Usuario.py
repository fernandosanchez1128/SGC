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

class Usuario (Base):
    __tablename__ = 'usuario'

    cedula = Column(String(40), primary_key=True)
    nombres = Column(String(50), index=True)
    apellidos = Column(String(50), index=True)
    direccion = Column(String(40), index=True)
    telefono = Column(String(40), index=True)
    correoElectronico = Column(String(40), index=True, nullable=False)
    fechaNacimiento = Column(Date, index=True)
    
    type = Column(String(50))

    __mapper_args__ = {
        'polymorphic_identity':'usuario',
        'polymorphic_on':type
    }

Base.metadata.create_all(engine)


'''session = Session()


session.add(user)
session.commit()'''
