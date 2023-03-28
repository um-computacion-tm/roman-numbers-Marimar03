import unittest

def roman_to_decimal(roman):
    total = 0
    for letter in roman:
        if letter == "I":
        elif letter == "V":
            if total > 0:
                total = -1
            total += 5
        elif letter == 

class Testromantodecimal (unittest.TestCase):
    def test_uno(self):
        resultado = roman_to_decimal("I")
        self.assertEqual(resultado, "1")
    def test_dos(self):
        resultado = roman_to_decimal("II")
        self.assertEqual(resultado, "2")
    def test_tres(self):
        resultado = roman_to_decimal("III")
        self.assertEqual(resultado, "3")

if __name__==  "__main__":
    unittest.main()
