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
        self.session.add(curso)
        self.session.commit()

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
        curso = self.session.query(Curso).filter_by(nombre=nombre_curso).first()
        curso.descripcion = curso_mod.descripcion
        self.session.commit()

    def modificarCursoActividades(self, nombre_curso, curso_mod):
        curso = self.session.query(Curso).filter_by(nombre=nombre_curso).first()
        curso.descripcion = curso_mod.descripcion
        curso.actividades = curso_mod.actividades
        curso.cohortes = curso_mod.cohortes
        self.session.commit()

    def eliminarCurso(self, id_curso_el):
        curso = self.session.query(Curso).filter_by(id=id_curso_el).first()
        self.session.delete(curso)
        self.session.commit()
        self.session.close()

    def cerrarSesion(self):
        self.session.close()

'''

log = LogicaCursos()
curso = Curso(id = 122, nombre= 'micurso24', descripcion='descripcion')
log.agregarCurso(curso)
#cursos= log.consultarCurso('micurso24')
#print cursos.actividades


'''