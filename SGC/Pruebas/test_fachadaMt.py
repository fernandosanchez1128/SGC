from unittest import TestCase
from Control.FachadaMt import FachadaMt
__author__ = 'braymrr'


class TestFachadaMt(TestCase):

    fach = FachadaMt()

    #TODAS ESTAS PRUEBAS SE HACEN SUPONIENDO QUE EXISTE UN CURSO CON ID=1, UN COHORTE DE ESTE CURSO CON I=1 Y UNA ACTIVIDAD DE ESTE CURSO CON ID=1, NO MAS
    #editar
    def test_agregar_entrega_uno(self):
        self.assertEqual(2, self.fach.agregar_entrega(1, 1, 1, '2015/09/15:12:30'))

    #agregar
    def test_agregar_entrega_dos(self):
        self.assertEqual(1, self.fach.agregar_entrega(1, 1, 1, '2018/09/15:12:30'))

    #cohorte inexistente
    def test_negative_uno(self):
        self.assertEqual(3, self.fach.agregar_entrega(1, 8, 1, '2015/09/15:12:30'))

    #ERROR EN EL TIPO DE DATO
    def test_negative_dos(self):
        self.assertEqual(4, self.fach.agregar_entrega('A', 1, 1, '2015/09/15:12:30'))


# from unittest import main
# if __name__ == "__main__":
#     main()





