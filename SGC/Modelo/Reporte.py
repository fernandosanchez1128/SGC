__author__ = 'braymrr'
from ORM.Curso import Curso
from Modelo.LogicaCursos import LogicaCursos

class Reporte:
    def cursos_mas_asistentes:
        #filtro fecha de inicio y fin de cohorte de cada curso pertenece la fecha actual
        #agrupo por id_curso
		#se cuenta en numero de matriculados de cada curso
        #ordena de menor a mayor y se traen los 10 primeros

