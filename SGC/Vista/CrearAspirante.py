# -*- coding: utf-8 -*-
from PyQt4 import uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui
from sqlalchemy.exc import SQLAlchemyError
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
        self.validaciones()
        self.ui.txtCorreo.textChanged.connect(self.check_state)
        self.validacion()


    def __del__ ( self ):
        self.ui = None

    def validaciones(self):
        validador = QIntValidator()
        exp_correo = QRegExp('^.*[@].*[.].*')
        exp_cadena = QRegExp('.+')
        val_correo = QRegExpValidator(exp_correo)
        val_vacio = QRegExpValidator(exp_cadena)
        self.ui.txtCorreo.setValidator(val_correo)

    def validacion(self):
        correo = self.ui.txtCorreo.validator().validate(self.ui.txtCorreo.text(), 0)[0]
        if (correo) == 2:
            return True
        else:
            return False

    def check_state(self):
        sender = self.sender()
        validator = sender.validator()
        state = validator.validate(sender.text(), 0)[0]
        if state == QValidator.Acceptable:
            color = '#c4df9b'  # green
        elif state == QValidator.Intermediate:
            color = '#fff79a'  # yellow
        else:
            color = '#f6989d'  # red
        sender.setStyleSheet('QLineEdit { background-color: %s }' % color)

    def buscaCaracter(self, caracter, cadena):
        booleano = False
        for letra in cadena:
            if letra == caracter:
                booleano = True
        return booleano

    def cancelar_clicked(self):
        self.close()

    def inscribir_clicked(self):
        print("Capturando Informacion...")
        try:
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
            if (cedula=="" or nombre=="" or apellidos==""):
                QMessageBox.information(self, "Aspirante", "El campo Identificacion, Nombre y Apellidos son obligatorios")
            elif (self.validacion() != 1):
                if (self.buscaCaracter("@", correo) == True):
                    QMessageBox.information(self, "Aspirante", "Correo debe contener un punto despues del arroba")
                elif (self.buscaCaracter(".", correo) == True):
                    QMessageBox.information(self, "Aspirante", "Correo debe contener un arroba antes del punto")
                else:
                    QMessageBox.information(self, "Aspirante", "Correo debe contener un @ y luego un punto")

            else:

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


                if(self.ControlDigi.agregarAspirante(parametros)=="Fracaso"):
                    QtGui.QMessageBox.warning(self, self.tr("Error en Base de Datos"),
                                      QString.fromUtf8("Error en Base de Datos. \n"
                                                              "Ya existe aspirante"))
                    self.ui.txtid.setFocus(True)
                else:
                    self.ControlDigi.cerrarSesion()
                    self.ui.txtid.setText("")

        except:
            QtGui.QMessageBox.warning(self, self.tr("Error en Base de Datos"),
                                      QString.fromUtf8("Error en Base de Datos."))