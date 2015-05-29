from PyQt4 import uic
from PyQt4 import QtGui
from datetime import datetime,date
from PyQt4.QtCore import *
import calendar
from PyQt4.QtGui import QFileDialog
from Control.FachadaLt import FachadaLt
from VistaDescargarCertificado import VistaDescargarCertificado
from Singleton import Singleton
import time
(Ui_MainWindow, QMainWindow) = uic.loadUiType('VistaLt.ui')

@Singleton
class VistaLt(QMainWindow):
    codigo_profesor = ""
    """MainWindow inherits QMainWindow"""
    fachadaLt = FachadaLt()
    id_curso = 0
    id_cohorte = 0
    name = ""
    nombre_curso=""
    cedula = ""
    usuario =""

    def __init__(self,usuario, parent=None):
        QMainWindow.__init__(self, parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect(self.ui.certificado, SIGNAL("clicked()"), self.vista_certificado)
        self.connect(self.ui.lista_cursos, SIGNAL("itemDoubleClicked(QListWidgetItem*)"), self.cargarNotas)
        self.usuario = usuario
        self.name = usuario.nombres
        self.cedula=usuario.cedula
        print "cedula_user", usuario.cedula
        self.cargar_cursos()



    def __del__(self):
        self.ui = None


    def cargar_cursos(self):
        # cambiar por el codigo del estudiante
        print self.cedula
        registros = self.fachadaLt.consulta_cursos_estudiante(self.cedula)
        id_curso_ant = 0
        num_curso =0
        for registro in registros:
            curso = self.fachadaLt.consulta_curso(registro.id_curso)
            item = QtGui.QListWidgetItem()
            item.setWhatsThis(QString (str (registro.id_cohorte)))
            if (curso.id == id_curso_ant):
                num_curso +=1
                item.setText(QString(curso.nombre + QString("-") +QString(str(num_curso))))
            else:
                num_curso =0
                item.setText(QString(curso.nombre))
            id_curso_ant = curso.id
            font = QtGui.QFont()
            font.setBold(True)
            font.setWeight(75)
            item.setFont (font)
            self.ui.lista_cursos.addItem(item)


    def cargarNotas(self):
        item_seleccionado = self.ui.lista_cursos.currentItem()
        fecha_actual = date.today()
        # extraccion del codigo y del cohorte
        nombre_curso_com = str(item_seleccionado.text())
        codigo_cohorte = str (item_seleccionado.whatsThis())
        index = nombre_curso_com.find('-')
        nombre_curso = ""
        if (index != -1):
            nombre_curso = nombre_curso_com[:index]
        else :
            nombre_curso = nombre_curso_com
        # busqueda de las actividades
        curso = self.fachadaLt.consulta_curso_by_name(nombre_curso)
        cohorte = self.fachadaLt.consultar_cohorte(curso.id,codigo_cohorte)
        print "fecha", fecha_actual
        print "fecha2", cohorte.fecha_fin
        if fecha_actual >  cohorte.fecha_fin:
            self.ui.certificado.setEnabled (True)
        else :
            self.ui.certificado.setEnabled (False)

        print "fecha cohorte" , cohorte.fecha_fin
        actividades = curso.actividades
        num_actividades = len(actividades)
        self.ui.tableWidget.setColumnCount(num_actividades)
        indice = 0
        fuente = QtGui.QFont()
        fuente.setBold(True)
        fuente.setWeight(75)
        for actividad in actividades:
            item1 = QtGui.QTableWidgetItem(actividad.nombre)
            item1.setFont(fuente)
            self.ui.tableWidget.setHorizontalHeaderItem(indice, item1)
            indice += 1
        self.fachadaLt.cerrar_session_curso()
        # consulta para estudiantes
        self.ui.tableWidget.setRowCount(1)
        indice = 0
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item = QtGui.QTableWidgetItem(str(self.name))
        item.setFont(font)
        self.ui.tableWidget.setVerticalHeaderItem(indice, item)
        self.id_curso = int(curso.id)
        self.id_cohorte = int(codigo_cohorte)
        self.nombre_curso=nombre_curso_com

        for num_act in range(0, (num_actividades), 1):
            item = QtGui.QTableWidgetItem()
            item.setFlags(Qt.ItemIsUserCheckable)
            nombre_actividad = str(self.ui.tableWidget.horizontalHeaderItem(num_act).text())
            actividad = self.fachadaLt.consultar_actividad(nombre_actividad, self.id_curso)
            nota = self.fachadaLt.consultar_nota(self.id_curso, actividad.id_actividad, self.cedula,self.id_cohorte)
            print self.id_curso,actividad.id_actividad,self.cedula,self.id_cohorte
            if (nota != None):
                item.setText(QString(str(nota.nota)))
            self.ui.tableWidget.setItem(0, num_act, item)




    def vista_certificado (self):
        ruta = QFileDialog.getSaveFileName(self, 'Guardar Certficado', '', selectedFilter='*.pdf')
        if ruta:
            print ruta
            persona=self.fachadaLt.buscarPersona(self.cedula)
            nombre=persona.nombres
            apellido=persona.apellidos
            nombreCompleto=str(nombre)+" "+str(apellido)
            nota=self.fachadaLt.registro_matricula(self.cedula,self.id_cohorte,self.id_curso).nota_definitiva
            nomCurso=self.nombre_curso
            if (nota != None):
                nota=float(nota)
                self.fachadaLt.descargaCertificado(ruta, nombreCompleto, self.cedula, nota, nomCurso)
            else :
                QtGui.QMessageBox.warning(self, 'Error', "La nota no ha sido subida al sistema \n "
                                                         "por favor espere o comuniquese con el coordinador", QtGui.QMessageBox.Ok)
        else:
            print "No se proporciono nombre de archivo"


