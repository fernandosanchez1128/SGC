__author__ = 'family'

from Usuario import Usuario
from MasterTeacher import MasterTeacher
from LeaderTeacher import LeaderTeacher

class FabricaUsuarios:
    def getUsuario(self, tipo, params):
        #Usuario
        if(tipo==1 and len(params)==7):
			print ("creando usuario")
			objUs = Usuario(cedula =params[0],nombres =params[1],apellidos = params[2], direccion = params[3],telefono = params[4],correoElectronico = params[5], fechaNacimiento = params[6])	
			return objUs
        #leaderTeacher
        elif(tipo==2 and len(params)==7):
			print ("creando MT")
			objMT = MasterTeacher(cedula =params[0],nombres =params[1],apellidos = params[2], direccion = params[3],telefono = params[4],correoElectronico = params[5], fechaNacimiento = params[6])
			return objMT
        #masterTeacher
        elif(tipo==3 and len(params)==13):
			print ("creando LT")
			objLT = LeaderTeacher(cedula =params[0],nombres =params[1],apellidos = params[2], direccion = params[3],telefono = params[4],correoElectronico = params[5], fechaNacimiento = params[6],
			sede = params [7],institucion = params[8],codigoInstitucion = params[9],grado = params[10], departamentoSecretaria = params [11],municipioSecretaria = params [12])
			return objLT
        else:
			print ("paso por none")
			return None

