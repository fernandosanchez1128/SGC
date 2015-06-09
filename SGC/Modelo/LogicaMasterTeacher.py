from sqlalchemy.orm import sessionmaker
from ORM.basetest import *
from ORM.MasterTeacher import MasterTeacher
from ORM.AreasDesempenadasm import AreasDesempenadasm
from ORM.Zonam import Zonam
from ORM.Modalidadm import Modalidadm
from ORM.GradosDesempenadosm import GradosDesempenadosm
from ORM.NivelesDesempenadosm import Nivelesm
from ORM.Etnoeducacionm import Etnoeducacionm

from sqlalchemy import exc as sqlalchemy_exceptions
from exceptions import *
from sqlalchemy.exc import *


class LogicaMasterTeacher():
    Session = sessionmaker(bind=engine)
    session = Session()

    def __init__(self):
        print ("En logica LeaderTeacher")


    def agregarMT(self, let):
        try:
            self.session.add(let)
            self.session.commit()
            self.session.close()
            return "Exito"
        except sqlalchemy_exceptions.IntegrityError:
            self.session.close()
            return str("Violacion de integridad en la BD: Cedula ya existe en la Base de datos")
        except sqlalchemy_exceptions.DisconnectionError:
            self.session.close()
            return str("Error de desconexion de base de datos")
        except sqlalchemy_exceptions.InternalError:
            self.session.close()
            return str("Internal Error: Consulte con el adminstrador")
        except sqlalchemy_exceptions.SQLAlchemyError:
            self.session.close()
            return str("Error interno en la Base de datos. Consulte con el administrador")

    def consultarMT(self, id_mt):
        mt=self.session.query(MasterTeacher).filter_by(cedula=id_mt).first()
        return mt

    ##-------------------------------------------------------------------------------
    #EDICION
    def editarMT(self, cedula, newlt):
        try:
            lt=self.session.query(MasterTeacher).filter_by(cedula=cedula).first()
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

            obj_areas = []
            obj_zonas = []
            obj_modalidades = []
            obj_grados = []
            obj_etnos = []
            obj_niveles = []
            i=0
            for zona in newlt.zona:
                obj_zona = Zonam(zona=newlt.zona[i].zona)
                obj_zonas.append(obj_zona)
                i+=1

            lt.zona=obj_zonas
            i=0

            for area in newlt.areas_desempenadas:
                obj_area = AreasDesempenadasm(area=newlt.areas_desempenadas[i].area)
                obj_areas.append(obj_area)
                i+=1

            lt.areas_desempenadas=obj_areas
            i=0

            for modalidad in newlt.modalidad:
                obj_modalidad = Modalidadm(modalidad=newlt.modalidad[i].modalidad)
                obj_modalidades.append(obj_modalidad)
                i+=1

            lt.modalidad=obj_modalidades
            i=0

            for grado in newlt.grados_desempenados:
                obj_grado = GradosDesempenadosm(grados=newlt.grados_desempenados[i].grados)
                obj_grados.append(obj_grado)
                i+=1

            lt.grados_desempenados=obj_grados
            i=0

            for etno in newlt.etnoeducacion:
                obj_etno = Etnoeducacionm(etnoeducacion=newlt.etnoeducacion[i].etnoeducacion)
                obj_etnos.append(obj_etno)
                i+=1

            lt.etnoeducacion=obj_etnos
            i=0

            for nivel in newlt.niveles_desempenados:
                obj_nivel = Nivelesm(niveles=newlt.niveles_desempenados[i].niveles)
                obj_niveles.append(obj_nivel)
                i+=1

            lt.niveles_desempenados=obj_niveles
            i=0

            self.session.commit()
            return "Exito"
        except sqlalchemy_exceptions.IntegrityError:
            #self.session.close()
            return str("Violacion de integridad en la BD: ")
        except sqlalchemy_exceptions.AmbiguousForeignKeysError:
            #self.session.close()
            return str("Error en llave foranea, Cedula no existe o error en multivaluados")
        except sqlalchemy_exceptions.DisconnectionError:
            #self.session.close()
            return str("Error de desconexion de base de datos")
        except sqlalchemy_exceptions.InternalError:
            #self.session.close()
            return str("Internal Error: Consulte con el adminstrador")
        except sqlalchemy_exceptions.SQLAlchemyError:
            #self.session.close()
            return str("Error interno en la Base de datos. Consulte con el administrador")

    def eliminarMT(self,cedula):
        try:
            lt=self.session.query(MasterTeacher).filter_by(cedula=cedula).first()
            self.session.delete(lt)
            self.session.commit()
            self.session.close()
        except sqlalchemy_exceptions:
            self.session.close()

    def cerrarSesion(self):
        self.session.close()