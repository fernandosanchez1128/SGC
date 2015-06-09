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

from ORM.AreasDesempenadasm import AreasDesempenadasm
from ORM.Zonam import Zonam
from ORM.Modalidadm import Modalidadm
from ORM.GradosDesempenadosm import GradosDesempenadosm
from ORM.NivelesDesempenadosm import Nivelesm
from ORM.Etnoeducacionm import Etnoeducacionm


class FabricaUsuarios:

    def __init__(self):
        print ("En fabrica Usuarios")


    def getUsuario(self, tipo, params):
        #Usuario
        if(tipo==1 and len(params)==8):
            print ("creando usuario")
            objUs = Usuario(cedula =params[0],nombres =params[1],apellidos = params[2], direccion = params[3],telefono = params[4],correo_electronico = params[5], fecha_nacimiento = params[6], contrasena= params[7])
            return objUs
        #Master Teacher
        elif(tipo==2 and len(params)==8):
            print ("creando MT")
            objMT = MasterTeacher(cedula =params[0],nombres =params[1],apellidos = params[2], direccion = params[3],telefono = params[4],correoElectronico = params[5], fechaNacimiento = params[6], contrasena= params[7])
            return objMT

        #Leader Teacher
        elif(tipo==3 and len(params)==35):
            print ("creando LT en fabrica")
            #Trato especial para multivaluados-21a25
            obj_areas = []
            obj_zonas = []
            obj_modalidades = []
            obj_grados = []
            obj_etnos = []
            obj_niveles = []

            for area in params[28]:
                obj_area = AreasDesempenadas(area=area)
                obj_areas.append(obj_area)

            for zona in params[29]:
                obj_zona = Zona(zona=zona)
                obj_zonas.append(obj_zona)

            for modalidad in params[30]:
                obj_modalidad = Modalidad(modalidad=modalidad)
                obj_modalidades.append(obj_modalidad)

            for grado in params[31]:
                obj_grado = GradosDesempenados(grados=grado)
                obj_grados.append(obj_grado)

            for etno in params[32]:
                obj_etno = Etnoeducacion(etnoeducacion=etno)
                obj_etnos.append(obj_etno)

            for nivel in params[33]:
                obj_nivel = Niveles(niveles=nivel)
                obj_niveles.append(obj_nivel)


            objLT = LeaderTeacher(
                nombres =params[1],
                apellidos = params[2],
                direccion = params[3],
                telefono = params[4],
                correo_electronico = params[5],
                fecha_nacimiento = params[6],
                contrasena = params[7],
                type='leaderteacher',

                cedula =params[0],
                municipio =params[8],
                genero = params[9],
                institucion = params[10],
                escalafon= params[11],
                sede = params[12],
                codigo_dane= params[13],
			    dpto_secretaria= params [14],
                tutor = params[15],
                usuario_col_aprende = params[16],
                tipo_institucion = params[17],
                exp_preescolar = params [18],
                exp_primaria = params [19],
                exp_secundaria =params[20],
                exp_media = params[21],
                exp_superior = params[22],
                exp_rural = params[23],
                exp_urbano= params[24],
                exp_publico = params[25],
                exp_privado= params[26],
			    exp_total= params [27],
                #INICIO VALORES MULTIVALUADOS
                areas_desempenadas = obj_areas,
                zona =obj_zonas,
                modalidad = obj_modalidades,
                grados_desempenados = obj_grados,
                etnoeducacion = obj_etnos,
                niveles_desempenados = obj_niveles,
                #FIN VALORES MULTIVALUADOS
                grado = params [34])
            print("FIN CREACION LT")
            return objLT

        elif(tipo==4 and len(params)==35):
            print ("creando MT en fabrica")
            #Trato especial para multivaluados-21a25
            obj_areas = []
            obj_zonas = []
            obj_modalidades = []
            obj_grados = []
            obj_etnos = []
            obj_niveles = []

            for area in params[28]:
                obj_area = AreasDesempenadasm(area=area)
                obj_areas.append(obj_area)

            for zona in params[29]:
                obj_zona = Zonam(zona=zona)
                obj_zonas.append(obj_zona)

            for modalidad in params[30]:
                obj_modalidad = Modalidadm(modalidad=modalidad)
                obj_modalidades.append(obj_modalidad)

            for grado in params[31]:
                obj_grado = GradosDesempenadosm(grados=grado)
                obj_grados.append(obj_grado)

            for etno in params[32]:
                obj_etno = Etnoeducacionm(etnoeducacion=etno)
                obj_etnos.append(obj_etno)

            for nivel in params[33]:
                obj_nivel = Nivelesm(niveles=nivel)
                obj_niveles.append(obj_nivel)


            objMT = MasterTeacher(
                nombres =params[1],
                apellidos = params[2],
                direccion = params[3],
                telefono = params[4],
                correo_electronico = params[5],
                fecha_nacimiento = params[6],
                contrasena = params[7],
                type='masterteacher',

                cedula =params[0],
                municipio =params[8],
                genero = params[9],
                institucion = params[10],
                escalafon= params[11],
                sede = params[12],
                codigo_dane= params[13],
			    dpto_secretaria= params [14],
                tutor = params[15],
                usuario_col_aprende = params[16],
                tipo_institucion = params[17],
                exp_preescolar = params [18],
                exp_primaria = params [19],
                exp_secundaria =params[20],
                exp_media = params[21],
                exp_superior = params[22],
                exp_rural = params[23],
                exp_urbano= params[24],
                exp_publico = params[25],
                exp_privado= params[26],
			    exp_total= params [27],
                #INICIO VALORES MULTIVALUADOS
                areas_desempenadas = obj_areas,
                zona =obj_zonas,
                modalidad = obj_modalidades,
                grados_desempenados = obj_grados,
                etnoeducacion = obj_etnos,
                niveles_desempenados = obj_niveles,
                #FIN VALORES MULTIVALUADOS
                grado = params [34])
            print("FIN CREACION MT")
            return objMT


        else:
            print ("paso por none")
            return None
