# -*- coding: utf-8 -*-
from PyQt4 import uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui

from Modelo.LogicaCursos import *
from ORM.Curso import *
from ORM.Actividades import *
from Modelo.LogicaActividades import *

( Ui_CrearCurso, QDialog ) = uic.loadUiType( 'CrearCurso.ui' )

class CrearCurso ( QDialog ):
    """CrearCurso inherits QDialog"""
    tipo=1

    def __init__ ( self, parent = None , tipo=1):
        self.tipo= tipo
        self.logicaCursos= LogicaCursos()
        self.logicaActividades= LogicaActividades()
        QDialog.__init__( self, parent )
        self.ui = Ui_CrearCurso()
        self.ui.setupUi( self )
        self.ui.twActividades.setRowCount(self.ui.sbNumActividades.value())
        self.connect(self.ui.sbNumActividades, SIGNAL("valueChanged(int)"), self.change_actividades)
        self.connect(self.ui.btCancelar, SIGNAL("clicked()"), self.cancelar_clicked)
        self.connect(self.ui.btCrear, SIGNAL("clicked()"), self.crear_clicked)
        self.connect(self.ui.btBuscar, SIGNAL("clicked()"), self.buscar_clicked)
        if tipo ==1:
			self.ui.btBuscar.setVisible(False)
			self.ui.btCrear.setText("Crear Curso")
			self.ui.leNombre.setEnabled(True)
			self.ui.teDescripcion.setEnabled(True)
			self.ui.label.setText("Creación de cursos")
        elif tipo ==2:
			self.ui.btBuscar.setVisible(True)
			self.ui.btCrear.setText("Modificar Curso")
			self.ui.leNombre.setEnabled(True)
			self.ui.teDescripcion.setEnabled(True)
			self.ui.label.setText("Edición de cursos")
        elif tipo==3:
			self.ui.btBuscar.setVisible(True)
			self.ui.btCrear.setText("Borrar Curso")
			self.ui.leNombre.setEnabled(True)
			self.ui.teDescripcion.setEnabled(False)
			self.ui.label.setText("Eliminación de cursos")

    def __del__ ( self ):
        self.ui = None
    
    def change_actividades(self):
        self.ui.twActividades.setRowCount(self.ui.sbNumActividades.value())
        
    def cancelar_clicked(self):
        self.close()
        
    def crear_clicked(self):
		if self.tipo==1:
			curso = Curso(nombre= str(self.ui.leNombre.text()), descripcion=str(self.ui.teDescripcion.toPlainText()))
			self.logicaCursos.agregarCurso(curso)
			i=0
			curso = self.logicaCursos.consultarCurso(str(self.ui.leNombre.text()))
			while i<self.ui.sbNumActividades.value():
				nombre_ac = str(self.ui.twActividades.item(i, 0).text())
				ponderado_ac = float(self.ui.twActividades.item(i, 1).text())
				actividad = Actividades(nombre = nombre_ac, ponderado = ponderado_ac, id_curso = curso.id )
				self.logicaActividades.agregarActividades(actividad)
				i+=1
			self.close()
		elif self.tipo==2:
			nombre_c = str(self.ui.leNombre.text())
			curso = Curso(nombre= nombre_c, descripcion=str(self.ui.teDescripcion.toPlainText()))
			self.logicaCursos.modificarCurso(nombre_c, curso)
			i=0
			curso = self.logicaCursos.consultarCurso(nombre_c)
			self.logicaActividades.eliminarActividadesXCurso(curso.id)
			while i<self.ui.sbNumActividades.value():
				nombre_ac = str(self.ui.twActividades.item(i, 0).text())
				ponderado_ac = float(self.ui.twActividades.item(i, 1).text())
				actividad = Actividades(nombre = nombre_ac, ponderado = ponderado_ac, id_curso =curso.id )
				self.logicaActividades.agregarActividades(actividad)
				i+=1
			self.close()
		elif self.tipo==3:
			id_curso_mod = self.logicaCursos.consultarCurso(str(self.ui.leNombre.text())).id
			self.logicaActividades.eliminarActividadesXCurso(id_curso_mod)
			self.logicaCursos.eliminarCurso(id_curso_mod)
			self.close()

    def buscar_clicked(self):
		curso = self.logicaCursos.consultarCurso(str(self.ui.leNombre.text()))
		self.ui.teDescripcion.setText(curso.descripcion)
		self.ui.leNombre.setEnabled(False)
		if (self.tipo==2)|(self.tipo==3):
			id_c = self.logicaCursos.consultarCurso(str(self.ui.leNombre.text())).id
			actividades = self.logicaActividades.consultarActividadesXCurso(id_c)
			self.ui.sbNumActividades.setValue(len(actividades))
			i=0
			for actividad in actividades:
				self.ui.twActividades.setItem(i, 0, QtGui.QTableWidgetItem())
				self.ui.twActividades.item(i, 0).setText(actividad.nombre)
				self.ui.twActividades.setItem(i, 1, QtGui.QTableWidgetItem())
				self.ui.twActividades.item(i, 1).setText(str(actividad.ponderado))
				i+=1
		
		    
