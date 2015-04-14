__author__ = 'family'

from Usuario import Usuario
from MasterTeacher import MasterTeacher
from LeaderTeacher import LeaderTeacher

class FabricaUsuarios:
    def getUsuario(self, tipo, params):
        if(tipo==1 & len(params)==7):
            objUs = Usuario(params[0],params[1],params[2],params[3],params[4],params[5],params[6])
            return objUs
        elif(tipo==2 & len(params)==7):
            objMT = MasterTeacher(params[0],params[1],params[2],params[3],params[4],params[5],params[6])
            return objMT
        elif(tipo==3 & len(params)==15):
            objLT = LeaderTeacher(params[0],params[1],params[2],params[3],params[4],params[5],params[6],params[7],params[8],params[9],params[10],params[11],params[12],params[13])
            return objLT
        else:
            return None

