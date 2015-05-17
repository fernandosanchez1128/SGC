# -*- coding: utf-8 -*-
from PyQt4 import uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui

##from Modelo.LogicaCursos import *
##from ORM.Curso import *
##from ORM.Actividades import *
##from Modelo.LogicaActividades import *


( Ui_VistaPreinscribirLT, QDialog ) = uic.loadUiType( 'VistaPreinscribirLT.ui' )

class PreinscribirLT ( QDialog ):

    def __init__ ( self, parent = None):
        #self.tipo= tipo
        #self.logicaCursos= LogicaCursos()
        #self.logicaActividades= LogicaActividades()
        QDialog.__init__( self, parent )
        self.ui = Ui_VistaPreinscribirLT()
        self.ui.setupUi( self )
        for i in range(3):
            self.ui.comboCursos.addItem("curso"+QString(str(i)))
        #self.ui.twActividades.setRowCount(self.ui.sbNumActividades.value())
        #self.connect(self.ui.sbNumActividades, SIGNAL("valueChanged(int)"), self.change_actividades)
        self.connect(self.ui.btSalir, SIGNAL("clicked()"), self.cancelar_clicked)
        self.connect(self.ui.btAceptar, SIGNAL("clicked()"), self.inscribir_clicked)


    def __del__ ( self ):
        self.ui = None

    def cancelar_clicked(self):
        self.close()

    def inscribir_clicked(self):
        print("Capturando Informacion...")
        cedula=str(self.ui.txtid.text())
        nombre=str(self.ui.txtNombre.text())
        apellidos=str(self.ui.txtApellidos.text())
        correo=str(self.ui.txtCorreo.text())
        celular=str(self.ui.txtCelular.text())
        direccion=str(self.ui.txtDireccion.text())
        if(self.ui.femenino.isChecked()):
            genero="Femenino"
        if(self.ui.masculino.isChecked()):
            genero="Masculino"
        f_nacimiento=QDate.getDate(self.ui.calendario.selectedDate())
        print(genero,f_nacimiento)
        ###1 DE 3
        sede=str(self.ui.txtSede.text())
        institucion=str(self.ui.txtInstitucion.text())
        Dane=str(self.ui.txtDane.text())
        grado=str(self.ui.txtGrado.text())
        secretaria=str(self.ui.txtSecretaria.text())
        municipio=str(self.ui.txtMunicipio.text())
        ###2 DE 3
        curso=str(self.ui.comboCursos.currentText())
        ##Tutor false aunque no seleccione ninguna
        if(self.ui.TutorSi.isChecked()):
            tutor=True
        else:
            tutor=False
        ###3 DE 3
        ##col_aprende false aunque no seleccione ninguna
        if(self.ui.ColAprendeSi.isChecked()):
            col_aprende=True
        else:
            col_aprende=False
        print(cedula,nombre,apellidos,correo,celular,direccion,sede,institucion,Dane,grado,secretaria,municipio,curso,tutor,col_aprende)


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