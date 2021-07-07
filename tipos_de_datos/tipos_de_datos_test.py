import unittest
import random

from tipos_de_datos import TiposDeDatos

class TestTiposDeDatos(unittest.TestCase):

    def setUp(self):
        self.tipos_de_datos = TiposDeDatos()

    def test_es_string(self):
        self.assertTrue(
            self.tipos_de_datos.es_string("Hola mundo")
        )
        falsos = [1, 1.0, [], True, False, b""]
        for f in falsos:
            self.assertFalse(
                self.tipos_de_datos.es_string(f)
            )

    def test_es_boolean(self):
        self.assertTrue(
            self.tipos_de_datos.es_boolean(True)
        )
        self.assertTrue(
            self.tipos_de_datos.es_boolean(False)
        )
        falsos = [1, 1.0, [], "Hola mundo", b""]
        for f in falsos:
            self.assertFalse(
                self.tipos_de_datos.es_boolean(f)
            )

    def test_es_int(self):
        for i in range(10):
            self.assertTrue(
                self.tipos_de_datos.es_int(i)
            )
        falsos = ["Hola mundo", 1.0, [], True, False, b""]
        for f in falsos:
            self.assertFalse(
                self.tipos_de_datos.es_int(f)
            )

    def test_es_float(self):
        self.assertTrue(
            self.tipos_de_datos.es_float(1.0)
        )
        self.assertTrue(
            self.tipos_de_datos.es_float(2.0)
        )
        falsos = [1, [], True, False, b""]
        for f in falsos:
            self.assertFalse(
                self.tipos_de_datos.es_float(f)
            )

    def test_es_byte(self):
        self.assertTrue(
            self.tipos_de_datos.es_byte(b"")
        )
        falsos = [1, 1.0, [], True, False, "Hola mundo"]
        for f in falsos:
            self.assertFalse(
                self.tipos_de_datos.es_byte(f)
            )

    def test_es_list(self):
        self.assertTrue(
            self.tipos_de_datos.es_list([])
        )
        falsos = [1, 1.0, True, False, "Hola mundo"]
        for f in falsos:
            self.assertFalse(
                self.tipos_de_datos.es_list(f)
            )
        
    def test_regresa_un_string(self):
        self.assertTrue(
            self.tipos_de_datos.es_string(
                self.tipos_de_datos.regresa_un_string()
            )
        )

    def test_regresa_un_boolean(self):
        self.assertTrue(
            self.tipos_de_datos.es_boolean(
                self.tipos_de_datos.regresa_un_boolean()
            )
        )

    def test_regresa_un_int(self):
        self.assertTrue(
            self.tipos_de_datos.es_int(
                self.tipos_de_datos.regresa_un_int()
            )
        )

    def test_regresa_un_float(self):
        self.assertTrue(
            self.tipos_de_datos.es_float(
                self.tipos_de_datos.regresa_un_float()
            )
        )

    def test_regresa_un_byte(self):
        self.assertTrue(
            self.tipos_de_datos.es_byte(
                self.tipos_de_datos.regresa_un_byte()
            )
        )

    def test_regresa_una_lista(self):
        self.assertTrue(
            self.tipos_de_datos.es_list(
                self.tipos_de_datos.regresa_una_lista()
            )
        )

    def regresa_una_lista_de_longitud_10(self):
        self.assertTrue(
            self.tipos_de_datos.es_lista(
                self.tipos_de_datos.regresa_una_lista_de_longitud_10()
            )
        )
        self.assertTrue(
            len(
                self.tipos_de_datos.regresa_una_lista_de_longitud_10()
            ) == 10
        )

    def test_to_string(self):
        for t in [1, 1.0, "Hola mundo", True, False]:
            self.assertTrue(
                self.tipos_de_datos.es_string(
                    self.tipos_de_datos.to_string(
                        t
                    )
                )
            )

    def test_int_to_float(self):
        r = random.randint(-100, 100)
        self.assertEqual(
            float(r), 
            self.tipos_de_datos.int_to_float(r)
        )

    def test_float_to_int(self):
        r = random.randint(-100, 100)
        r_f = random.randint(1, 100) / 100
        self.assertEqual(
            int(r + r_f), 
            self.tipos_de_datos.float_to_int(r + r_f)
        )

if __name__ == '__main__':
    unittest.main()
