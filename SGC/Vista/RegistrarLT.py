# -*- coding: utf-8 -*-
from PyQt4 import uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui

##from Modelo.LogicaCursos import *
##from ORM.Curso import *
##from ORM.Actividades import *
##from Modelo.LogicaActividades import *


( Ui_VistaRegistrarLT, QDialog ) = uic.loadUiType( 'VistaRegistrarLT.ui' )

class RegistrarLT ( QDialog ):

    def __init__ ( self, parent = None):
        #self.tipo= tipo
        #self.logicaCursos= LogicaCursos()
        #self.logicaActividades= LogicaActividades()
        QDialog.__init__( self, parent )
        self.ui = Ui_VistaRegistrarLT()
        self.ui.setupUi( self )
        #self.ui.twActividades.setRowCount(self.ui.sbNumActividades.value())
        #self.connect(self.ui.sbNumActividades, SIGNAL("valueChanged(int)"), self.change_actividades)
        self.connect(self.ui.btSalir, SIGNAL("clicked()"), self.cancelar_clicked)
        self.connect(self.ui.btRegistrar, SIGNAL("clicked()"), self.inscribir_clicked)
        self.connect(self.ui.btBuscar, SIGNAL("clicked()"), self.buscar_clicked)


    def __del__ ( self ):
        self.ui = None

    def cancelar_clicked(self):
        self.close()
    
    def buscar_clicked(self):
        print("Buscando...")

    def inscribir_clicked(self):
        print("Capturando Informacion...")
        Zonas=[]
        Modalidad=[]
        ModalidadTec=[]
        if (self.ui.zonaurbana.isChecked()):
            Zonas.append("Zona urbana")
        if (self.ui.zonaurbanamarginada.isChecked()):
            Zonas.append("Zona urbana marginada")
        if (self.ui.zonarural.isChecked()):
            Zonas.append("Zona rural")
        if (self.ui.zonaruraldificil.isChecked()):
            Zonas.append("Zona rural dificil acceso")
        print(Zonas)
        if (self.ui.modalacademica.isChecked()):
            Modalidad.append("Academica")
        elif(self.ui.modaltecnica.isChecked()):
            Modalidad.append("Tecnica")
        print(Modalidad)
        if (self.ui.agro.isChecked()):
            ModalidadTec.append("Agropecuario")
        if (self.ui.comercial.isChecked()):
            ModalidadTec.append("Comercial")
        if (self.ui.promoSionSocial.isChecked()):
            ModalidadTec.append("Promocion Social")
        print(ModalidadTec)

    '''
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
	'''