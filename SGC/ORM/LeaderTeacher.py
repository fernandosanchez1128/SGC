__author__ = 'cenesis'

from Usuario import Usuario


#engine = create_engine('postgresql://brayanrod:bryan1112@localhost:5432/sgc', echo=True)
#engine = create_engine('postgresql://braymrr:braymrr@pgsql/braymrr', echo=True)
#engine = create_engine('sqlite:///leaderteacher.db', echo=True)
#Base = declarative_base()


from basetest import *
class LeaderTeacher(Usuario, Base):
    __tablename__ = 'leaderteacher'

    cedula = Column(String(20), ForeignKey('usuario.cedula'), primary_key=True)
    municipio = Column(String(40))
    genero = Column(String(10))
    sede = Column(String(40))
    codigo_institucion = Column(String(20))
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
    niveles_desempenados = relationship("NivelesDesempenados", backref='leaderteacher',cascade="all, delete, delete-orphan")
    
    grado = Column(Integer)
    departamentoSecretaria= Column (String (20))
    municipioSecretaria = Column(String(40))
    __mapper_args__ = {
        'polymorphic_identity':'leaderteacher',
    }


Base.metadata.create_all(engine)
    


