from PyQt4 import uic
from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui
from datetime import datetime,date
from Control.ControlCoordinador import ControlCoordinador
( Ui_Asignacion, QDialog ) = uic.loadUiType( 'Asignacion_fechas_cohortes.ui' )

class AsignacionCohortes ( QDialog ):
    """Asignacion inherits QMainWindow"""
    id_curso = 0
    fachadaCordinador = ControlCoordinador()
    list_actividades = []
    ultimo_mod =0
    year =0
    semestre =1
    mes =0
    fecha_actual=0
    fecha_limit =0
    def __init__ ( self,parent = None):
        QDialog.__init__( self, parent )
        self.ui = Ui_Asignacion()
        self.ui.setupUi( self )
        self.cargar_cursos()
        self.connect(self.ui.guardar, SIGNAL("clicked()"), self.guardar)
        self.connect(self.ui.listWidget, SIGNAL("itemDoubleClicked(QListWidgetItem*)"), self.cargar_grid)


    def __del__ ( self ):
        self.ui = None

    def cargar_cursos (self):
        fecha_actual = date.today()
        self.fecha_actual = fecha_actual
        self.year = fecha_actual.year
        mes =fecha_actual.month

        print "mes" ,mes
        if (mes <=6):
            self.mes =6
            self.semestre=1
        else:
            self.mes =11
            self.semestre=2
        cursos = self.fachadaCordinador.consultar_cursos()
        print len(cursos)
        for curso in cursos :
            item = QtGui.QListWidgetItem()
            item.setText(QString (curso.nombre))
            item.setWhatsThis(str (curso.id))
            self.ui.listWidget.addItem(item)
        self.fachadaCordinador.cerrarSesion()


    def cargar_grid(self):

        fecha_limit = date(self.year,self.mes,30)
        self.fecha_limit = fecha_limit
        item_seleccionado = self.ui.listWidget.currentItem()
        curso = self.fachadaCordinador.buscarCurso(str (item_seleccionado.text()))
        self.id_curso = curso.id
        cohortes = curso.cohortes
        self.fachadaCordinador.cerrarSesion()
        #borrado de los datos anteriores
        for i in range (1,self.ultimo_mod,1):
            print "paso"
            item = self.ui.grid.itemAtPosition(i,0)
            wid = item.widget()
            wid.deleteLater()
            item1= self.ui.grid.itemAtPosition(i,1)
            wid1 = item1.widget()
            wid1.deleteLater()
            item2 = self.ui.grid.itemAtPosition(i,2)
            wid2 = item2.widget()
            wid2.deleteLater()
            item3 = self.ui.grid.itemAtPosition(i,3)
            wid3 = item3.widget()
            wid3.deleteLater()
            item4 = self.ui.grid.itemAtPosition(i,4)
            wid4= item4.widget()
            wid4.deleteLater()
        #agregando los nuevos datos
        indice =1
        self.ultimo_mod = indice
        for cohorte in cohortes:
            if (cohorte.semestre == self.semestre and cohorte.ano == self.year) :
                label = QtGui.QLabel()
                time_ini = cohorte.fecha_inicio
                time_final = cohorte.fecha_fin
                self.ui.grid.setRowMinimumHeight(indice,20)
                label.setText(QString(str (indice)))
                label.setObjectName(QString(str (cohorte.id_cohorte)))
                fecha_inicio = QtGui.QDateEdit()
                fecha_fin = QtGui.QDateEdit()
                #fecha de inicio
                name = str (indice)
                fecha_inicio.setCalendarPopup(True)
                fecha_inicio.setCursor(QtGui.QCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor)))
                fecha_inicio.setObjectName(name)
                #fecha de fin
                fecha_fin.setCalendarPopup(True)
                fecha_fin.setCursor(QtGui.QCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor)))
                fecha_fin.setObjectName(name)
                checkBox = QtGui.QCheckBox()
                checkBox.setCursor(QtGui.QCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor)))
                checkBox.setText(QString("guardar"))
                checkBox.setObjectName(QString (name))
                label_estado = QtGui.QLabel()
                if (cohorte.fecha_inicio != None and cohorte.fecha_fin != None) :
                    print "paso"
                    fecha_ini = cohorte.fecha_inicio  #fecha
                    label_estado.setText(QString("Asignado"))
                    fecha_inicio.setDate(QDate(cohorte.fecha_inicio)) #label
                    fecha_fin.setDateRange(cohorte.fecha_inicio,fecha_limit)
                    fecha_fin.setDate(QDate(cohorte.fecha_fin))
                    if (fecha_ini < self.fecha_actual):
                        fecha_inicio.setDateRange(fecha_ini,fecha_limit)
                    else:
                        fecha_inicio.setDateRange(self.fecha_actual,fecha_limit)

                else :
                    label_estado.setText(QString("No Asignado"))
                    fecha_inicio.setDateRange(self.fecha_actual,fecha_limit)
                    fecha_fin.setDateRange(self.fecha_actual,fecha_limit)

                self.connect(fecha_fin, SIGNAL("dateChanged(QDate)"),self.fin_cambiado)
                self.connect(fecha_inicio, SIGNAL("dateChanged(QDate)"),self.inicio_cambiado)
                self.connect(checkBox, SIGNAL("stateChanged(int)"),self.cambio)
                self.ui.grid.addWidget(label,indice,0)
                self.ui.grid.addWidget(fecha_inicio,indice,1)
                self.ui.grid.addWidget(fecha_fin,indice,2)
                self.ui.grid.addWidget(checkBox,indice,3)
                self.ui.grid.addWidget(label_estado,indice,4)
                indice +=1
            self.ultimo_mod = indice

    def cambio (self,estado):
        sender = self.sender()
        fila = int (sender.objectName())
        if (estado == 2):
            self.list_actividades.append(fila)
            print self.list_actividades
            # item = self.ui.grid.itemAtPosition(fila,0)
            # print item.widget()
        elif (estado == 0):
            self.list_actividades.remove(fila)
            print self.list_actividades

    def inicio_cambiado (self,fecha):

        sender = self.sender()
        fila = int (sender.objectName())
        item = self.ui.grid.itemAtPosition(fila,2)
        fecha_fin = item.widget()
        fecha_fin.setDateRange(fecha,self.fecha_limit)

    def fin_cambiado (self,fecha):
        sender = self.sender()
        fila = int (sender.objectName())
        item = self.ui.grid.itemAtPosition(fila,1)
        fecha_inicio = item.widget()  #label
        fecha_ini = fecha_inicio.date() #fecha del label
        fecha_inicio.setDateRange(fecha_ini,fecha)


    def guardar(self):
        for fila in self.list_actividades:
            item = self.ui.grid.itemAtPosition(fila,0)
            label_cohorte = item.widget()
            item1 = self.ui.grid.itemAtPosition(fila,1)
            wid_fecha_inicio= item1.widget()
            item2 = self.ui.grid.itemAtPosition(fila,2)
            wid_fecha_fin= item2.widget()
            item3 = self.ui.grid.itemAtPosition(fila,4)
            estado= item3.widget()
            cohorte = int(str(label_cohorte.objectName()))
            fecha_inicio = str (wid_fecha_inicio.date().toString(QString ("dd/MM/yyyy")))
            fecha_fin= str (wid_fecha_fin.date().toString(QString ("dd/MM/yyyy")))

            exito = self.fachadaCordinador.modificar_cohorte(self.id_curso,cohorte,fecha_inicio,fecha_fin)
            if (exito):
                estado.setText ("Asignado")
            else :
                QtGui.QMessageBox.warning(self, 'Error', "no se pudo guardar", QtGui.QMessageBox.Ok)
        self.close()