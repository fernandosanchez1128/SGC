__author__ = 'cenesis'

from Usuario import Usuario


from basetest import *
class LeaderTeacher(Usuario, Base):
    __tablename__ = 'leaderteacher'

    cedula = Column(String(20), ForeignKey('usuario.cedula'), primary_key=True)
    municipio = Column(String(40))
    genero = Column(String(10))
    institucion = Column(String(50))
    escalafon = Column(Integer)
    sede = Column(String(40))
    codigo_dane = Column(String(20))
    dpto_secretaria  = Column(String(20))
    tutor = Column(Boolean) #no estoy seguro del tipo
    usuario_col_aprende = Column(String(50))
    dpto_secretaria  = Column(String(20))
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
    areas_desempenadas = relationship("AreasDesempenadas", backref='leaderteacher',cascade="all, delete, delete-orphan")
    zona = relationship("Zona", backref='leaderteacher',cascade="all, delete, delete-orphan")
    modalidad = relationship("Modalidad", backref='leaderteacher',cascade="all, delete, delete-orphan")
    grados_desempenados = relationship("GradosDesempenados", backref='leaderteacher',cascade="all, delete, delete-orphan")
    etnoeducacion = relationship("Etnoeducacion", backref='leaderteacher',cascade="all, delete, delete-orphan")
    niveles_desempenados = relationship("Niveles", backref='leaderteacher',cascade="all, delete, delete-orphan")
    
    grado = Column(Integer)
    departamento_secretaria= Column (String (20))
    municipio_secretaria = Column(String(40))
    __mapper_args__ = {
        'polymorphic_identity':'leaderteacher',
    }

from AreasDesempenadas import *
from Zona import *
from Modalidad import *
from GradosDesempenados import *
from Etnoeducacion import *
from NivelesDesempenados import *


Base.metadata.create_all(engine)
    



# Session = sessionmaker(bind=engine)
# session = Session()
# user = LeaderTeacher(cedula  = 1421, correo_electronico='c@ah.com', contrasena= 'c')
#
# session.add(user)
# session.commit()