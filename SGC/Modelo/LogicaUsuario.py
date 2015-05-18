from sqlalchemy.orm import sessionmaker

from ORM.MasterTeacher import *


class LogicaUsuario():
    # def __init__ (self)
    Session = sessionmaker(bind=engine)
    session = Session()

    def __init__(self):
        #llamado para prueba del iterador
        print ("contructor Logica Usuarios")

    def agregarUsuario(self, usuario):
        print("ENTRO EN AGREGAR USUARIO")
        self.session.add(usuario)
        self.session.commit()
        self.session.close()

    def buscarUsuario(self, cedula_usuario):
        usuario = self.session.query(Usuario).filter_by(cedula=cedula_usuario).first()
        self.session.close()
        return usuario

    def buscarUsuarioUsername(self, username):
        usuario = self.session.query(Usuario).filter_by(correo_electronico=username).first()
        self.session.close()
        return usuario


    def modificarUsuario(self, cedula_user, usuario_mod):
        usuario = self.session.query(Usuario).filter_by(cedula=cedula_user).first()
        usuario.nombres = usuario_mod.nombres
        usuario.apellidos = usuario_mod.apellidos
        usuario.telefono = usuario_mod.telefono
        usuario.direccion = usuario_mod.direccion
        usuario.correo_electronico = usuario_mod.correo_electronico
        usuario.fecha_nacimiento = usuario_mod.fecha_nacimiento
        self.session.commit()
        self.session.close()

    def eliminarUsuario(self, cedula_user):
        usuario = self.session.query(Usuario).filter_by(cedula=cedula_user).first()
        self.session.delete(usuario)
        self.session.commit()
        self.session.close()


    def cerrarSesion(self):
        self.session.close()
