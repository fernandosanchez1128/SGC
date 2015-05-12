from PyQt4 import uic
from PyQt4 import  QtGui
from duplicity import log
from PyQt4.QtCore import *
from Modelo.Cursos import Cursos
from Modelo.LogicaCursos import LogicaCursos
from Modelo.LogicaDicta import LogicaDicta
from Modelo.LogicaActividades import LogicaActividades
from Modelo.LogicaMatricula import LogicaMatricula
from Modelo.LogicaUsuario import LogicaUsuario
from ORM.Curso import *
from Actividades import Actividades

(Ui_MainWindow, QMainWindow) = uic.loadUiType('mainwindow.ui')


class MainWindow(QMainWindow):
    """MainWindow inherits QMainWindow"""
	codigo_profesor = ""
	fachadaMt = FachadaMt()
	id_curso = 0
	id_cohorte = 0
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect(self.ui.boton, SIGNAL("clicked()"), self.empezar)
        self.connect(self.ui.lista_cursos, SIGNAL("itemDoubleClicked(QListWidgetItem*)"), self.cargarNotas)
        self.empezar()

    def __del__(self):
        self.ui = None

    def empezar(self):
		#cambiar por el codigo del profesor
        registros = self.fachadaMt.consulta_cursos_prof("1")
        for reg_mat in registros :
            curso = self.fachadaMt.consulta_curso(reg_mat.id_curso)
            item = QString(curso.nombre + "-" + str(reg_mat.id_cohorte))
            self.ui.lista_cursos.addItem(item)

    def cargarNotas(self):
        item_seleccionado = str(self.ui.lista_cursos.currentItem().text())
        # extraccion del codigo y del cohorte
        index = item_seleccionado.find('-')
        nombre_curso = item_seleccionado[:index]
        codigo_cohorte = item_seleccionado[index+1:len(item_seleccionado)]


        # busqueda de las actividades
        log_curso= LogicaCursos()
        curso = self.fachadaMt.consulta_curso_by_name(nombre_curso)
        # print "actividades",curso.actividades
        #print curso.actividades
        actividades = LogicaActividades().actividades_curso(curso.id)
        num_actividades = len(actividades)
        self.ui.tableWidget.setColumnCount(num_actividades)
        indice = 0
        for actividad in actividades:
            #en implementacion cambiar actividad por actividad.nombre
            item1 = QtGui.QTableWidgetItem(actividad.nombre)
            self.ui.tableWidget.setHorizontalHeaderItem(indice, item1)
            indice += 1

        # consulta para estudiantes
        print curso.id,codigo_cohorte
        estudiantes  = self.fachadaMt.estudiantes_curso(int(curso.id),int(codigo_cohorte))
        print "tamano",len(estudiantes)
        num_estudiantes = len(regs_matricula)
        self.ui.tableWidget.setRowCount(num_estudiantes)
        indice = 0
        for estudiante in estudiantesa:
            print estudiante.nombres
            item = QtGui.QTableWidgetItem(str(estudiante.cedula))
            self.ui.tableWidget.setVerticalHeaderItem(indice, item)
            indice+=1
        self.id_curso = int (curso.id)
        self.id_cohorte = int (curso.id_cohorte)    
        
            
            


