__author__ = 'JuanD'

import sys
import os
from PyQt4 import uic
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Control.ControlCoordinador import ControlCoordinador

( Ui_VistaDescargarCertificado, QDialog ) = uic.loadUiType( 'vistadescargarcertificado.ui' )

class VistaDescargarCertificado ( QDialog ):
    """VistaLogin inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.controlCoordinador = ControlCoordinador()
        self.ui = Ui_VistaDescargarCertificado()
        self.ui.setupUi( self )
        self.connect(self.ui.btnBuscar, SIGNAL("clicked()"), self.buscar_clicked)
        self.connect(self.ui.btnDescargar, SIGNAL("clicked()"), self.descargar_clicked)
        self.ui.comboCursos.setEnabled(0)
        self.ui.btnDescargar.setEnabled(0)

    def buscar_clicked(self):
        self.ui.comboCursos.clear()
        self.cedula=str(self.ui.txtCedula.text())
        if self.cedula!=None and self.cedula != "":
            self.matriculas=self.controlCoordinador.cursosTerminadosEstudiantes(self.cedula)
            self.idsCursos=[]
            self.nombresCursos=[]
            for matricula in self.matriculas:
                idCurso=matricula.id_curso
                self.idsCursos.append(idCurso)
                curso=self.controlCoordinador.buscarCursoId(idCurso)
                nombreCurso=curso.nombre
                self.nombresCursos.append(nombreCurso)
            for nombre in self.nombresCursos:
                self.ui.comboCursos.addItem(nombre)
            if len(self.nombresCursos)<1:
                self.ui.comboCursos.setEnabled(0)
                self.ui.btnDescargar.setEnabled(0)
            else:
                self.ui.comboCursos.setEnabled(1)
                self.ui.btnDescargar.setEnabled(1)


    def descargar_clicked(self):
        indice= self.ui.comboCursos.currentIndex()
        ruta = QFileDialog.getSaveFileName(self, 'Guardar Certficado', '', selectedFilter='*.pdf')
        if ruta:
            print ruta
            persona=self.controlCoordinador.buscarPersona(self.cedula)
            nombre=persona.nombres
            apellido=persona.apellidos
            nombreCompleto=str(nombre)+" "+str(apellido)
            nota=self.matriculas[indice-1].nota_definitiva
            nota=float(nota)
            nomCurso=str(self.nombresCursos[indice-1])
            self.controlCoordinador.descargaCertificado(ruta, nombreCompleto, self.cedula, nota, nomCurso)
        else:
            print "No se proporciono nombre de archivo"



    def __del__ ( self ):
        self.ui = None