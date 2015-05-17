__author__ = 'family'
#from Modelo import FabricaUsuarios
from ORM.Aspirante import Aspirante
from Modelo.LogicaAspirante import LogicaAspirante
from Modelo.LogicaCursos import LogicaCursos


class ControlDigitador:
    def __init__(self):
        #self.fabrica=  FabricaUsuarios()
        self.LogicaAspirante = LogicaAspirante()
        self.LogicaCursos = LogicaCursos()

    def consultarCursos(self):
        cursos=self.LogicaCursos.consultarCursos()
        return cursos

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
                              usuario_col_aprende=params[15], id_curso=params[16])
        self.LogicaAspirante.agregarAspirante(aspirante)

