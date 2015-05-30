from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ORM.Curso import *

from ORM.basetest import *


class LogicaCursos():
    Session = sessionmaker(bind=engine)
    session = Session()

    def __init__(self):
        # llamado para prueba del iterador
        print ("contructor Logica Cursos")

    def agregarCurso(self, curso):
        self.session.rollback()
        self.session.add(curso)
        self.session.commit()
        self.session.close()

    def consultarCursos(self):
        cursos = self.session.query(Curso).all()
        return cursos

    def consultarCurso(self, nombre_curso):
        curso = self.session.query(Curso).filter_by(nombre=nombre_curso).first()
        return curso

    def consultarCurso_id(self, id_curso):
        curso = self.session.query(Curso).filter_by(id=id_curso).first()
        return curso

    def modificarCurso(self, nombre_curso, curso_mod):
        self.session.rollback()
        curso = self.session.query(Curso).filter_by(nombre=nombre_curso).first()
        curso.descripcion = curso_mod.descripcion
        self.session.commit()
        self.session.close()

    def modificarCursoActividades(self, nombre_curso, curso_mod):
        self.session.rollback()
        curso = self.session.query(Curso).filter_by(nombre=nombre_curso).first()
        curso.descripcion = curso_mod.descripcion
        curso.actividades = curso_mod.actividades
        self.session.commit()
        self.session.close()

    def eliminarCurso(self, nombre_c):
        curso = self.session.query(Curso).filter_by(nombre=nombre_c).first()
        self.session.delete(curso)
        self.session.commit()
        self.cerrarSesion()

    def cerrarSesion(self):
        self.session.close()

'''

log = LogicaCursos()
curso = Curso(id = 122, nombre= 'micurso24', descripcion='descripcion')
log.agregarCurso(curso)
#cursos= log.consultarCurso('micurso24')
#print cursos.actividades


'''