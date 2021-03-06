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
        self.connect(self.ui.tableWidget, SIGNAL(("cellChanged(int,int)")), self.guardarNota)
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
        self.ui.tableWidget.setColumnCount(num_actividades*2)
        indice = 0
        for actividad in actividades:
            item1 = QtGui.QTableWidgetItem(actividad.nombre)
            self.ui.tableWidget.setHorizontalHeaderItem(indice, item1)
            item2 = QtGui.QTableWidgetItem("asistio")
            indice += 1
            self.ui.tableWidget.setHorizontalHeaderItem(indice, item2)
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

        for i in range(0, num_estudiantes, 1):
            cod_estudiante =str(self.ui.tableWidget.verticalHeaderItem (i).text())
            #print cod_estudiante
            nota =0
            for a in range (0,(num_actividades*2),1):
                item = QtGui.QTableWidgetItem()
                if (a % 2 == 0):
                    nombre_actividad =str (self.ui.tableWidget.horizontalHeaderItem(a).text())
                    actividad =self.fachadaMt.consultar_actividad(nombre_actividad,self.id_curso)
                    # print self.id_curso, actividad.id_actividad, cod_estudiante, self.id_cohorte
                    nota = self.fachadaMt.consultar_nota(self.id_curso,actividad.id_actividad,cod_estudiante,self.id_cohorte)
                    print "nota", nota
                    if (nota != None):
                        item.setText(QString(str(nota.nota)))
                        if (nota.nota== 0):
                            item.setFlags(Qt.ItemIsUserCheckable)

                else :
                    if (nota != None):
                        if (nota.nota == 0):
                            item.setCheckState(False)
                        else :
                            item.setCheckState(True)
                    else:
                        item.setCheckState(True)


                self.ui.tableWidget.setItem(i,a,item)


    def guardarNota(self, fila,columna):
        sender = self.sender()
        nombre_actividad = ""
        cedula = ""
        id_actividad = 0
        item = sender.item(fila, columna)
        validacion = False
        nota = 0
        if (item != None ):
            if (columna %2 == 0 and item.text() != ""):
                nombre_actividad = str(self.ui.tableWidget.horizontalHeaderItem(columna).text())
                cedula = str(self.ui.tableWidget.verticalHeaderItem(fila).text())
                actividad = self.fachadaMt.consultar_actividad(nombre_actividad, self.id_curso)
                id_actividad = actividad.id_actividad
                #print item
                nota_str = str(item.text())
                try:
                    nota = float(nota_str)
                    validacion = True
                except ValueError:
                    validacion = False
                    msj = "ingrese un numero"+str(columna)
                    QtGui.QMessageBox.warning(self, 'Error',msj , QtGui.QMessageBox.Ok)
                if (validacion):

                    if (nota >= 0.0 and nota <= 5.0):
                        print id_actividad, cedula
                        self.fachadaMt.guardar_nota(id_actividad, self.id_curso, self.id_cohorte, cedula, nota,True)
                    else:
                        QtGui.QMessageBox.warning(self, 'Error', "ingrese un numero entre 0.0 y 5.0", QtGui.QMessageBox.Ok)
            elif (columna % 2 != 0):
                estado = item.checkState()
                nombre_actividad = str(self.ui.tableWidget.horizontalHeaderItem(columna - 1).text())
                cedula = str(self.ui.tableWidget.verticalHeaderItem(fila).text())
                actividad = self.fachadaMt.consultar_actividad(nombre_actividad, self.id_curso)
                id_actividad = actividad.id_actividad
                item_ant = sender.item(fila, columna - 1)
                # itemant.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsEnabled)
                if (estado == 0):
                    item_ant.setFlags(Qt.ItemIsUserCheckable)
                    item_ant.setText ("0.0")
                    self.fachadaMt.guardar_nota(id_actividad, self.id_curso, self.id_cohorte, cedula, 0, False)
                elif (estado == 2):
                    item_ant.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsEnabled|Qt.ItemIsEditable)


