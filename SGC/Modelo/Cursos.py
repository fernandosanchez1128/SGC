from IteratorCurso import *
from CursoColeccion import *


class Cursos(CursoColeccion):
    _atributo = 0

    def __init__(self, cursos):
        print "constructor"
        self.cursos = cursos


    def iterator(self):
        print "retornando iterador"
        return IteratorCursos(self.cursos)


class IteratorCursos(IteratorCurso):
    def __init__(self, cursos):
        self.actual = -1
        self.cursos = cursos

    def next(self):
        if self.actual < len(self.cursos):
            self.actual += 1
            return self.cursos[self.actual]

    def hasNext(self):
        if self.actual + 1 < len(self.cursos):
            return True
        else:
            return False;

    def current(self):
        return self.cursos[self.actual]
					
	
		
