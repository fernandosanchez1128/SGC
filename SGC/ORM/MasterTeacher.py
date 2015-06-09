__author__ = 'nelson'

from Usuario import Usuario

from basetest import *


class MasterTeacher(Usuario, Base):
    __tablename__ = 'masterteacher'

    cedula = Column(String(40), ForeignKey('usuario.cedula'), primary_key=True)
    municipio = Column(String(40))
    genero = Column(String(10))
    institucion = Column(String(50))
    escalafon = Column(String(20))
    sede = Column(String(40))
    codigo_dane = Column(String(20))
    dpto_secretaria  = Column(String(20))
    tutor = Column(Boolean)
    usuario_col_aprende = Column(Boolean)
    tipo_institucion = Column(String(20))

    exp_preescolar = Column(Integer)
    exp_primaria = Column(Integer)
    exp_secundaria= Column(Integer)
    exp_media= Column(Integer)
    exp_superior= Column(Integer)
    exp_rural = Column(Integer)
    exp_urbano = Column(Integer)
    exp_publico= Column(Integer)
    exp_privado= Column(Integer)
    exp_total= Column(Integer)

    #multivaluados
    areas_desempenadas = relationship("AreasDesempenadasm", backref='masterteacher',cascade="all, delete, delete-orphan")
    zona = relationship("Zonam", backref='masterteacher',cascade="all, delete, delete-orphan")
    modalidad = relationship("Modalidadm", backref='masterteacher',cascade="all, delete, delete-orphan")
    grados_desempenados = relationship("GradosDesempenadosm", backref='masterteacher',cascade="all, delete, delete-orphan")
    etnoeducacion = relationship("Etnoeducacionm", backref='masterteacher',cascade="all, delete, delete-orphan")
    niveles_desempenados = relationship("Nivelesm", backref='masterteacher',cascade="all, delete, delete-orphan")

    grado = Column(String(50))
    __mapper_args__ = {
        'polymorphic_identity':'masterteacher',
        # 'polymorphic_on':type
    }

from AreasDesempenadasm import *
from Zonam import *
from Modalidadm import *
from GradosDesempenadosm import *
from Etnoeducacionm import *
from NivelesDesempenadosm import *
Base.metadata.create_all(engine)


# Session = sessionmaker(bind=engine)
# session = Session()
# user = MasterTeacher(cedula  = 2246, nombres = 'Da',correo_electronico='d@ah.com', contrasena= 'd')
#
# session.add(user)
# session.commit()
