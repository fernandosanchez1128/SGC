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
        id=str(self.ui.txtid.text())
        nombres="recuperar con consulta"
        self.ui.txtnombre.setText(nombres)
        apellidos="recuperar con consulta"
        self.ui.txtapellido.setText(apellidos)
        ###1 De 8
        Zonas=[]
        Modalidad=[]
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
            ModalidadTec.append(otram)
        print(ModalidadTec)
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

        print(etnoeducativa)
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
            niveles.append(otronivel)
        print(niveles)
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
            grados.append(otrogrado)
        print(grados)

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
        print(areas)

        ### 6 de 8
        nivel_educacion=[]
        if (self.ui.niveltecnico.isChecked()):
            nivel_educacion.append("Nivel Tecnico")
        if (self.ui.niveltecnologico.isChecked()):
            nivel_educacion.append("Nivel Tecnologico")
        if (self.ui.nivelprofesional.isChecked()):
            nivel_educacion.append("Nivel Profesional")
        if (self.ui.nivelnormalista.isChecked()):
            nivel_educacion.append("Nivel Normalista Superior")
        if (self.ui.nivellicenciatura.isChecked()):
            nivel_educacion.append("Nivel Licenciatura")
        if (self.ui.nivelespecializaciones.isChecked()):
            nivel_educacion.append("Nivel Especializaciones")
        if (self.ui.nivelmaestria.isChecked()):
            nivel_educacion.append("Nivel Maestria")
        if (self.ui.niveldoctorado.isChecked()):
            nivel_educacion.append("Nivel Doctorado")
        print(nivel_educacion)

        ## 7 de 8
        exp_preescolar=int(self.ui.exppreescolar.value())
        print(exp_preescolar)
        exp_primaria=int(self.ui.expprimaria.value())
        print(exp_primaria)
        exp_secundaria=int(self.ui.expsecundaria.value())
        print(exp_secundaria)
        exp_media=int(self.ui.expmedia.value())
        print(exp_media)
        exp_superior=int(self.ui.expsuperior.value())
        print(exp_superior)
        ## 8 de 8
        exp_rural=int(self.ui.exprural.value())
        print(exp_rural)
        exp_urbana=int(self.ui.expurbana.value())
        print(exp_urbana)
        exp_publico=int(self.ui.exppublico.value())
        print(exp_publico)
        exp_privado=int(self.ui.expprivado.value())
        print(exp_privado)
        exp_total=int(self.ui.exptotal.value())
        print(exp_total)

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