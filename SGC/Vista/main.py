import sys

# import PyQt4 QtCore and QtGui modules
from PyQt4.QtCore import *
from PyQt4.QtGui import *




if __name__ == '__main__':
    app = QApplication( sys.argv )
    app.setApplicationName( 'My PyQt4 QtGui Project')
    try:
        # create application
        from VistaLogin import VistaLogin
    except Exception as e:
        QMessageBox.information(None, "Error", "Hay un problema en la conexion a la base de datos")
        print str(e)
        exit()

    w = VistaLogin()
    w.show()

    # connection
    QObject.connect( app, SIGNAL( 'lastWindowClosed()' ), app, SLOT( 'quit()' ) )

    # execute application
    sys.exit( app.exec_() )


