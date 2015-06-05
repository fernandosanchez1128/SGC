from PyQt4 import uic, QtCore,QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Singleton import Singleton

from CrearCurso import CrearCurso
from AsignarMT import AsignarMT
from Asignacion_cohortes import AsignacionCohortes
from NotasEstudiante import NotasEstudiante
from Control.ControlCoordinador import ControlCoordinador
from EstudiantesAprob import EstudiantesAprob
from EstudiantesDpto import EstudiantesDpto
from PorcentajeAprob import PorcentajeAprob
from PorcentajesReprob import PorcentajesReprob
from VistaDescargarCertificado import VistaDescargarCertificado
from Top10 import *
from datetime import date
import math

( Ui_VistaCoordinador, QMainWindow ) = uic.loadUiType( 'vistacoordinador.ui' )


@Singleton
class VistaCoordinador ( QMainWindow ):
    """VistaCoordinador inherits QMainWindow"""

    def __init__ ( self, parent = None ):
        QMainWindow.__init__( self, parent )
        self.ui = Ui_VistaCoordinador()
        self.ui.setupUi( self )
        self.control  = ControlCoordinador()

        self.connect(self.ui.btCrear, SIGNAL("clicked()"), self.crear_clicked)
        self.connect(self.ui.btConsultar, SIGNAL("clicked()"), self.consultar_clicked)
        self.connect(self.ui.btEditar, SIGNAL("clicked()"), self.editar_clicked)
       # self.connect(self.ui.btEliminar, SIGNAL("clicked()"), self.eliminar_clicked)
        self.connect(self.ui.btMatricular, SIGNAL("clicked()"), self.matricular_clicked)
        self.connect(self.ui.btAsignar, SIGNAL("clicked()"), self.asignar_clicked)
        self.connect(self.ui.btAsignarFecha, SIGNAL("clicked()"), self.asignarFecha_clicked)
        self.connect(self.ui.btCursosAsistentes, SIGNAL("clicked()"), self.curso_asistentes)
        self.connect(self.ui.btLTDpto, SIGNAL("clicked()"), self.ltxdpto)
        self.connect(self.ui.btCursosAvance, SIGNAL("clicked()"), self.cursosAvance_clicked)
        self.connect(self.ui.btNotasLT, SIGNAL("clicked()"), self.notasLT_clicked)
        self.connect(self.ui.btLTReprobaron, SIGNAL("clicked()"), self.lt_reprobaron_clicked)
        self.connect(self.ui.btLTAprobaron, SIGNAL("clicked()"), self.lt_aprobaron_clicked)
        self.connect(self.ui.btLTCurso, SIGNAL("clicked()"), self.aprob_clicked)
        self.connect(self.ui.btHistoricoDpto, SIGNAL("clicked()"), self.hist_dpto_clicked)
        self.connect(self.ui.btCertificado, SIGNAL("clicked()"), self.certificado_clicked)


    def __del__ ( self ):
        self.ui = None

    def crear_clicked(self):
        venCrear =  CrearCurso(None, 1).exec_()

    def consultar_clicked(self):
        venConsultar =  CrearCurso(None,2).exec_()

    def editar_clicked(self):
        venConsultar =  CrearCurso(None,3).exec_()

    def eliminar_clicked(self):
		venEliminar =  CrearCurso(None,4).exec_()

    def matricular_clicked(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file','', ("Text files (*.txt)" ))
        if fname:
            try:
                ano = date.today().year
                semestre  = math.ceil(float(date.today().month)/6)
                resultado = self.control.procesarMatriculados(fname, ano, semestre)
                if resultado==2:
                    QtGui.QMessageBox.warning(self, 'Error',"No se ha logrado matricular\nPuede ser por el formato del archivo\nPor favor, comunicarse con el remitente del archivo.", QtGui.QMessageBox.Ok)
                elif resultado=='':
                    QtGui.QMessageBox.information(self, 'Exito',"Se han matriculado todos los estudiantes con exito.", QtGui.QMessageBox.Ok)
                else:
                    QtGui.QMessageBox.warning(self, 'Error',"No se ha logrado matricular los siguientes estudiantes:", QtGui.QMessageBox.Ok)
            except :
                QtGui.QMessageBox.warning(self, 'Error',"Ha ocurrido un error en la base de datos.\nPor favor, vuelva a intentarlo.", QtGui.QMessageBox.Ok)
        else:
            QtGui.QMessageBox.warning(self, 'Error',"Por favor seleccione el archivo de los matriculados.", QtGui.QMessageBox.Ok)

    def asignar_clicked(self):
        venAs = AsignarMT().exec_()

    def asignarFecha_clicked(self):
        v = AsignacionCohortes().exec_()

    #REPORTES
    def cursosAvance_clicked (self):
        fecha_act = date.today()
        ruta = QFileDialog.getSaveFileName(self, 'Guardar Reporte', '', selectedFilter='*.svg')
        if ruta:
            if ruta[-4:]!='.svg':
                ruta=ruta+'.svg'
            exito =self.control.cursos_menos_avance(fecha_act, str (ruta))
            if exito == 0 :
                QtGui.QMessageBox.warning(self, 'Error',"no se encontraron datos para generar reporte", QtGui.QMessageBox.Ok)
        else :
            QtGui.QMessageBox.warning(self, 'Error',"por favor seleccione un destino", QtGui.QMessageBox.Ok)

    def notasLT_clicked(self):
        ne = NotasEstudiante().exec_()

    def curso_asistentes(self):
        self.r1=Top10(None,1)
        self.r1.show()

    def ltxdpto(self):
        self.r1=Top10(None,2)
        self.r1.show()

    def aprob_clicked(self):
        w=EstudiantesAprob().exec_()

    def hist_dpto_clicked(self):
        w=EstudiantesDpto().exec_()

    def lt_reprobaron_clicked(self):
        v = PorcentajesReprob().exec_()

    def lt_aprobaron_clicked(self):
        v = PorcentajeAprob().exec_()

    def certificado_clicked(self):
        v= VistaDescargarCertificado().exec_()
