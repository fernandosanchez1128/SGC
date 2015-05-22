__author__ = 'nelson'
from Modelo.FabricaUsuarios import FabricaUsuarios
from ORM.Aspirante import Aspirante
from Modelo.LogicaAspirante import LogicaAspirante
from Modelo.LogicaCursos import LogicaCursos
from ORM.Preinscripcion import Preinscripcion
from Modelo.LogicaPreinscripcion import LogicaPreinscripcion
from Modelo.LogicaLeaderTeacher import LogicaLeaderTeacher
from Modelo.LogicaUsuario import LogicaUsuario


class ControlDigitador:
    def __init__(self):
        self.LogicaAspirante = LogicaAspirante()
        self.LogicaCursos = LogicaCursos()
        self.LogicaPreinscripcion=LogicaPreinscripcion()
        self.Fabrica=FabricaUsuarios()
        self.LogicaLT=LogicaLeaderTeacher()
        self.LogicaUsuarios=LogicaUsuario()

    def consultarCursos(self):
        cursos=self.LogicaCursos.consultarCursos()
        return cursos

    def consultarAspirante(self, id_asp):
        asp=self.LogicaAspirante.consultarAspirante(id_asp)
        return asp

    def consultarIdCurso(self, nombre):
        id_curso=self.LogicaCursos.consultarCurso(nombre)
        return id_curso

    def agregarLT(self, tipo, params):
        leaderTeacher=self.Fabrica.getUsuario(tipo,params)
        print("paso por fabrica")
        self.LogicaLT.agregarLT(leaderTeacher)
        print("paso por logica")


    def consultarLT(self,cedula):
        lt=self.LogicaLT.consultarLT(cedula)
        return lt

    def consultarUsuario(self, cedula):
        user=self.LogicaUsuarios.buscarUsuario(cedula)
        return user

    #CASO MULTIVALUADOS:
    def consultarZonas(self, cedula):
        zonas=self.LogicaLT.consultarZona(cedula)
        return zonas

    def consultarAreasDesempenadas(self, cedula):
        areasdes=self.LogicaLT.consultarAreasDesempenadas(cedula)
        return areasdes


    def consultarModalidad(self, cedula):
        modalidad=self.LogicaLT.consultarModalidad(cedula)
        return modalidad

    def consultarGrados(self, cedula):
        grados=self.LogicaLT.consultarGrados(cedula)
        return grados

    def consultarNiveles(self, cedula):
        nivel=self.LogicaLT.consultarNiveles(cedula)
        return nivel

    def consultarEtnoeducacion(self, cedula):
        etno=self.LogicaLT.consultarEtnoeducacion(cedula)
        return etno




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


    #EDICION:
    def editarUsuarioLT(self, ced, params):
        user= self.Fabrica.getUsuario(1,params)
        self.LogicaUsuarios.modificarUsuario(ced,user)

    def editarLT(self, ced, params):
        lt=self.Fabrica.getUsuario(3,params)
        self.LogicaLT.editarLT(ced,lt)

    def cerrarSesion(self):
        self.LogicaUsuarios.cerrarSesion()
        self.LogicaLT.cerrarSesion()