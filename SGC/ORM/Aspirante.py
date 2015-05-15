__author__ = 'cenesis'

from Usuario import Usuario


#engine = create_engine('postgresql://brayanrod:bryan1112@localhost:5432/sgc', echo=True)
#engine = create_engine('postgresql://braymrr:braymrr@pgsql/braymrr', echo=True)
#engine = create_engine('sqlite:///leaderteacher.db', echo=True)
#Base = declarative_base()


from basetest import *
class Aspirante(Base):
    __tablename__ = 'aspirante'
    cedula = Column(String(20), primary_key=True)
    nombres = Column(String(50))
    apellidos = Column(String(50))
    direccion = Column(String(40))
    telefono = Column(String(40))
    correo_electronico = Column(String(40), nullable=False)
    fecha_nacimiento = Column(Date)
    municipio = Column(String(40))
    genero = Column(String(10))
    institucion = Column(String(50))
    escalafon = Column(Integer)
    sede = Column(String(40))
    codigo_dane = Column(String(20))
    dpto_secretaria  = Column(String(20))
    tutor = Column(Boolean) #no estoy seguro del tipo
    usuario_col_aprende = Column(String(50))
    
Base.metadata.create_all(engine)
