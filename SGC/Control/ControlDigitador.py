__author__ = 'family'
#from Modelo import FabricaUsuarios
from ORM.Aspirante import Aspirante
from Modelo.LogicaAspirante import LogicaAspirante
from Modelo.LogicaCursos import LogicaCursos
from ORM.Preinscripcion import Preinscripcion
from Modelo.LogicaPreinscripcion import LogicaPreinscripcion

class ControlDigitador:
    def __init__(self):
        #self.fabrica=  FabricaUsuarios()
        self.LogicaAspirante = LogicaAspirante()
        self.LogicaCursos = LogicaCursos()
        self.LogicaPreinscripcion=LogicaPreinscripcion()

    def consultarCursos(self):
        cursos=self.LogicaCursos.consultarCursos()
        return cursos

    def consultarAspirante(self, id_asp):
        asp=self.LogicaAspirante.consultarAspirante(id_asp)
        return asp

    def consultarIdCurso(self, nombre):
        id_curso=self.LogicaCursos.consultarCurso(nombre)
        return id_curso

    def agregarLT(self, tipo, parametros):
        #return self.fabrica.getUsuario(tipo, parametros)
        return 0

    def agregarAspirante(self, params):
        aspirante = Aspirante(cedula=params[0], nombres=params[1], apellidos=params[2], direccion=params[3],
                              telefono=params[4], correo_electronico=params[5], fecha_nacimiento=params[6],
                              municipio=params[7],genero=params[8],institucion=params[9], escalafon=params[10],
                              sede=params[11],codigo_dane=params[12], dpto_secretaria=params[13], tutor=params[14],
                              usuario_col_aprende=params[15])
        self.LogicaAspirante.agregarAspirante(aspirante)

    def agregarPreinscripcion(self, params):
        preinscripcion=Preinscripcion(cedula_asp=params[0], id_curso=params[1], fecha=params[2] )
        self.LogicaPreinscripcion.agregarPreinscripcion(preinscripcion)




