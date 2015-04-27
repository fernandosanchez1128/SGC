__author__ = 'cenesis'

from Usuario import Usuario

from sqlalchemy import (create_engine, Column, Date, Integer, ForeignKey, String, Table)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

#engine = create_engine('postgresql://brayanrod:bryan1112@localhost:5432/sgc', echo=True)
#engine = create_engine('postgresql://braymrr:braymrr@pgsql/braymrr', echo=True)
#engine = create_engine('sqlite:///masterteacher.db', echo=True)
#Base = declarative_base()


from basetest import *


class MasterTeacher(Usuario, Base):
    __tablename__ = 'masterteacher'

    cedula = Column(String(40), ForeignKey('usuario.cedula'), primary_key=True)
    
    __mapper_args__ = {
        'polymorphic_identity':'masterteacher',
    }


Base.metadata.create_all(engine)


