import unittest

def decimal_to_roman(decimal):
    total = ""
    if decimal >= 100:
        centena = decimal // 100
        total = "C" * centena 
        decimal = decimal % 100
    if decimal <= 3:
        total += "I" * decimal 
    elif decimal == 5:
        total += "V" * decimal 
    elif decimal == 10:
        total += "X"
    return total 

class TestDecimalToRoman (unittest.TestCase):
    def test_uno (self):
        resultado = decimal_to_roman (1)
        self.assertEqual (resultado, "I")
    
    def test_diez (self):
        resultado = decimal_to_roman (10)
        self.assertEqual (resultado, "X")

    def test_cinco (self):
        resultado = decimal_to_roman (5)
        self.assertEqual (resultado, "V")

if __name__ == "__main__":
    unittest.main()

    
