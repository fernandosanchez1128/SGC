# -*- coding: utf-8 -*-
from PyQt4 import uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui
from Control.ControlDigitador import *



( Ui_VistaAspirante, QDialog ) = uic.loadUiType( 'VistaAspirante.ui' )

class CrearAspirante ( QDialog ):

    def __init__ ( self, parent = None):
        self.ControlDigi = ControlDigitador()
        QDialog.__init__( self, parent )
        self.ui = Ui_VistaAspirante()
        self.ui.setupUi( self )
        self.connect(self.ui.btSalir, SIGNAL("clicked()"), self.cancelar_clicked)
        self.connect(self.ui.btAceptar, SIGNAL("clicked()"), self.inscribir_clicked)


    def __del__ ( self ):
        self.ui = None

    def cancelar_clicked(self):
        self.close()

    def inscribir_clicked(self):
        print("Capturando Informacion...")
        parametros=[]
        cedula=str(self.ui.txtid.text())
        nombre=str(self.ui.txtNombre.text())
        apellidos=str(self.ui.txtApellidos.text())
        correo=str(self.ui.txtCorreo.text())
        celular=str(self.ui.txtCelular.text())
        direccion=str(self.ui.txtDireccion.text())
        genero=""
        if(self.ui.femenino.isChecked()):
            genero="Femenino"
        if(self.ui.masculino.isChecked()):
            genero="Masculino"
        f_nacimiento=str(QDate.toPyDate(self.ui.calendario.selectedDate()))
        ###1 DE 3
        sede=str(self.ui.txtSede.text())
        institucion=str(self.ui.txtInstitucion.text())
        Dane=str(self.ui.txtDane.text())
        grado=str(self.ui.txtGrado.text())
        secretaria=str(self.ui.txtSecretaria.text())
        municipio=str(self.ui.txtMunicipio.text())
        ###2 DE 3

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


        #print("AKSNDOAI:",newcurso.id)
        parametros.append(cedula)
        parametros.append(nombre)
        parametros.append(apellidos)
        parametros.append(direccion)
        parametros.append(celular)
        parametros.append(correo)
        parametros.append(f_nacimiento)
        parametros.append(municipio)
        parametros.append(genero)
        parametros.append(institucion)
        parametros.append(grado)
        parametros.append(sede)
        parametros.append(Dane)
        parametros.append(secretaria)
        parametros.append(tutor)
        parametros.append(col_aprende)

        self.ControlDigi.agregarAspirante(parametros)
