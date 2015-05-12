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
from Actividades import Actividades

(Ui_MainWindow, QMainWindow) = uic.loadUiType('mainwindow.ui')


class MainWindow(QMainWindow):
    """MainWindow inherits QMainWindow"""

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
        registros = LogicaDicta().consultarCursosProf("1")
        for reg_mat in registros :
            curso = LogicaCursos().consultarCurso(reg_mat.id_curso)
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
        curso = log_curso.consulta_by_name(nombre_curso)
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
        regs_matricula = LogicaMatricula().consultar_estudiantes(int(curso.id),int(codigo_cohorte))
        print "tamano",len(regs_matricula)
        num_estudiantes = len(regs_matricula)
        self.ui.tableWidget.setRowCount(num_estudiantes)
        indice = 0
        for reg_matricula in regs_matricula:
            estudiante = LogicaUsuario().buscarUsuario(reg_matricula.cedula_lt)
            print estudiante.nombres
            item = QtGui.QTableWidgetItem(str(estudiante.cedula))
            self.ui.tableWidget.setVerticalHeaderItem(indice, item)
            indice+=1


