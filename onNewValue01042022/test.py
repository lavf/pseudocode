import unittest
from daten import ergebnisse, TempList
from pseudocode01042022 import maxPeriod, onNewValue


tempListObj = TempList()
onNewValue(1,2,3, tempListObj)  
onNewValue(1,3,4, tempListObj)  
onNewValue(2,4,5, tempListObj)  
onNewValue(1,2,2, tempListObj) 

class Test(unittest.TestCase):    

      # Testfall 1: onNewValue(1,2,3, tempListObj) 
    def testAufgabe1onNewValue(self):     
        self.assertEqual(tempListObj.getValue(1,1).stringValue(),"Value = 1, 2, 3")
    
    # Testfall 2: onNewValue(1,3,4, tempListObj) 
    def testAufgabe2onNewValue(self):
        self.assertEqual(tempListObj.getValue(1,2).stringValue(),"Value = 1, 3, 4")

    # Testfall 3: onNewValue(2,4,5, tempListObj) 
    def testAufgabe3onNewValue(self):
        self.assertEqual(tempListObj.getValue(2,1).stringValue(),"Value = 2, 4, 5")

    # Testfall 4: onNewValue(1,2,2, tempListObj) 
    def testAufgabe4onNewValue(self): 
        self.assertEqual(tempListObj.getValue(1,3).stringValue(),"Value = 1, 2, 2")

    #############################################################################################

    # Testfall 1: Beispiel überprüfen
    def testAufgabe1maxPeriod(self):
        self.assertEqual(maxPeriod(0,22), ergebnisse[0])
    
    # Testfall 2: Wenn es eine Folge von drei Werte gibt in dem Temperturwerte-Array gibt
    def testAufgabe2maxPeriod(self):
        self.assertEqual(maxPeriod(1,22), ergebnisse[1])

    # Testfall 3: Wenn es nur eine Mindestwert gibt in dem Temperturwerte-Array gibt
    def testAufgabe3maxPeriod(self):
        self.assertEqual(maxPeriod(2,22), ergebnisse[2])

    # Testfall 4: Wenn es kein Mindestwert gibt in dem Temperturwerte-Array gibt
    def testAufgabe4maxPeriod(self):
        self.assertEqual(maxPeriod(3,22), ergebnisse[3])


if __name__ == '__main__':
    unittest.main()