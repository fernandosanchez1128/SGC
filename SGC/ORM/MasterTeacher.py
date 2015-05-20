__author__ = 'cenesis'

from Usuario import Usuario


from basetest import *


class MasterTeacher(Usuario, Base):
    __tablename__ = 'masterteacher'

    cedula = Column(String(40), ForeignKey('usuario.cedula'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity':'masterteacher',
    }


Base.metadata.create_all(engine)


