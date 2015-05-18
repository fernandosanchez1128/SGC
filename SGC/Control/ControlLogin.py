__author__ = 'JuanD'

from ORM.Usuario import Usuario
from Modelo.LogicaUsuario import LogicaUsuario


class ControlLogin:
    def __init__(self):
        # self.logCurso = LogicaCurso()
        self.logicaUsuario = LogicaUsuario()

    def buscarUsuarioUsername(self, username):
        return self.logicaUsuario.buscarUsuarioUsername(username)

    def modificarFechaAcceso(self, username, fecha):
        self.logicaUsuario.modificarUsuarioFechaAcceso(username, fecha)
