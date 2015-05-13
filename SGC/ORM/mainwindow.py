from PyQt4 import uic
from PyQt4 import QtGui

from PyQt4.QtCore import *

from Control.FachadaMt import FachadaMt


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
        # cambiar por el codigo del profesor
        registros = self.fachadaMt.consulta_cursos_prof("1")
        for reg_mat in registros:
            curso = self.fachadaMt.consulta_curso(reg_mat.id_curso)
            item = QString(curso.nombre + "-" + str(reg_mat.id_cohorte))
            self.ui.lista_cursos.addItem(item)


    def cargarNotas(self):
        item_seleccionado = str(self.ui.lista_cursos.currentItem().text())
        # extraccion del codigo y del cohorte
        index = item_seleccionado.find('-')
        nombre_curso = item_seleccionado[:index]
        codigo_cohorte = item_seleccionado[index + 1:len(item_seleccionado)]


        # busqueda de las actividades
        curso = self.fachadaMt.consulta_curso_by_name(nombre_curso)
        # print "actividades",curso.actividades
        # print curso.actividades
        actividades = curso.actividades
        num_actividades = len(actividades)
        self.ui.tableWidget.setColumnCount(num_actividades)
        indice = 0
        for actividad in actividades:
            # en implementacion cambiar actividad por actividad.nombre
            item1 = QtGui.QTableWidgetItem(actividad.nombre)
            self.ui.tableWidget.setHorizontalHeaderItem(indice, item1)
            indice += 1
        self.fachadaMt.cerrar_session_curso()
        # consulta para estudiantes
        print curso.id, codigo_cohorte
        estudiantes = self.fachadaMt.estudiantes_curso(int(curso.id), int(codigo_cohorte))
        print "tamano", len(estudiantes)
        num_estudiantes = len(estudiantes)
        self.ui.tableWidget.setRowCount(num_estudiantes)
        indice = 0
        for estudiante in estudiantes:
            print estudiante.nombres
            item = QtGui.QTableWidgetItem(str(estudiante.cedula))
            self.ui.tableWidget.setVerticalHeaderItem(indice, item)
            indice += 1
        self.id_curso = int(curso.id)
        self.id_cohorte = int(codigo_cohorte)
        for  i in range (0,num_actividades,1) :
            for  a in range (0,num_estudiantes,1) :
                item = QtGui.QTableWidgetItem()
                cadena = str (i)+ "-" + str(a)
                item.setText(QString (cadena))
                self.ui.tableWidget.setItem(i,a,item)
        
            
            


