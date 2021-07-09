import unittest
import random

from if_statement import (
    Ropa, 
    Semaforo,
    Pastel,
    Futbol
)

class TestRopa(unittest.TestCase):

    def setUp(self):
        self.ropa = Ropa()

    def test_tender(self):
        self.assertEqual(
            "no tiendo", self.ropa.tender("lluvia")
        )
        self.assertEqual(
            "tiendo", self.ropa.tender("sol")
        )

    def test_tender_con_negacion(self):
        self.assertEqual(
            "no tiendo", self.ropa.tender_con_negacion("lluvia")
        )
        self.assertEqual(
            "tiendo", self.ropa.tender_con_negacion("sol")
        )

class TestSemaforo(unittest.TestCase):
    def setUp(self):
        self.semaforo = Semaforo()

    def test_avanza(self):
        self.assertEqual(
            "avanza", self.semaforo.avanza("verde")
        )
        self.assertEqual(
            "no avanza", self.semaforo.avanza("rojo")
        )
        self.assertEqual(
            "no avanza", self.semaforo.avanza("amarillo")
        )

class TestPastel(unittest.TestCase):
    def setUp(self):
        self.pastel = Pastel()

    def test_suficiente(self):
        self.assertEqual(
            "suficiente", self.pastel.suficiente(100, 90)
        )
        self.assertEqual(
            "suficiente", self.pastel.suficiente(100, 100)
        )
        self.assertEqual(
            "insuficiente", self.pastel.suficiente(90, 100)
        )

    def test_diferencia(self):
        cr = 100
        cb = 90
        self.assertEqual(
            abs(cr - cb), self.pastel.diferencia(cr, cb)
        )

    def test_es_de_chocolate(self):
        self.assertEqual(
            "si", self.pastel.es_de_chocolate("chocolate")
        )
        self.assertEqual(
            "no", self.pastel.es_de_chocolate("vainilla")
        )

class TestFutbol(unittest.TestCase):
    def setUp(self):
        self.futbol = Futbol()

    def test_equipo_valido(self):
        self.assertEqual(
            "valido", self.futbol.equipo_valido(11)
        )
        self.assertEqual(
            "no valido", self.futbol.equipo_valido(8)
        )



if __name__ == '__main__':
    unittest.main()
