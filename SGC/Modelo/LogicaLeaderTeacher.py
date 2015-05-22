from sqlalchemy.orm import sessionmaker
from ORM.basetest import *
from ORM.LeaderTeacher import LeaderTeacher
from ORM.AreasDesempenadas import AreasDesempenadas
from ORM.Zona import Zona
from ORM.Modalidad import Modalidad
from ORM.GradosDesempenados import GradosDesempenados
from ORM.NivelesDesempenados import Niveles
from ORM.Etnoeducacion import Etnoeducacion

class LogicaLeaderTeacher():
    Session = sessionmaker(bind=engine)
    session = Session()

    def __init__(self):
        print ("En logica LeaderTeacher")


    def agregarLT(self, let):
        print("ENTRO EN AGREGAR LT")
        self.session.add(let)
        self.session.commit()
        self.session.close()


    def consultarLT(self, id_lt):
        lt=self.session.query(LeaderTeacher).filter_by(cedula=id_lt).first()
        return lt

    #Caso Multivaluados

    def consultarZona(self, cedula):
        zonas=self.session.query(Zona).filter_by(cedula_lt=cedula).all()
        self.session.close()
        return zonas

    def consultarAreasDesempenadas(self, cedula):
        areasdes=self.session.query(AreasDesempenadas).filter_by(cedula_lt=cedula).all()
        self.session.close()
        return areasdes

    def consultarModalidad(self, cedula):
        modalidad=self.session.query(Modalidad).filter_by(cedula_lt=cedula).all()
        self.session.close()
        return modalidad

    def consultarGrados(self, cedula):
        grados=self.session.query(GradosDesempenados).filter_by(cedula_lt=cedula).all()
        self.session.close()
        return grados

    def consultarNiveles(self, cedula):
        nivel=self.session.query(Niveles).filter_by(cedula_lt=cedula).all()
        self.session.close()
        return nivel

    def consultarEtnoeducacion(self, cedula):
        etno=self.session.query(Etnoeducacion).filter_by(cedula_lt=cedula).all()
        self.session.close()
        return etno
    ##-------------------------------------------------------------------------------
    #EDICION
    def editarLT(self, cedula, newlt):
        lt=self.session.query(LeaderTeacher).filter_by(cedula=cedula).first()

        lt.nombres=newlt.nombres
        lt.apellidos=newlt.apellidos
        lt.direccion =newlt.direccion
        lt.telefono = newlt.telefono
        lt.correo_electronico= newlt.correo_electronico
        lt.contrasena = newlt.contrasena
        lt.fecha_nacimiento=newlt.fecha_nacimiento

        lt.municipio = newlt.municipio
        lt.genero = newlt.genero
        lt.institucion = newlt.institucion
        lt.escalafon =  newlt.escalafon
        lt.sede = newlt.sede
        lt.codigo_dane = newlt.codigo_dane
        lt.dpto_secretaria  = newlt.dpto_secretaria
        lt.tutor =  newlt.tutor
        lt.usuario_col_aprende =  newlt.usuario_col_aprende

        #Academica o Tecnica
        lt.tipo_institucion = newlt.tipo_institucion
        #Relacionado a Experiencia
        lt.exp_preescolar = newlt.exp_preescolar
        lt.exp_primaria = newlt.exp_primaria
        lt.exp_secundaria= newlt.exp_secundaria
        lt.exp_media = newlt.exp_media
        lt.exp_superior = newlt.exp_superior
        lt.exp_rural = newlt.exp_rural
        lt.exp_urbano = newlt.exp_urbano
        lt.exp_publico = newlt.exp_publico
        lt.exp_privado = newlt.exp_privado
        lt.exp_total = newlt.exp_total
        lt.grado = newlt.grado
        self.session.commit()
        self.session.close()



    def cerrarSesion(self):
        self.session.close()

'''
log=LogicaLeaderTeacher()
log.consultarAreasDesempenadas('1144')
'''
