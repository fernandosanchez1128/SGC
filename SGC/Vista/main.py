import sys

# import PyQt4 QtCore and QtGui modules
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import webbrowser

#from VistaMt import MainWindow
from RegistrarLT import RegistrarLT
from CrearAspirante import CrearAspirante
from VistaDigitador import VistaDigitador
from vistacoordinador import *
from Top10 import *
from VistaLogin import VistaLogin

if __name__ == '__main__':
    # create application
    app = QApplication( sys.argv )
    app.setApplicationName( 'My PyQt4 QtGui Project')
    #w = RegistrarLT()
    #w = CrearAspirante()
    #w=VistaDigitador()
    w=VistaLogin()
    #w=Top10()
    #w=VistaCoordinador.Instance()
    w.show()
    #new = 2
    #url = "file:///home/nelson/Documentos/Git/SGC/SGC/Vista/test.html"
    #webbrowser.open(url,new=new)

    # connection
    QObject.connect( app, SIGNAL( 'lastWindowClosed()' ), app, SLOT( 'quit()' ) )
    # execute application
    sys.exit( app.exec_() )
