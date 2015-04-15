__author__ = 'family'
from Modelo import FabricaUsuarios

class ControlDigitador:
    def __init__(self):
        self.fabrica=  FabricaUsuarios()

    def crearUsuario(self, tipo, parametros):
        return self.fabrica.getUsuario(tipo, parametros)