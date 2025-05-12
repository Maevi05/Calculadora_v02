import unittest
from Calculadora import calcular_valor


class TestCalculadora(unittest.TestCase):
    def test_soma1(self):
        self.assertEqual(calcular_valor(3, 5, '+'), 8)

    def test_soma2(self):
        self.assertEqual(calcular_valor(9, 7, '+'), 16)

    def test_soma3(self):
        self.assertEqual(calcular_valor(14878, 521054, '+'), 535932)

    def test_subtracao1(self):
        self.assertEqual(calcular_valor(10, 4, '-'), 6)

    def test_subtracao2(self):
        self.assertEqual(calcular_valor(50, 10, '-'), 40)

    def test_subtracao3(self):
        self.assertEqual(calcular_valor(85441, 34100, '-'), 51341)

    def test_multiplicacao1(self):
        self.assertEqual(calcular_valor(2, 3, '*'), 6)

    def test_multiplicacao2(self):
        self.assertEqual(calcular_valor(12, 12, '*'), 144)

    def test_multiplicacao3(self):
        self.assertEqual(calcular_valor(81, 175, '*'), 14175)

    def test_divisao1(self):
        self.assertEqual(calcular_valor(10, 2, '/'), 5)

    def test_divisao2(self):
        self.assertEqual(calcular_valor(90, 3, '/'), 30)

    def test_divisao3(self):
        self.assertEqual(calcular_valor(810, 5, '/'), 162)

    def test_potenciacao1(self):
        self.assertEqual(calcular_valor(2, 3, '^'), 8)

    def test_potenciacao2(self):
        self.assertEqual(calcular_valor(3, 5, '^'), 243)

    def test_potenciacao3(self):
        self.assertEqual(calcular_valor(6, 5, '^'), 7776)

    def test_divisao_por_zero1(self):
        with self.assertRaises(ZeroDivisionError):
            calcular_valor(15, 0, '/')

    def test_divisao_por_zero2(self):
        with self.assertRaises(ZeroDivisionError):
            calcular_valor(0, 0, '/')

    def test_operacao_invalida1(self):
        with self.assertRaises(ValueError):
            calcular_valor(5, 5, '%')

    def test_operacao_invalida2(self):
        with self.assertRaises(ValueError):
            calcular_valor(1, 6, '&')

    def test_valor_invalido2(self):
        with self.assertRaises(ValueError):
            calcular_valor("abc", 5, '+')

    def test_valor_invalido1(self):
        with self.assertRaises(ValueError):
            calcular_valor("dsadsada", 15, '/')


if __name__ == '__main__':
    unittest.main()