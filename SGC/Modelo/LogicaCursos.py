from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ORM.Curso import *
from itertools import *
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
        index =0
        for act, act_mod in izip(curso.actividades, curso_mod.actividades):
            print act.nombre
            print act_mod.nombre
            if act.nombre== act_mod.nombre:
                act.ponderado=act_mod.ponderado
            else:
                act.nombre = act_mod.nombre
                act.ponderado=act_mod.ponderado
            index+=1
        print "empieza el for"
        for i in range (index,len(curso_mod.actividades)):
            print curso_mod.actividades[i].nombre
            curso.actividades.append(curso_mod.actividades[i])
        #curso.actividades.append(curso_mod.actividades[0])
        #curso.actividades = curso_mod.actividades
        self.session.commit()
        self.session.close()

    def eliminarCurso(self, nombre_c):
        self.session.rollback()
        curso = self.session.query(Curso).filter_by(nombre=nombre_c).first()
        self.session.delete(curso)
        self.session.commit()
        self.cerrarSesion()

    def cerrarSesion(self):
        self.session.close()


'''
log = LogicaCursos()
act1 = Actividades(id_curso = 28, nombre = 'act3', ponderado = 0.8)
act2 = Actividades(id_curso = 28, nombre = 'act4', ponderado = 0.2)
actividades = [act1, act2]
curso = Curso(nombre= 'curso_', descripcion='desc curso_', actividades=actividades)
log.modificarCursoActividades('curso_', curso)
#cursos= log.consultarCurso('micurso24')
#print cursos.actividades
'''
