__author__ = 'braymrr'
from ORM.Curso import Curso
from Modelo.LogicaCursos import LogicaCursos

class Reporte:
    def cursos_mas_asistentes:
		#se mira fecha de inicio y fin de cohorte de cada curso
		#si el mes actual pertenece a este rango de fechas 
		#se cuenta el numero de estudiantes que asistieron a cada nota
		#
