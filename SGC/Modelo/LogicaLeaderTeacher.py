from sqlalchemy.orm import sessionmaker
from ORM.basetest import *
from ORM.LeaderTeacher import LeaderTeacher
from ORM.AreasDesempenadas import AreasDesempenadas
from ORM.Zona import Zona
from ORM.Modalidad import Modalidad
from ORM.GradosDesempenados import GradosDesempenados
from ORM.NivelesDesempenados import Niveles
from ORM.Etnoeducacion import Etnoeducacion

from sqlalchemy import exc as sqlalchemy_exceptions


class LogicaLeaderTeacher():
    Session = sessionmaker(bind=engine)
    session = Session()

    def __init__(self):
        print ("En logica LeaderTeacher")


    def agregarLT(self, let):
        try:
            self.session.add(let)
            self.session.commit()
            self.session.close()
            return "Exito"
        except Exception:
            self.session.close()
            return "Fracaso"

    def consultarLT(self, id_lt):
        lt=self.session.query(LeaderTeacher).filter_by(cedula=id_lt).first()
        return lt

    ##-------------------------------------------------------------------------------
    #EDICION
    def editarLT(self, cedula, newlt):
        try:
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

            obj_areas = []
            obj_zonas = []
            obj_modalidades = []
            obj_grados = []
            obj_etnos = []
            obj_niveles = []
            i=0
            for zona in newlt.zona:
                obj_zona = Zona(zona=newlt.zona[i].zona)
                obj_zonas.append(obj_zona)
                i+=1

            lt.zona=obj_zonas
            i=0

            for area in newlt.areas_desempenadas:
                obj_area = AreasDesempenadas(area=newlt.areas_desempenadas[i].area)
                obj_areas.append(obj_area)
                i+=1

            lt.areas_desempenadas=obj_areas
            i=0

            for modalidad in newlt.modalidad:
                obj_modalidad = Modalidad(modalidad=newlt.modalidad[i].modalidad)
                obj_modalidades.append(obj_modalidad)
                i+=1

            lt.modalidad=obj_modalidades
            i=0

            for grado in newlt.grados_desempenados:
                obj_grado = GradosDesempenados(grados=newlt.grados_desempenados[i].grados)
                obj_grados.append(obj_grado)
                i+=1

            lt.grados_desempenados=obj_grados
            i=0

            for etno in newlt.etnoeducacion:
                obj_etno = Etnoeducacion(etnoeducacion=newlt.etnoeducacion[i].etnoeducacion)
                obj_etnos.append(obj_etno)
                i+=1

            lt.etnoeducacion=obj_etnos
            i=0

            for nivel in newlt.niveles_desempenados:
                obj_nivel = Niveles(niveles=newlt.niveles_desempenados[i].niveles)
                obj_niveles.append(obj_nivel)
                i+=1

            lt.niveles_desempenados=obj_niveles
            i=0

            self.session.commit()
            return "Exito"
        except Exception:
            self.session.close()
            return "Fracaso"

    def eliminarLT(self,cedula):
        try:
            lt=self.session.query(LeaderTeacher).filter_by(cedula=cedula).first()
            self.session.delete(lt)
            self.session.commit()
            self.session.close()
        except sqlalchemy_exceptions:
            self.session.close()


    def cerrarSesion(self):
        self.session.close()

'''
log=LogicaLeaderTeacher()
log.eliminarLT('1144')
'''
