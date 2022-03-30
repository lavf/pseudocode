import unittest
from pseudocode30032022 import erstelleKomprimierung
from daten import ergebnisse, unkomprimiert


class Test(unittest.TestCase):

    # Testfall 1: Beispiel überprüfen
    def testAufgabe1(self):
        self.assertEqual(erstelleKomprimierung(unkomprimiert[0]), ergebnisse[0])
    
    # Testfall 2: Wenn es letzte zwei verschiedene Werte des unkomprimierten Arrays gibt
    def testAufgabe2(self):
        self.assertEqual(erstelleKomprimierung(unkomprimiert[1]), ergebnisse[1])

    # Testfall 3: Wenn es letzte zwei gleiche Werte des unkomprimierten Arrays gibt
    def testAufgabe3(self):
        self.assertEqual(erstelleKomprimierung(unkomprimiert[2]), ergebnisse[2])
    
    # Testfall 4: Wenn es keine Komprimiertung gibt
    def testAufgabe4(self):
        self.assertEqual(erstelleKomprimierung(unkomprimiert[3]), ergebnisse[3])
    
    # Testfall 5: Wenn das ganze Array komprimiert wird (Fall 1)
    def testAufgabe5(self):
        self.assertEqual(erstelleKomprimierung(unkomprimiert[4]), ergebnisse[4])

    # Testfall 6: Wenn das ganze Array komprimiert wird (Fall 2)
    def testAufgabe6(self):
        self.assertEqual(erstelleKomprimierung(unkomprimiert[5]), ergebnisse[5])

    # Testfall 7: Wenn ein String die Eingabe ist
    def testAufgabe7(self):
        self.assertEqual(erstelleKomprimierung(unkomprimiert[6]), ergebnisse[6])

    # Testfall 8: Wenn das unkomprimierte Array nur eine Wert enzhält
    def testAufgabe8(self):
        self.assertEqual(erstelleKomprimierung(unkomprimiert[7]), ergebnisse[7])


if __name__ == '__main__':
    unittest.main()