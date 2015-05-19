import sys

# import PyQt4 QtCore and QtGui modules
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from VistaLogin import *
from VistaDescargarCertificado import *


from CrearAspirante import CrearAspirante
from RegistrarLT import RegistrarLT
from CrearPreinscripcion import CrearPreinscripcion

if __name__ == '__main__':
    # create application
    app = QApplication( sys.argv )
    app.setApplicationName( 'My PyQt4 QtGui Project')
    '''
    venCrear =  VistaLogin()
    venCrear.show()
    '''
    venCrear=VistaDescargarCertificado()
    venCrear.show()

    # connection
    QObject.connect( app, SIGNAL( 'lastWindowClosed()' ), app, SLOT( 'quit()' ) )

    # execute application
    sys.exit( app.exec_() )
