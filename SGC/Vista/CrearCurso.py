# -*- coding: utf-8 -*-
from PyQt4 import uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui
from sqlalchemy.exc import SQLAlchemyError
from VerEstudiantes import VerEstudiantes
from AnularLT import AnularLT

from Control.ControlCoordinador import ControlCoordinador


from datetime import date
import math

( Ui_CrearCurso, QDialog ) = uic.loadUiType('CrearCurso.ui')


class CrearCurso(QDialog):
    """CrearCurso inherits QDialog"""
    tipo = 1

    def __init__(self, parent=None, tipo=1):
        self.tipo = tipo
        self.control = ControlCoordinador()
        QDialog.__init__(self, parent)
        self.ui = Ui_CrearCurso()
        self.ui.setupUi(self)
        self.id_curso = None
        self.ui.twActividades.setRowCount(self.ui.sbNumActividades.value())
        self.connect(self.ui.sbNumActividades, SIGNAL("valueChanged(int)"), self.change_actividades)
        self.connect(self.ui.btCancelar, SIGNAL("clicked()"), self.cancelar_clicked)
        self.connect(self.ui.btCrear, SIGNAL("clicked()"), self.crear_clicked)
        self.connect(self.ui.btBuscar, SIGNAL("clicked()"), self.buscar_clicked)
        self.connect(self.ui.btVer, SIGNAL("clicked()"), self.ver_clicked)
        if tipo == 1:  # crear
            self.ui.btBuscar.setVisible(False)
            self.ui.btCrear.setText("Crear Curso")
            self.ui.leNombre.setEnabled(True)
            self.ui.teDescripcion.setEnabled(True)
            self.ui.label.setText(QString.fromUtf8("<P><b><FONT SIZE = 4> Creación de cursos </b></P></br>"))
            self.ui.btVer.setVisible(False)
        elif tipo == 2:  # consultar
            self.ui.btBuscar.setVisible(True)
            self.ui.btCrear.setVisible(False)
            self.ui.leNombre.setEnabled(True)
            self.ui.teDescripcion.setEnabled(False)
            self.ui.label.setText(QString.fromUtf8("<P><b><FONT SIZE = 4> Edición de cursos </b></P></br>"))
            self.ui.btVer.setText(QString.fromUtf8("Ver Estudiantes"))
            self.ui.btVer.setVisible(True)
        elif tipo == 3:  # modificar
            self.ui.btBuscar.setVisible(True)
            self.ui.btCrear.setText("Modificar Curso")
            self.ui.leNombre.setEnabled(True)
            self.ui.teDescripcion.setEnabled(True)
            self.ui.label.setText(QString.fromUtf8("<P><b><FONT SIZE = 4> Edición de cursos </b></P></br>"))
            self.ui.btVer.setText(QString.fromUtf8("Anular Matrícula a LT"))
            self.ui.btVer.setVisible(True)
        elif tipo == 4:  # Eliminar
            self.ui.btBuscar.setVisible(True)
            self.ui.btCrear.setText("Eliminar Curso")
            self.ui.leNombre.setEnabled(True)
            self.ui.teDescripcion.setEnabled(False)
            self.ui.label.setText(QString.fromUtf8("<P><b><FONT SIZE = 4> Eliminación de cursos </b></P></br>"))
            self.ui.btVer.setVisible(False)

    def __del__(self):
        self.ui = None

    def change_actividades(self):

        self.ui.twActividades.setRowCount(self.ui.sbNumActividades.value())

    def cancelar_clicked(self):

        self.close()

    def crear_clicked(self):
        if self.tipo == 1:
            nombre_c = str(self.ui.leNombre.text())
            descripcion_c = str(self.ui.teDescripcion.toPlainText())
            if not (nombre_c.strip() == "" or descripcion_c.strip() == ""):
                try:
                    i = 0
                    actividades = []
                    acum_pon = 0
                    flag = False
                    while i < self.ui.sbNumActividades.value():
                        nombre_ac = str(self.ui.twActividades.item(i, 0).text())
                        if nombre_ac.strip() == "":
                            QtGui.QMessageBox.warning(self, self.tr("Error en datos"),
                                                      QString.fromUtf8("Recuerde llenar todos los campos."))
                            flag = True
                            break
                        ponderado_ac = float(self.ui.twActividades.item(i,
                                                                        1).text()) / 100  # la idea es que el usuario ingrese un numero entre 0 y 100
                        acum_pon += ponderado_ac
                        actividades.append([nombre_ac, ponderado_ac])
                        i += 1
                    if not (acum_pon == 1 or self.ui.sbNumActividades.value() == 0) and flag:
                        QtGui.QMessageBox.warning(self, self.tr("Error en datos"),
                                                  QString.fromUtf8(
                                                      "Recuerde que la suma de ponderados de todas las actividades debe dar 100"))
                    else:
                        self.control.crearCurso(nombre_c, descripcion_c, actividades)
                        self.close()
                        self.control.cerrarSesion()
                except SQLAlchemyError, e:
                   QtGui.QMessageBox.warning(self, self.tr("Error en Base de Datos"),
                                             QString.fromUtf8("Error en Base de Datos. \n"
                                                              "Recuerde que los nombres de los cursos son únicos \n"
                                                              "y que no debe haber dos actividades con el mismo nombre en el mismo curso."))
                   print e
                except:
                   QtGui.QMessageBox.warning(self, self.tr("Error en datos"),
                                             QString.fromUtf8(
                                                 "Recuerde que los ponderados de las actividades deben ser numeros entre 0 y 100."))
            else:
                QtGui.QMessageBox.warning(self, self.tr("Error en datos"),
                                          QString.fromUtf8("Recuerde llenar todos los campos."))
        elif self.tipo == 3:
            nombre_c = str(self.ui.leNombre.text())
            descripcion_c = str(self.ui.teDescripcion.toPlainText())
            if not (descripcion_c.strip() == ""):
                try:
                    i = 0
                    actividades = []
                    acum_pon = 0
                    flag = False
                    while i < self.ui.sbNumActividades.value():
                        nombre_ac = str(self.ui.twActividades.item(i, 0).text())
                        if nombre_ac.strip() == "":
                            QtGui.QMessageBox.warning(self, self.tr("Error en datos"),
                                                      QString.fromUtf8("Recuerde llenar todos los campos."))
                            flag = True
                            break
                        ponderado_ac = float(self.ui.twActividades.item(i,
                                                                        1).text()) / 100  # la idea es que el usuario ingrese un numero entre 0 y 100
                        acum_pon += ponderado_ac
                        actividades.append([nombre_ac, ponderado_ac])
                        i += 1
                    if not (acum_pon == 1 or self.ui.sbNumActividades.value() == 0) and flag:
                        QtGui.QMessageBox.warning(self, self.tr("Error en datos"),
                                                  QString.fromUtf8(
                                                      "Recuerde que la suma de ponderados de todas las actividades debe dar 100"))
                    else:
                        self.control.modificarCurso(nombre_c, descripcion_c, actividades)
                        self.close()
                        self.control.cerrarSesion()
                except SQLAlchemyError, e:
                   QtGui.QMessageBox.warning(self, self.tr("Error en Base de Datos"),
                                             QString.fromUtf8("Error en Base de Datos. \n"
                                                              "Recuerde que los nombres de los cursos son únicos \n"
                                                              "y que no debe haber dos actividades con el mismo nombre en el mismo curso."))
                   print e
                except:
                   QtGui.QMessageBox.warning(self, self.tr("Error en datos"),
                                             QString.fromUtf8(
                                                 "Recuerde que los ponderados de las actividades deben ser numeros entre 0 y 100."))
            else:
                QtGui.QMessageBox.warning(self, self.tr("Error en datos"),
                                          QString.fromUtf8("Recuerde llenar todos los campos."))
        elif self.tipo == 4:
            nombre_c = str(self.ui.leNombre.text())
            self.control.eliminarCurso(nombre_c)
            self.close()

    def buscar_clicked(self):
        curso = self.control.buscarCurso(str(self.ui.leNombre.text()))
        if not curso==None:
            self.id_curso = curso.id
            self.ui.teDescripcion.setText(curso.descripcion)
            self.ui.leNombre.setEnabled(False)
            if (self.tipo == 2) | (self.tipo == 3) | (self.tipo == 4):
                actividades = curso.actividades
                self.ui.sbNumActividades.setValue(len(actividades))
                i = 0
                for actividad in actividades:
                    self.ui.twActividades.setItem(i, 0, QtGui.QTableWidgetItem())
                    self.ui.twActividades.item(i, 0).setText(actividad.nombre)
                    self.ui.twActividades.setItem(i, 1, QtGui.QTableWidgetItem())
                    self.ui.twActividades.item(i, 1).setText(str(actividad.ponderado))
                    if self.tipo==2:
                        self.ui.twActividades.item(i, 0).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
                        self.ui.twActividades.item(i, 1).setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
                    i += 1
        else:
            QtGui.QMessageBox.warning(self, self.tr("Error en datos"),
                                          QString.fromUtf8("El curso no existe."))
    def ver_clicked(self):
        ano = date.today().year
        semestre  = math.ceil(float(date.today().month)/6)
        if self.id_curso!=None and self.control.consultarNumCohortes(self.id_curso,ano,semestre)!=0:
            if self.tipo == 2: #ver estudiantes
                    v = VerEstudiantes(None, self.id_curso).exec_()
            elif self.tipo == 3: #anular matricula
                v = AnularLT(None, self.id_curso).exec_()
        else:
            QtGui.QMessageBox.warning(self, self.tr("Error"),
                                              QString.fromUtf8("No hay cohortes asociados a este curso en este semestre."))

