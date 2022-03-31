import unittest
from pseudocode31032022 import ermittlePruefziffer, sucheTopseller
from daten import ergebnisse, arrays, absatz, absatz1, absatz2, topSeller


class Test(unittest.TestCase):

    # Testfall 1: Beispiel überprüfen
    def testAufgabe1ermittlePruefziffer(self):
        self.assertEqual(ermittlePruefziffer(arrays[0]), ergebnisse[0])
    
    # Testfall 2: Array mit 9 zeros
    def testAufgabe2ermittlePruefziffer(self):
        self.assertEqual(ermittlePruefziffer(arrays[1]), ergebnisse[1])

    # Testfall 3: Array mit 9 eins
    def testAufgabe3ermittlePruefziffer(self):
        self.assertEqual(ermittlePruefziffer(arrays[2]), ergebnisse[2])
    
    # Testfall 4: Array mit 9 zwei
    def testAufgabe4ermittlePruefziffer(self):
        self.assertEqual(ermittlePruefziffer(arrays[3]), ergebnisse[3])

    #######################################################################

    # Testfall 1: Beispiel überprüfen
    def testAufgabe1sucheTopseller(self):
        self.assertEqual(sucheTopseller(0,123,absatz), topSeller[0])
    
    # Testfall 2: Wenn das Array einen Top Seller in der letzten Zeile hat
    def testAufgabe2sucheTopseller(self):
        self.assertEqual(sucheTopseller(0,123,absatz1), topSeller[1])

    # Testfall 3: Wenn das Array keinen Top Seller hat
    def testAufgabe3sucheTopseller(self):
        self.assertEqual(sucheTopseller(0,123,absatz2), topSeller[2])
    
    # Testfall 4: Wenn das Array die übergebende Vorgabewert nicht enthält 
    def testAufgabe4sucheTopseller(self):
        self.assertEqual(sucheTopseller(0,555,absatz), topSeller[3])

    # Verschieden Kriterium

    # Testfall 5: Beispiel überprüfen
    def testAufgabe5sucheTopseller(self):
        self.assertEqual(sucheTopseller(3,2,absatz), topSeller[0])
    
    # Testfall 6: Wenn das Array einen Top Seller in der letzten Zeile hat
    def testAufgabe6sucheTopseller(self):
        self.assertEqual(sucheTopseller(3,5,absatz1), topSeller[1])

    # Testfall 7: Wenn das Array keinen Top Seller hat
    def testAufgabe7sucheTopseller(self):
        self.assertEqual(sucheTopseller(3,5,absatz2), topSeller[4])
    
    # Testfall 8: Wenn das Array die übergebende Vorgabewert nicht enthält 
    def testAufgabe8sucheTopseller(self):
        self.assertEqual(sucheTopseller(3,555,absatz), topSeller[5])
    


if __name__ == '__main__':
    unittest.main()