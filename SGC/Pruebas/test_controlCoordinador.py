from unittest import TestCase
from Control.ControlCoordinador import ControlCoordinador
from ORM.Curso import Curso
__author__ = 'family'


class TestControlCoordinador(TestCase):
    def test_crearCurso(self):
        self.fail()
    def test_Raiz(self):

        #Test para la raiz de nueve que devuelve 3 que debe pasar.
        self.assertEqual((0.0, -0.5), self.s.demo(2, 1, 0))

    def test_negative(self):

        #Test para la raiz de un numeo negativo, que debe fallar.

        # Este debe devolver un Exception, pero se espera un Exception.

        with self.assertRaises(ZeroDivisionError):
            self.s.demo(0,1,8)
