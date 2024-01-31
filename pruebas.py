import unittest
import libreria_complejos
import math

class TestLibComplex(unittest.TestCase):
    n1, n2= ((-3,2),(5,-8))
    n3, n4 = ((2.5,-9), (4,1))
    n5, n6 = ((5.25, 8), (6.8,2))

    def test_suma(self):
        prueba_1 = libreria_complejos.suma(self.n1, self.n2)
        self.assertAlmostEqual(prueba_1[0], 2)
        self.assertAlmostEqual(prueba_1[1],-6)
        prueba_2 = libreria_complejos.suma(self.n3, self.n4)
        self.assertAlmostEqual(prueba_2[0], 6.5)
        self.assertAlmostEqual(prueba_2[1],-8)
        prueba_3 = libreria_complejos.suma(self.n5, self.n6)
        self.assertAlmostEqual(prueba_3[0], 12.05)
        self.assertAlmostEqual(prueba_3[1],10)

    def test_multiplicacion(self):
        prueba_1 = libreria_complejos.multiplicacion(self.n1, self.n2)
        self.assertAlmostEqual(prueba_1[0], 1)
        self.assertAlmostEqual(prueba_1[1],34)
        prueba_2 = libreria_complejos.multiplicacion(self.n3, self.n4)
        self.assertAlmostEqual(prueba_2[0], 19)
        self.assertAlmostEqual(prueba_2[1],-33.5)
        prueba_3 = libreria_complejos.multiplicacion(self.n5, self.n6)
        self.assertAlmostEqual(prueba_3[0], 19.7)
        self.assertAlmostEqual(prueba_3[1],64.9)

    def test_resta(self):
        prueba_1 = libreria_complejos.resta(self.n1, self.n2)
        self.assertAlmostEqual(prueba_1[0], -8)
        self.assertAlmostEqual(prueba_1[1],10)
        prueba_2 = libreria_complejos.resta(self.n3, self.n4)
        self.assertAlmostEqual(prueba_2[0], -1.5)
        self.assertAlmostEqual(prueba_2[1],-10)
        prueba_3 = libreria_complejos.resta(self.n5, self.n6)
        self.assertAlmostEqual(prueba_3[0], -1.55)
        self.assertAlmostEqual(prueba_3[1],6)


    def test_division(self):
        prueba_1 = libreria_complejos.division(self.n1, self.n2)
        self.assertAlmostEqual(prueba_1[0], -0.3483146067)
        self.assertAlmostEqual(prueba_1[1],-0.1573033708)
        prueba_2 = libreria_complejos.division(self.n3, self.n4)
        self.assertAlmostEqual(prueba_2[0], 0.05882352941)
        self.assertAlmostEqual(prueba_2[1],-2.264705882)
        prueba_3 = libreria_complejos.division(self.n5, self.n6)
        self.assertAlmostEqual(prueba_3[0], 1.02906051)
        self.assertAlmostEqual(prueba_3[1],0.8738057325)


    def test_modulo(self):
        self.assertAlmostEqual(libreria_complejos.modulo(self.n1), (3.605551275))
        self.assertAlmostEqual(libreria_complejos.modulo(self.n3), (9.340770846))
        self.assertAlmostEqual(libreria_complejos.modulo(self.n5), (9.568829605))

    def test_conjugado(self):
        prueba_1 = libreria_complejos.conjugado(self.n1)
        self.assertAlmostEqual(prueba_1[0], -3)
        self.assertAlmostEqual(prueba_1[1],-2)
        prueba_2 = libreria_complejos.conjugado(self.n3)
        self.assertAlmostEqual(prueba_2[0], 2.5)
        self.assertAlmostEqual(prueba_2[1], 9)
        prueba_3 = libreria_complejos.conjugado(self.n5)
        self.assertAlmostEqual(prueba_3[0], 5.25)
        self.assertAlmostEqual(prueba_3[1],-8)



    def test_CartToPolar(self):
        prueba_1 = libreria_complejos.cart_to_polar(self.n1)
        self.assertAlmostEqual(prueba_1[0], 3.605551275)
        self.assertAlmostEqual(prueba_1[1], 2.55359005)
        prueba_2 = libreria_complejos.cart_to_polar(self.n3)
        self.assertAlmostEqual(prueba_2[0], 9.340770846)
        self.assertAlmostEqual(prueba_2[1], -1.299849476)
        prueba_3 = libreria_complejos.cart_to_polar(self.n5)
        self.assertAlmostEqual(prueba_3[0], 9.568829605)
        self.assertAlmostEqual(prueba_3[1], 0.9900399732)


    n7 = (8, math.pi/2)
    n8 = (-2, -math.pi/11)
    n9 = (5, -math.pi/6)
    
    def test_PolarToCart(self):
        prueba_1 = libreria_complejos.polar_to_cart(self.n7)
        self.assertAlmostEqual(prueba_1[0], 0)
        self.assertAlmostEqual(prueba_1[1], 8)
        prueba_2 = libreria_complejos.polar_to_cart(self.n8)
        self.assertAlmostEqual(prueba_2[0], -1.918985947)
        self.assertAlmostEqual(prueba_2[1], 0.5634651137)
        prueba_3 = libreria_complejos.polar_to_cart(self.n9)
        self.assertAlmostEqual(prueba_3[0], 4.330127019)
        self.assertAlmostEqual(prueba_3[1], -2.5)


    def test_fase(self):
        self.assertAlmostEqual(libreria_complejos.fase(self.n1), 2.55359005)
        self.assertAlmostEqual(libreria_complejos.fase(self.n3), -1.299849476)
        self.assertAlmostEqual(libreria_complejos.fase(self.n5), 0.9900399732)
        
if __name__ == '__main__':
    unittest.main()