__author__ = 'family'

from ORM.Usuario import Usuario
from ORM.MasterTeacher import MasterTeacher
from ORM.LeaderTeacher import LeaderTeacher
from ORM.AreasDesempenadas import AreasDesempenadas
from ORM.Zona import Zona
from ORM.Modalidad import Modalidad
from ORM.GradosDesempenados import GradosDesempenados
from ORM.NivelesDesempenados import Niveles
from ORM.Etnoeducacion import Etnoeducacion


class FabricaUsuarios:

    def __init__(self):
        print ("En fabrica Usuarios")


    def getUsuario(self, tipo, params):
        #Usuario
        if(tipo==1 and len(params)==7):
            print ("creando usuario")
            objUs = Usuario(cedula =params[0],nombres =params[1],apellidos = params[2], direccion = params[3],telefono = params[4],correo_electronico = params[5], fecha_nacimiento = params[6])
            return objUs
        #Master Teacher
        elif(tipo==2 and len(params)==7):
            print ("creando MT")
            objMT = MasterTeacher(cedula =params[0],nombres =params[1],apellidos = params[2], direccion = params[3],telefono = params[4],correoElectronico = params[5], fechaNacimiento = params[6])
            return objMT

        #Leader Teacher
        elif(tipo==3 and len(params)==28):
            print ("creando LT en fabrica")
            #Trato especial para multivaluados-21a25
            obj_areas = []
            obj_zonas = []
            obj_modalidades = []
            obj_grados = []
            obj_etnos = []
            obj_niveles = []

            for area in params[21]:
                obj_area = AreasDesempenadas(area=area)
                obj_areas.append(obj_area)

            for zona in params[22]:
                obj_zona = Zona(zona=zona)
                obj_zonas.append(obj_zona)

            for modalidad in params[23]:
                obj_modalidad = Modalidad(modalidad=modalidad)
                obj_modalidades.append(obj_modalidad)

            for grado in params[24]:
                obj_grado = GradosDesempenados(grados=grado)
                obj_grados.append(obj_grado)

            for etno in params[25]:
                obj_etno = Etnoeducacion(etnoeducacion=etno)
                obj_etnos.append(obj_etno)

            for nivel in params[26]:
                obj_nivel = Niveles(niveles=nivel)
                obj_niveles.append(obj_nivel)


            objLT = LeaderTeacher(
                cedula =params[0],
                municipio =params[1],
                genero = params[2],
                institucion = params[3],
                escalafon= params[4],
                sede = params[5],
                codigo_dane= params[6],
			    dpto_secretaria= params [7],
                tutor = params[8],
                usuario_col_aprende = params[9],
                tipo_institucion = params[10],
                exp_preescolar = params [11],
                exp_primaria = params [12],
                exp_secundaria =params[13],
                exp_media = params[14],
                exp_superior = params[15],
                exp_rural = params[16],
                exp_urbano= params[17],
                exp_publico = params[18],
                exp_privado= params[19],
			    exp_total= params [20],
                #INICIO VALORES MULTIVALUADOS
                areas_desempenadas = obj_areas,
                zona =obj_zonas,
                modalidad = obj_modalidades,
                grados_desempenados = obj_grados,
                etnoeducacion = obj_etnos,
                niveles_desempenados = obj_niveles,
                #FIN VALORES MULTIVALUADOS
                grado = params [27])
            print("FIN CREACION LT")
            return objLT

        else:
            print ("paso por none")
            return None
