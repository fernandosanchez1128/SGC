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

'''
Session = sessionmaker(bind=engine)
session = Session()
user = MasterTeacher(cedula  = 2246, nombres = 'Da',correo_electronico='d@ah.com', contrasena= 'd')

session.add(user)
session.commit()
'''