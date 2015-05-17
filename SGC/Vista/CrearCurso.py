# -*- coding: utf-8 -*-
from PyQt4 import uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui
from sqlalchemy.exc import SQLAlchemyError
import sys

from Control.ControlCoordinador import ControlCoordinador


( Ui_CrearCurso, QDialog ) = uic.loadUiType( 'CrearCurso.ui' )

class CrearCurso ( QDialog ):
    """CrearCurso inherits QDialog"""
    tipo=1

    def __init__ ( self, parent = None , tipo=1):
        self.tipo= tipo
        self.control= ControlCoordinador()
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
			self.ui.label.setText(QString.fromUtf8("<P><b><FONT SIZE = 4> Creación de cursos </b></P></br>") )
        elif tipo ==2:
			self.ui.btBuscar.setVisible(True)
			self.ui.btCrear.setText("Modificar Curso")
			self.ui.leNombre.setEnabled(True)
			self.ui.teDescripcion.setEnabled(True)
			self.ui.label.setText(QString.fromUtf8("<P><b><FONT SIZE = 4> Edición de cursos </b></P></br>") )
        elif tipo==3:
			self.ui.btBuscar.setVisible(True)
			self.ui.btCrear.setText("Borrar Curso")
			self.ui.leNombre.setEnabled(True)
			self.ui.teDescripcion.setEnabled(False)
			self.ui.label.setText(QString.fromUtf8("<P><b><FONT SIZE = 4> Eliminación de cursos </b></P></br>") )

    def __del__ ( self ):
        self.ui = None
    
    def change_actividades(self):
        self.ui.twActividades.setRowCount(self.ui.sbNumActividades.value())
        
    def cancelar_clicked(self):
        self.close()
        
    def crear_clicked(self):
		if self.tipo==1:
			nombre_c= str(self.ui.leNombre.text())
			descripcion_c =str(self.ui.teDescripcion.toPlainText())
			if not (nombre_c.strip()=="" or descripcion_c.strip()==""):
				try:
					i=0
					actividades = []
					acum_pon = 0
					while i<self.ui.sbNumActividades.value():
						nombre_ac = str(self.ui.twActividades.item(i, 0).text())
						if nombre_ac.strip()=="":
							QtGui.QMessageBox.warning(self, self.tr("Error en datos"),
												   QString.fromUtf8("Recuerde llenar todos los campos."))
						ponderado_ac = float(self.ui.twActividades.item(i, 1).text())/100 #la idea es que el usuario ingrese un numero entre 0 y 100
						acum_pon+=ponderado_ac
						actividades.append([nombre_ac, ponderado_ac])
						i+=1
					if not(acum_pon==1 or self.ui.sbNumActividades.value()==0) :
						QtGui.QMessageBox.warning(self, self.tr("Error en datos"),
												   QString.fromUtf8("Recuerde que la suma de ponderados de todas las actividades debe dar 100"))
					else:
						self.control.crearCurso(nombre_c,descripcion_c,actividades)
						self.close()
						self.control.cerrarSesion()
				except SQLAlchemyError:
					QtGui.QMessageBox.warning(self, self.tr("Error en Base de Datos"),
												   QString.fromUtf8("Error en Base de Datos. \n"
												   "Recuerde que los nombres de los cursos son únicos \n"
												   "y que no debe haber dos actividades con el mismo nombre en el mismo curso."))
				except:
					QtGui.QMessageBox.warning(self, self.tr("Error en datos"),
												   QString.fromUtf8("Recuerde que los ponderados de las actividades deben ser numeros entre 0 y 100."))
			else:
				QtGui.QMessageBox.warning(self, self.tr("Error en datos"),
												   QString.fromUtf8("Recuerde llenar todos los campos."))

		elif self.tipo==2:
			nombre_c = str(self.ui.leNombre.text())
			descripcion=str(self.ui.teDescripcion.toPlainText())
			i=0
			actividades = []
			while i<self.ui.sbNumActividades.value():
				nombre_ac = str(self.ui.twActividades.item(i, 0).text())
				ponderado_ac = float(self.ui.twActividades.item(i, 1).text())
				actividades.append([nombre_ac, ponderado_ac])
				i+=1
			self.control.modificarCurso(nombre_c,descripcion, actividades)
			self.close()
			self.control.cerrarSesion()
		elif self.tipo==3:
			nombre_c = str(self.ui.leNombre.text())
			self.control.eliminarCurso(nombre_c)
			self.close()
			self.control.cerrarSesion()

    def buscar_clicked(self):
		curso = self.control.buscarCurso(str(self.ui.leNombre.text()))
		self.ui.teDescripcion.setText(curso.descripcion)
		self.ui.leNombre.setEnabled(False)
		if (self.tipo==2)|(self.tipo==3):
			actividades = curso.actividades
			self.ui.sbNumActividades.setValue(len(actividades))
			i=0
			for actividad in actividades:
				self.ui.twActividades.setItem(i, 0, QtGui.QTableWidgetItem())
				self.ui.twActividades.item(i, 0).setText(actividad.nombre)
				self.ui.twActividades.setItem(i, 1, QtGui.QTableWidgetItem())
				self.ui.twActividades.item(i, 1).setText(str(actividad.ponderado))
				i+=1
		
		    
