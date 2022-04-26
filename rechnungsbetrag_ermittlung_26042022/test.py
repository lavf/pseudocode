import unittest
from pseudocode26042022 import rechnungsbetrag_ermittlung


class Test(unittest.TestCase):    

    # Testfall 1: 'Zuse, Maria'
    def testAufgabe1onNewValue(self):     
        self.assertEqual(rechnungsbetrag_ermittlung(126),584.00)
    
    # Testfall 2: 'Anders, Max' 
    def testAufgabe2onNewValue(self):
        self.assertEqual(rechnungsbetrag_ermittlung(123),1793.60)

    # Testfall 3: 'Müller, Anna'
    def testAufgabe3onNewValue(self):
        self.assertEqual(rechnungsbetrag_ermittlung(125),2302.80)

    # Testfall 4: 'Meier, Paul' 
    def testAufgabe4onNewValue(self): 
        self.assertEqual(rechnungsbetrag_ermittlung(124),1125.20)



if __name__ == '__main__':
    unittest.main()