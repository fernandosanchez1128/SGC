from Observable import *


class Notas(object, Observable):
    __id_curso = ""
    __id_actividad = ""
    __id_lt = ""
    __nota = 5
    lista_observadores = ()

    def __init__(self, curso, actividad, lt, nota):
        self.id_curso = id_curso
        self.id_actividad = id_actividad
        self.id_lt = id_lt
        self.nota = nota

    def notifyObservers:
        for observador in lista_observadores:
            obsevador.update

    def add(self, observador):
        # Add to the list of Observers
        lista_observadores.append(observador)


    def remove(self, observador):
        print "remove observer"


    def agregar(self, obj_nota)
    # agregar nota de la actividad
        notifyObservers(self)


    def getNnota(self):
        return self.nota
		
		
		
