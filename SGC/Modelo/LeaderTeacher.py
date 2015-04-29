__author__ = 'cenesis'

from Usuario import Usuario

from sqlalchemy import (create_engine, Column, Date, Integer, ForeignKey, String, Table)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


#engine = create_engine('postgresql://brayanrod:bryan1112@localhost:5432/sgc', echo=True)
#engine = create_engine('postgresql://braymrr:braymrr@pgsql/braymrr', echo=True)
#engine = create_engine('sqlite:///leaderteacher.db', echo=True)
#Base = declarative_base()


from basetest import *
class LeaderTeacher(Usuario, Base):
    __tablename__ = 'leaderteacher'

    cedula = Column(String(40), ForeignKey('usuario.cedula'), primary_key=True)
    sede = Column(String(40))
    institucion = Column(String(100))
    codigoInstitucion = Column(String(40))
    grado = Column(Integer)
    departamentoSecretaria= 
    municipioSecretaria = ""
    tutorProgramaPTA = False
    usuarioColombiaAprende = False
    __mapper_args__ = {
        'polymorphic_identity':'leaderteacher',
    }


Base.metadata.create_all(engine)
    


