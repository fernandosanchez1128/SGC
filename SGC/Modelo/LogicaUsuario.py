from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from MasterTeacher import *
class LogicaUsuario ():
	#def __init__ (self) 
	Session = sessionmaker(bind=engine)
	session = Session()
	def __init__ (self) :
		#llamado para prueba del iterador 
		print ("contructor")
		
	def agregarUsuario (self, usuario)	:
		self.session.add(usuario)
		self.session.commit()
		self.session.close ()
		
	def buscarUsuario (self, cedula_usuario):	
		usuario = self.session.query(Usuario).filter_by (cedula = cedula_usuario).first()
		return usuario
		
	def modificarUsuario (self, cedula_user, usuario_mod): 
		usuario = self.session.query(Usuario).filter_by(cedula= cedula_user).first() 
		usuario.nombres= usuario_mod.nombres
		usuario.apellidos =  usuario_mod.apellidos
		usuario.telefono =  usuario_mod.telefono
		usuario.direccion =  usuario_mod.direccion
		usuario.correoElectronico =  usuario_mod.correoElectronico
		usuario.fechaNacimiento =  usuario_mod.fechaNacimiento
		self.session.commit() 
		self.session.close () 
	
	def eliminarUsuario (self, cedula_user):
		usuario = self.session.query(Usuario).filter_by(cedula= cedula_user).first() 
		self.session.delete (usuario)
		self.session.commit() 
		self.session.close () 
		 
	

	
	
