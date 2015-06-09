# -*- coding: utf-8 -*-
from PyQt4 import uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui
from sqlalchemy.exc import SQLAlchemyError

from Control.ControlDigitador import ControlDigitador


( Ui_VistaRegistrarLT, QDialog ) = uic.loadUiType( 'VistaRegistrarLT.ui' )

#[1:Crear 2;Editar 3:Consultar]
class RegistrarLT ( QDialog ):

    def __init__ ( self, parent = None, modo=1):
        self.tipo=modo
        self.cedula=""
        self.controldigi=ControlDigitador()
        self.flag=False
        self.obligatorios=""
        QDialog.__init__( self, parent )
        self.ui = Ui_VistaRegistrarLT()
        self.ui.setupUi( self )
        if(self.tipo==1):
            self.ui.tabWidget.removeTab(10)
            self.ui.tabWidget.removeTab(9)
        if(self.tipo==2):
            self.ui.lbModo.setText("EDICION")
            self.ui.btRegistrar.setText("Editar")
        if(self.tipo==3):
            self.ui.lbModo.setText("CONSULTA")
            self.ui.btRegistrar.setVisible(False)
        if(self.tipo==4):
            self.ui.lbModo.setText("ELIMINACION")
            self.ui.btRegistrar.setVisible(False)
            self.ui.btSalir.setText("Eliminar")

        self.connect(self.ui.btSalir, SIGNAL("clicked()"), self.cancelar_clicked)
        self.connect(self.ui.btRegistrar, SIGNAL("clicked()"), self.inscribir_clicked)
        self.connect(self.ui.btBuscar, SIGNAL("clicked()"), self.buscar_clicked)
        self.validaciones()
        self.ui.txtcorreo.textChanged.connect(self.check_state)
        self.validacion()



    def __del__ ( self ):
        self.ui = None

    def validaciones(self):
        validador = QIntValidator()
        exp_correo = QRegExp('^.*[@].*[.].*')
        exp_cadena = QRegExp('.+')
        val_correo = QRegExpValidator(exp_correo)
        val_vacio = QRegExpValidator(exp_cadena)
        self.ui.txtcorreo.setValidator(val_correo)

    def validacion(self):
        correo = self.ui.txtcorreo.validator().validate(self.ui.txtcorreo.text(), 0)[0]
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

    #Devuelve la cantidad de caracteres alfabeticos
    @staticmethod
    def validarcontrasena(cad):
        bandera=True
        cont=0
        for letra in cad:
            try:
                int(letra)
            except ValueError:
                cont+=1
        return cont




    def cancelar_clicked(self):
        if(self.tipo==4):
            cedula=str(self.ui.txtid.text())
            self.controldigi.eliminarLT(cedula)
        else:
            self.close()
    
    def buscar_clicked(self):
        print("Buscando...")
        try:
            ced=str(self.ui.txtid.text())
            self.cedula=ced
            if(self.tipo == 1):
                asp=self.controldigi.consultarAspirante(ced)
                if(asp==None):
                    QtGui.QMessageBox.warning(self, self.tr("Error en Base de Datos"),
                                          QString.fromUtf8("No hay Aspirante registrado con esa identificacion"))
                    self.ui.btRegistrar.setEnabled(False)
                else:
                    self.ui.btRegistrar.setEnabled(True)
                    self.ui.txtnombre.setText(asp.nombres)
                    self.ui.txtapellido.setText(asp.apellidos)

            else:
                #RECUPERANDO INFORMACION
                lt=self.controldigi.consultarLT(ced)
                user=self.controldigi.consultarUsuario(ced)
                if (lt!=None or user!=None):
                    self.ui.btRegistrar.setEnabled(True)
                    #DATOS DE USUARIO
                    self.ui.txtnombre.setText(user.nombres)
                    self.ui.txtapellido.setText(user.apellidos)
                    self.ui.txttelefono.setText(user.telefono)
                    self.ui.txtdireccion.setText(user.direccion)
                    self.ui.txtcorreo.setText(user.correo_electronico)
                    self.ui.txtpassword.setText(user.contrasena)
                    self.ui.calendario.setSelectedDate(QDate(user.fecha_nacimiento))

                    #DATOS de LEADER TEACHER
                    self.ui.txtmunicipio.setText(lt.municipio)
                    self.ui.txtinstitucion.setText(lt.institucion)
                    self.ui.txtescalafon.setText(lt.escalafon)
                    self.ui.txtsede.setText(lt.sede)
                    self.ui.txtdane.setText(lt.codigo_dane)
                    dptotemp=lt.dpto_secretaria
                    coldpto ={'Valle del Cauca':0,'Cauca':1,'Narino':2,'Tolima':3,'Huila':4,'Caqueta':5,'Putumayo':6,'Amazonas':7}
                    indexdpto=coldpto[dptotemp]
                    self.ui.txtsecretaria.setCurrentIndex(indexdpto)
                    if(lt.usuario_col_aprende):
                        self.ui.col_aprendeSi.setChecked(True)
                    else:
                        self.ui.col_aprendeNo.setChecked(True)
                    if(lt.tutor):
                        self.ui.tutorSi.setChecked(True)
                    else:
                        self.ui.tutorNo.setChecked(True)
                    if(lt.genero=="Femenino"):
                        print("truetutor")
                        self.ui.femenino.setChecked(True)
                    else:
                        self.ui.masculino.setChecked(True)

                    if(lt.tipo_institucion=="Academica"):
                        self.ui.modalacademica.setChecked(True)
                    else:
                        self.ui.modaltecnica.setChecked(True)

                    #6 de 9
                    if(lt.grado=="Nivel Tecnico"):
                        self.ui.niveltecnico.setChecked(True)
                    if(lt.grado=="Nivel Tecnologico"):
                        self.ui.niveltecnologico.setChecked(True)
                    if(lt.grado=="Nivel Profesional"):
                        self.ui.nivelprofesional.setChecked(True)
                    if(lt.grado=="Nivel Normalista Superior"):
                        self.ui.nivelnormalista.setChecked(True)
                    if(lt.grado=="Nivel Licenciatura"):
                        self.ui.nivellicenciatura.setChecked(True)
                    if(lt.grado=="Nivel Especializaciones"):
                        self.ui.nivelespecializaciones.setChecked(True)
                    if(lt.grado=="Nivel Maestria"):
                        self.ui.nivelmaestria.setChecked(True)
                    if(lt.grado=="Nivel Doctorado"):
                        self.ui.niveldoctorado.setChecked(True)

                    #8 y 9 Experiencias
                    self.ui.exppreescolar.setValue(lt.exp_preescolar)
                    self.ui.expprimaria.setValue(lt.exp_primaria)
                    self.ui.expsecundaria.setValue(lt.exp_secundaria)
                    self.ui.expmedia.setValue(lt.exp_media)
                    self.ui.expsuperior.setValue(lt.exp_superior)
                    self.ui.exprural.setValue(lt.exp_rural)
                    self.ui.expurbana.setValue(lt.exp_urbano)
                    self.ui.exppublico.setValue(lt.exp_publico)
                    self.ui.expprivado.setValue(lt.exp_privado)
                    self.ui.exptotal.setValue(lt.exp_total)

                    #Caso Multivaluados
                    for z in lt.zona:
                        if(z.zona=="Zona urbana"):
                            self.ui.zonaurbana.setChecked(True)
                        if (z.zona=="Zona urbana marginada"):
                            self.ui.zonaurbanamarginada.setChecked(True)
                        if (z.zona=="Zona rural"):
                            self.ui.zonarural.setChecked(True)
                        if (z.zona=="Zona rural dificil acceso"):
                            self.ui.zonaruraldificil.setChecked(True)

                    for m in lt.modalidad:
                        if (m.modalidad==("Agropecuario")):
                            self.ui.agro.setChecked(True)
                        elif (m.modalidad==("Comercial")):
                            self.ui.comercial.setChecked(True)
                        elif (m.modalidad==("Promocion Social")):
                            self.ui.promocionSocial.setChecked(True)
                        elif (m.modalidad==("Finanzas")):
                            self.ui.finanzas.setChecked(True)
                        elif (m.modalidad==("Administracion")):
                            self.ui.administracion.setChecked(True)
                        elif (m.modalidad==("Ecologia")):
                            self.ui.ecologia.setChecked(True)
                        elif (m.modalidad==("Medio Ambiente")):
                            self.ui.medioambiente.setChecked(True)
                        elif (m.modalidad==("Industrial")):
                            self.ui.industrial.setChecked(True)
                        elif (m.modalidad==("Informatica")):
                            self.ui.informatica.setChecked(True)
                        elif (m.modalidad==("Mineria")):
                            self.ui.mineria.setChecked(True)
                        elif (m.modalidad==("Salud")):
                            self.ui.salud.setChecked(True)
                        elif (m.modalidad==("Recreacion")):
                            self.ui.recreacion.setChecked(True)
                        elif (m.modalidad==("Turismo")):
                            self.ui.turismo.setChecked(True)
                        elif (m.modalidad==("Deporte")):
                            self.ui.deporte.setChecked(True)
                        else:
                            self.ui.otromodalidad.setChecked(True)
                            self.ui.txtotromodalidad.setText(m.modalidad)

                        #3 de 9
                    for et in lt.etnoeducacion:
                        if (et.etnoeducacion==("Etnia Afrocolombiana")):
                            self.ui.afro.setChecked(True)
                        if (et.etnoeducacion==("Etnia Indigena")):
                            self.ui.indigena.setChecked(True)
                        if (et.etnoeducacion==("Etnia Rom")):
                            self.ui.rom.setChecked(True)
                        if (et.etnoeducacion=="Ninguna Etnia"):
                            self.ui.ningunaetnia.setChecked(True)

                    for niv in lt.niveles_desempenados:
                        if (niv.niveles==("Transicion")):
                            self.ui.transicion.setChecked(True)
                        elif (niv.niveles==("Educacion Inicial")):
                            self.ui.eduinicial.setChecked(True)
                        elif (niv.niveles==("Educacion Primaria")):
                            self.ui.eduprimaria.setChecked(True)
                        elif (niv.niveles==("Educacion Secundaria")):
                            self.ui.edusecundaria.setChecked(True)
                        elif (niv.niveles==("Educacion Media")):
                            self.ui.edumedia.setChecked(True)
                        elif (niv.niveles==("Educacion Superior")):
                            self.ui.edusuperior.setChecked(True)
                        else:
                            self.ui.otronivel.setChecked(True)
                            self.ui.txtotronivel.setText(niv.niveles)

                    #4 de 9
                    for gr in lt.grados_desempenados:
                        if (gr.grados==("Grado Transicion")):
                            self.ui.gtransicion.setChecked(True)
                        elif (gr.grados=="Grado Inicial"):
                            self.ui.ginicial.setChecked(True)
                        elif (gr.grados=="Grado 1"):
                            self.ui.g1.setChecked(True)
                        elif (gr.grados=="Grado 2"):
                            self.ui.g2.setChecked(True)
                        elif (gr.grados=="Grado 3"):
                            self.ui.g3.setChecked(True)
                        elif (gr.grados==("Grado 4")):
                            self.ui.g4.setChecked(True)
                        elif (gr.grados==("Grado 5")):
                            self.ui.g5.setChecked(True)
                        elif (gr.grados==("Grado 6")):
                            self.ui.g6.setChecked(True)
                        elif (gr.grados==("Grado 7")):
                            self.ui.g7.setChecked(True)
                        elif (gr.grados==("Grado 8")):
                            self.ui.g8.setChecked(True)
                        elif (gr.grados==("Grado 9")):
                            self.ui.g9.setChecked(True)
                        elif (gr.grados==("Grado 10")):
                            self.ui.g10.setChecked(True)
                        elif (gr.grados==("Grado 11")):
                            self.ui.g11.setChecked(True)
                        else:
                            self.ui.gotro.setChecked(True)
                            self.ui.txtotrogrado.setText(gr.grados)

                    for ar in lt.areas_desempenadas:
                        if (ar.area==("Ciencias Naturales y Educacion Ambiental")):
                            self.ui.naturales.setChecked(True)
                        if (ar.area==("Ciencias Sociales")):
                            self.ui.sociales.setChecked(True)
                        if (ar.area==("Artistica")):
                            self.ui.artistica.setChecked(True)
                        if (ar.area==("Etica y Valores Humanos")):
                            self.ui.etica.setChecked(True)
                        if (ar.area==("Fisica Recreacion y Deportes")):
                            self.ui.fisica.setChecked(True)
                        if (ar.area==("Edicacion Religiosa")):
                            self.ui.religiosa.setChecked(True)
                        if (ar.area==("Humanidades Lengua Castellana e Idioma Extranjero")):
                            self.ui.humanidades.setChecked(True)
                        if (ar.area==("Matematicas")):
                            self.ui.matematicas.setChecked(True)
                        if (ar.area==("Tecnologia")):
                            self.ui.tecnologia.setChecked(True)
                else:
                    QMessageBox.information(self, "Registro", "No hay leaderteacher con esa identificacion")
                    self.ui.btRegistrar.setEnabled(False)

        except Exception:
            QMessageBox.information(self, "Registro", "Error interno, campos faltantes del leaderteacher o aspirante")




#_____________________________________________________________________________#

    def inscribir_clicked(self):
        parametros=[]
        print("Capturando Informacion...")
        #id=str(self.ui.txtid.text())
        id=self.cedula

        ###DATOS DE USUARIO
        unombre=str(self.ui.txtnombre.text())
        uapellido=str(self.ui.txtapellido.text())
        utelefono=str(self.ui.txttelefono.text())
        udireccion=str(self.ui.txtdireccion.text())
        ucorreo=str(self.ui.txtcorreo.text())
        ucalendario=str(QDate.toPyDate(self.ui.calendario.selectedDate()))
        password=str(self.ui.txtpassword.text())

        umunicipio=str(self.ui.txtmunicipio.text())
        uinstitucion=str(self.ui.txtinstitucion.text())
        uescalafon=str(self.ui.txtescalafon.text())
        usede=str(self.ui.txtsede.text())
        udane=str(self.ui.txtdane.text())
        usecretaria=str(self.ui.txtsecretaria.currentText())

        #VALIDACION CAMPOS TEXTO VACIOS
        if(self.tipo==2):
            if(unombre=="" or uapellido=="" or utelefono=="" or udireccion=="" or ucorreo =="" or ucalendario=="" or password==""
               or umunicipio=="" or uinstitucion=="" or uescalafon=="" or usede=="" or udane=="" or usecretaria==""):
                self.flag=True
                self.obligatorios=self.obligatorios+"Campos de Texto"

        if(self.tipo==1):
            if(unombre=="" or uapellido=="" or password==""):
                self.flag=True
                self.obligatorios=self.obligatorios+"Campos de Texto"

        if(self.ui.col_aprendeSi.isChecked()):
            uusuario_col_aprende=True
        else:
            uusuario_col_aprende=False
        if(self.ui.tutorSi.isChecked()):
            ututor=True
        else:
            ututor=False
        ugenero=""
        if(self.ui.femenino.isChecked()):
            ugenero="Femenino"
        else:
            ugenero="Masculino"

        ###1 De 8
        Zonas=[]
        Modalidad="Academica"
        if (self.ui.zonaurbana.isChecked()):
            Zonas.append("Zona urbana")
        if (self.ui.zonaurbanamarginada.isChecked()):
            Zonas.append("Zona urbana marginada")
        if (self.ui.zonarural.isChecked()):
            Zonas.append("Zona rural")
        if (self.ui.zonaruraldificil.isChecked()):
            Zonas.append("Zona rural dificil acceso")
        #print(Zonas)
        if (self.ui.modalacademica.isChecked()):
            Modalidad="Academica"
        elif(self.ui.modaltecnica.isChecked()):
            Modalidad="Tecnica"
        #print(Modalidad)

        if(len(Zonas)==0):
            self.flag=True
            self.obligatorios=self.obligatorios+", Zonas"

        ### 2 de 8
        ModalidadTec=[]
        if (self.ui.agro.isChecked()):
            ModalidadTec.append("Agropecuario")
        if (self.ui.comercial.isChecked()):
            ModalidadTec.append("Comercial")
        if (self.ui.promocionSocial.isChecked()):
            ModalidadTec.append("Promocion Social")
        if (self.ui.finanzas.isChecked()):
            ModalidadTec.append("Finanzas")
        if (self.ui.administracion.isChecked()):
            ModalidadTec.append("Administracion")
        if (self.ui.ecologia.isChecked()):
            ModalidadTec.append("Ecologia")
        if (self.ui.medioambiente.isChecked()):
            ModalidadTec.append("Medio Ambiente")
        if (self.ui.industrial.isChecked()):
            ModalidadTec.append("Industrial")
        if (self.ui.informatica.isChecked()):
            ModalidadTec.append("Informatica")
        if (self.ui.mineria.isChecked()):
            ModalidadTec.append("Mineria")
        if (self.ui.salud.isChecked()):
            ModalidadTec.append("Salud")
        if (self.ui.recreacion.isChecked()):
            ModalidadTec.append("Recreacion")
        if (self.ui.turismo.isChecked()):
            ModalidadTec.append("Turismo")
        if (self.ui.deporte.isChecked()):
            ModalidadTec.append("Deporte")
        if (self.ui.otromodalidad.isChecked()):
            otram=str(self.ui.txtotromodalidad.text())
            if(otram==""):
                self.flag=True
                self.obligatorios=self.obligatorios+", Otra Modalidad: vacia"
            else:
                ModalidadTec.append(otram)

        if(len(Modalidad)==0):
            self.flag=True
            self.obligatorios=self.obligatorios+", Modalidad"
        #print(ModalidadTec)
        ### 3 de 8
        etnoeducativa=[]
        if (self.ui.afro.isChecked()):
            etnoeducativa.append("Etnia Afrocolombiana")
        if (self.ui.indigena.isChecked()):
            etnoeducativa.append("Etnia Indigena")
        if (self.ui.rom.isChecked()):
            etnoeducativa.append("Etnia Rom")
        if (self.ui.ningunaetnia.isChecked()):
            etnoeducativa=[]
            etnoeducativa.append("Ninguna Etnia")

        if(len(etnoeducativa)==0):
            self.flag=True
            self.obligatorios=self.obligatorios+", Clasificacion etnoeducativa"
        #print(etnoeducativa)
        niveles=[]
        if (self.ui.transicion.isChecked()):
            niveles.append("Transicion")
        if (self.ui.eduinicial.isChecked()):
            niveles.append("Educacion Inicial")
        if (self.ui.eduprimaria.isChecked()):
            niveles.append("Educacion Primaria")
        if (self.ui.edusecundaria.isChecked()):
            niveles.append("Educacion Secundaria")
        if (self.ui.edumedia.isChecked()):
            niveles.append("Educacion Media")
        if (self.ui.edusuperior.isChecked()):
            niveles.append("Educacion Superior")
        if (self.ui.otronivel.isChecked()):
            otronivel=str(self.ui.txtotronivel.text())
            if(otronivel==""):
                self.flag=True
                self.obligatorios=self.obligatorios+", Otro Nivel escolar:Vacio"
            else:
                niveles.append(otronivel)

        if(len(niveles)==0):
            self.flag=True
            self.obligatorios=self.obligatorios+", Nivel escolar"

        #print(niveles)
        ###4 de 8
        grados=[]
        if (self.ui.gtransicion.isChecked()):
            grados.append("Grado Transicion")
        if (self.ui.ginicial.isChecked()):
            grados.append("Grado Inicial")
        if (self.ui.g1.isChecked()):
            grados.append("Grado 1")
        if (self.ui.g2.isChecked()):
            grados.append("Grado 2")
        if (self.ui.g3.isChecked()):
            grados.append("Grado 3")
        if (self.ui.g4.isChecked()):
            grados.append("Grado 4")
        if (self.ui.g5.isChecked()):
            grados.append("Grado 5")
        if (self.ui.g6.isChecked()):
            grados.append("Grado 6")
        if (self.ui.g7.isChecked()):
            grados.append("Grado 7")
        if (self.ui.g8.isChecked()):
            grados.append("Grado 8")
        if (self.ui.g9.isChecked()):
            grados.append("Grado 9")
        if (self.ui.g10.isChecked()):
            grados.append("Grado 10")
        if (self.ui.g11.isChecked()):
            grados.append("Grado 11")
        if (self.ui.gotro.isChecked()):
            otrogrado=str(self.ui.txtotrogrado.text())
            if(otrogrado==""):
                self.flag=True
                self.obligatorios=self.obligatorios+", Otros Grados: Vacio"
            else:
                grados.append(otrogrado)

        if(len(grados)==0):
            self.flag=True
            self.obligatorios=self.obligatorios+", Grados"
        #print(grados)

        ### 5 de 8
        areas=[]
        if (self.ui.naturales.isChecked()):
            areas.append("Ciencias Naturales y Educacion Ambiental")
        if (self.ui.sociales.isChecked()):
            areas.append("Ciencias Sociales")
        if (self.ui.artistica.isChecked()):
            areas.append("Artistica")
        if (self.ui.etica.isChecked()):
            areas.append("Etica y Valores Humanos")
        if (self.ui.fisica.isChecked()):
            areas.append("Fisica Recreacion y Deportes")
        if (self.ui.religiosa.isChecked()):
            areas.append("Edicacion Religiosa")
        if (self.ui.humanidades.isChecked()):
            areas.append("Humanidades Lengua Castellana e Idioma Extranjero")
        if (self.ui.matematicas.isChecked()):
            areas.append("Matematicas")
        if (self.ui.tecnologia.isChecked()):
            areas.append("Tecnologia")

        if(len(areas)==0):
            self.flag=True
            self.obligatorios=self.obligatorios+", Areas"
        #print(areas)

        ### 6 de 8
        nivel_educacion=""
        if (self.ui.niveltecnico.isChecked()):
            nivel_educacion="Nivel Tecnico"
        if (self.ui.niveltecnologico.isChecked()):
            nivel_educacion="Nivel Tecnologico"
        if (self.ui.nivelprofesional.isChecked()):
            nivel_educacion="Nivel Profesional"
        if (self.ui.nivelnormalista.isChecked()):
            nivel_educacion="Nivel Normalista Superior"
        if (self.ui.nivellicenciatura.isChecked()):
            nivel_educacion="Nivel Licenciatura"
        if (self.ui.nivelespecializaciones.isChecked()):
            nivel_educacion="Nivel Especializaciones"
        if (self.ui.nivelmaestria.isChecked()):
            nivel_educacion="Nivel Maestria"
        if (self.ui.niveldoctorado.isChecked()):
            nivel_educacion="Nivel Doctorado"
        #print(nivel_educacion)


        ## 7 de 8
        exp_preescolar=int(self.ui.exppreescolar.value())
        #print(exp_preescolar)
        exp_primaria=int(self.ui.expprimaria.value())
        #print(exp_primaria)
        exp_secundaria=int(self.ui.expsecundaria.value())
        #print(exp_secundaria)
        exp_media=int(self.ui.expmedia.value())
        #print(exp_media)
        exp_superior=int(self.ui.expsuperior.value())
        #print(exp_superior)
        ## 8 de 8
        exp_rural=int(self.ui.exprural.value())
        #print(exp_rural)
        exp_urbana=int(self.ui.expurbana.value())
        #print(exp_urbana)
        exp_publico=int(self.ui.exppublico.value())
        #print(exp_publico)
        exp_privado=int(self.ui.expprivado.value())
        #print(exp_privado)
        exp_total=int(self.ui.exptotal.value())
        #print(exp_total)



        #Consultamos aspirante para almacenar los datos

        asp=self.controldigi.consultarAspirante(id)

        if(self.tipo==1):
            parametros.append(id)
            parametros.append(asp.nombres)
            parametros.append(asp.apellidos)
            parametros.append(asp.direccion)
            parametros.append(asp.telefono)
            parametros.append(asp.correo_electronico)
            parametros.append(asp.fecha_nacimiento)
            parametros.append(password)
        if(self.tipo==2):
            parametros.append(id)
            parametros.append(unombre)
            parametros.append(uapellido)
            parametros.append(udireccion)
            parametros.append(utelefono)
            parametros.append(ucorreo)
            parametros.append(ucalendario)
            parametros.append(password)

        #DATOS PARA LT
        if(self.tipo==1):
            parametros.append(asp.municipio)
            parametros.append(asp.genero)
            parametros.append(asp.institucion)
            parametros.append(asp.escalafon)
            parametros.append(asp.sede)
            parametros.append(asp.codigo_dane)
            parametros.append(asp.dpto_secretaria)
            parametros.append(asp.tutor)
            parametros.append(asp.usuario_col_aprende)
        if(self.tipo==2):
            parametros.append(umunicipio)
            parametros.append(ugenero)
            parametros.append(uinstitucion)
            parametros.append(uescalafon)
            parametros.append(usede)
            parametros.append(udane)
            parametros.append(usecretaria)
            parametros.append(ututor)
            parametros.append(uusuario_col_aprende)

        parametros.append(Modalidad)
        parametros.append(exp_preescolar)
        parametros.append(exp_primaria)
        parametros.append(exp_secundaria)
        parametros.append(exp_media)
        parametros.append(exp_superior)
        parametros.append(exp_rural)
        parametros.append(exp_urbana)
        parametros.append(exp_publico)
        parametros.append(exp_privado)
        parametros.append(exp_total)
        parametros.append(areas)
        parametros.append(Zonas)
        parametros.append(ModalidadTec)
        parametros.append(grados)
        parametros.append(etnoeducativa)
        parametros.append(niveles)
        parametros.append(nivel_educacion)




        # creamos el LT Si esta en modo Crear
        if(self.tipo==1):
            if (self.flag==True):
                QMessageBox.information(self, "Registro", "Recuerde que todos los campos son obligatorios, asegurece de que\n"
                                                          "que no haya campos vacios y seleccionar al menos una opcion de:\n"+
                                        self.obligatorios)
                self.obligatorios=""
                self.flag=False
            elif(self.validarcontrasena(password)==len(password) or len(password)<6):
                QMessageBox.information(self, "Registro", "El Password debe contener por lo menos seis caracteres y un numero")

            else:
                msj=self.controldigi.agregarLT(3,parametros)
                if( msj != "Exito"):
                    QMessageBox.information(self, "Registro", "Error al momento de registrar leaderteacher\n"+msj)
                else:
                    QMessageBox.information(self, "Registro", "Registro de leaderteacher Exitoso!")
                    self.controldigi.cerrarSesion()


        #Editamos LT
        if(self.tipo==2):

            if (self.flag==True):
                QMessageBox.information(self, "Registro", "Recuerde que todos los campos son obligatorios, asegurece de que\n"
                                                          "que no haya campos vacios y seleccionar al menos una opcion de:\n"+
                                        self.obligatorios)
                self.obligatorios=""
                self.flag=False
            elif (self.validacion() != 1):
                if (self.buscaCaracter("@", ucorreo) == True):
                    QMessageBox.information(self, "Registro", "Correo debe contener un punto despues del arroba")
                elif (self.buscaCaracter(".", ucorreo) == True):
                    QMessageBox.information(self, "Registro", "Correo debe contener un arroba antes del punto")
                else:
                    QMessageBox.information(self, "Registro", "Correo debe contener un @ y luego un punto")

            elif(self.validarcontrasena(password)==len(password) or len(password)<6):
                QMessageBox.information(self, "Registro", "El Password debe contener por lo menos seis caracteres y un numero")

            else:
                mensaje="Editar Leader Teacher con cedula:"+self.cedula
                if (QMessageBox.Yes == QMessageBox(QMessageBox.Information, "Confirmar", mensaje, QMessageBox.Yes|QMessageBox.No).exec_()):
                    print("SI... enviando a edicion...")
                    #self.controldigi.editarUsuarioLT(self.cedula,editparams)
                    editmsj=self.controldigi.editarLT(self.cedula,parametros)
                    if(editmsj != "Exito"):
                        QtGui.QMessageBox.warning(self, self.tr("Error en Base de Datos"),
                                      QString.fromUtf8("Error al momento de editar leaderteacher\n"+editmsj))

                    else:
                        QMessageBox.information(self, "Registro", "Actualizacion de leaderteacher Exitoso!")
                        self.controldigi.cerrarSesion()
                else:
                    print("No...")