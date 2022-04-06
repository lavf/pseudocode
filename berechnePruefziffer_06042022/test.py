import unittest
from pseudocode06042022 import pruefeId

id1 = "6258431979"
id2 = "6258431970"
id3 = "1111111116"
id4 = "1181151216"

class Test(unittest.TestCase):    

    # Testfall 1:  Beispiel übeprüfen
    def testAufgabe1onNewValue(self):     
        self.assertEqual(pruefeId(id1), True)
    
    # Testfall 2:  Beispiel mit geändeter Prüfungsiffer
    def testAufgabe2onNewValue(self):
        self.assertEqual(pruefeId(id2), False)

    # Testfall 3: IDNummer mit eins
    def testAufgabe3onNewValue(self):
        self.assertEqual(pruefeId(id3), True)

    # Testfall 4: Beliebige IDNummer
    def testAufgabe4onNewValue(self): 
        self.assertEqual(pruefeId(id4), True)


if __name__ == '__main__':
    unittest.main()