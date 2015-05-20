from unittest import TestCase
from Control.FachadaMt import FachadaMt
from sqlalchemy.exc import *
__author__ = 'braymrr'


class TestFachadaMt(TestCase):

    def __init__(self):
        self.fach = FachadaMt()

    def test_agregar_entrega_uno(self):
        self.assertEqual((0.0, -0.5), self.fach.agregar_entrega(2, 1, 0))


    def test_agregar_entrega_dos(self):
        self.assertEqual((0.0, -0.5), self.fach.agregar_entrega(2, 1, 0))

    def test_negative_uno(self):
        with self.assertRaises(IntegrityError):
            self.fach.agregar_entrega(0,1,8)

    def test_negative_dos(self):
        with self.assertRaises(NoReferenceError):
            self.s.agregar_entrega(0,1,8)