from PyQt4 import uic
from PyQt4 import QtGui
from PyQt4.QtCore import *
from Control.FachadaMt import FachadaMt

( Ui_Asignacion, QMainWindow ) = uic.loadUiType( 'Asignacion.ui' )

class Asignacion ( QMainWindow ):
    """Asignacion inherits QMainWindow"""
    id_curso = 0
    id_cohorte =0
    fachadaMt = FachadaMt()
    list_actividades = []
    def __init__ ( self,id_curso, id_cohorte, parent = None):
        QMainWindow.__init__( self, parent )
        self.id_curso = id_curso
        self.id_cohorte = id_cohorte
        self.ui = Ui_Asignacion()
        self.ui.setupUi( self )
        self.cargar_grid()
        self.connect(self.ui.guardar, SIGNAL("clicked()"), self.guardar)


    def __del__ ( self ):
        self.ui = None

    def cargar_grid(self):
        print "curso", self.id_curso,self.id_cohorte
        curso = self.fachadaMt.consulta_curso(self.id_curso)
        actividades = curso.actividades
        self.fachadaMt.cerrar_session_curso()
        indice =1
        cohorte = self.fachadaMt.consultar_cohorte(self.id_curso,self.id_cohorte)
        time_ini = cohorte.fecha_inicio
        time_final = cohorte.fecha_fin
        for actividad in actividades:
            label = QtGui.QLabel()
            self.ui.grid.setRowMinimumHeight(indice,20)
            label.setText(QString(actividad.nombre))
            fecha = QtGui.QDateTimeEdit()
            fecha.setCalendarPopup(True)
            fecha.setDateRange(time_ini,time_final)
            checkBox = QtGui.QCheckBox()
            checkBox.setText(QString("Asignar"))
            name = str (indice)
            checkBox.setObjectName(QString (name))
            print checkBox.objectName()
            self.connect(checkBox, SIGNAL("stateChanged(int)"),self.cambio)
            label_estado = QtGui.QLabel()
            id_actividad = actividad.id_actividad
            asignacion = self.fachadaMt.consular_asignacion(self.id_curso,self.id_cohorte,id_actividad)
            if (asignacion != None):
                label_estado.setText(QString("Asignado"))
                fecha.setDateTime(QDateTime(asignacion.fecha_hora))
            else :
                label_estado.setText(QString("No Asignado"))
            self.ui.grid.addWidget(label,indice,0)
            self.ui.grid.addWidget(fecha,indice,1)
            self.ui.grid.addWidget(checkBox,indice,2)
            self.ui.grid.addWidget(label_estado,indice,3)
            indice +=1


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


    def guardar(self):
        for fila in self.list_actividades :
            item = self.ui.grid.itemAtPosition(fila,0)
            label_nombre = item.widget()
            item1 = self.ui.grid.itemAtPosition(fila,1)
            fecha= item1.widget()
            item2 = self.ui.grid.itemAtPosition(fila,3)
            estado= item2.widget()
            nombre_actividad = str (label_nombre.text())
            id_actividad = self.fachadaMt.consultar_actividad(nombre_actividad,self.id_curso).id_actividad
            fecha_entrega =  str (fecha.dateTime().toString(QString ("dd/MM/yyyy:hh:mm")))
            print fecha_entrega
            estado.setText ("Asignado")
            self.fachadaMt.agregar_entrega(self.id_curso,self.id_cohorte,id_actividad,fecha_entrega)