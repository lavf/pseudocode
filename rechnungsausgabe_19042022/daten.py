### 1° Klassen 
### 2° Daten


class Artikel(object):
    def __init__(self, artikelNr, bezeichnung):
        self._artikeldata = [artikelNr, bezeichnung]

    def __getitem__(self, item):
        return self._artikeldata[item]

    def getArtikelNr(self):
        return self._artikeldata[0]

    def getBezeichnung(self):
        return self._artikeldata[1] 


class BestellPosition(object):
    def __init__(self, bestellNr, posNr, artikel, einzelPreis, menge):
        self._bestellpositiondata = [bestellNr, posNr, artikel, einzelPreis, menge]

    def __getitem__(self, item):
        return self._bestellpositiondata[item]

    def getBestellNr(self):
        return self._bestellpositiondata[0]

    def getPosNr(self):
        return self._bestellpositiondata[1]

    def getArtikel(self):
        return self._bestellpositiondata[2]

    def getEinzelPreis(self):
        return self._bestellpositiondata[3]

    def getMenge(self):
        return self._bestellpositiondata[4]


class Rechnung(object):
    def __init__(self, rechnungNr, rechnungsDatum):
        self._rechnungdata = [rechnungNr, rechnungsDatum]

    def __getitem__(self, item):
         return self._rechnungdata[item]

    def getRechnungsNr(self):
        return self._rechnungdata[0]

    def getRechnungsDatum(self):
        return self._rechnungdata[1]


class Bestellung(object):
    def __init__(self, bestellNr, bestellDatum, rechnung, bestellPositionen):
        self._bestellungdata = [bestellNr, bestellDatum, rechnung, bestellPositionen]

    def __getitem__(self, item):
         return self._bestellungdata[item]
        
    def getBestellNr(self):
        return self._bestellungdata[0]

    def getBestellDatum(self):
        return self._bestellungdata[1]
    
    def getRechnung(self):
        return self._bestellungdata[2]

    def getBestellPositionen(self):
        return self._bestellungdata[3]


class Kunde(object):
    def __init__(self, kundenNr, name, strasse, PLZ, ort, bestellungen, rabatt):
        self._kundendata = [kundenNr, name, strasse, PLZ, ort, bestellungen, rabatt]
        #self._kundenNr = kundenNr
        #self._name = name
        #self._strasse = strasse
        #self._PLZ = PLZ
        #self._ort = ort
        #self._rabatt = rabatt

    def __getitem__(self, item):
         return self._kundendata[item]

    def getKundenNr(self):
        return self._kundendata[0]

    def getName(self):
        return self._kundendata[1]
    
    def getStrasse(self):
        return self._kundendata[2]

    def getPLZ(self):
        return self._kundendata[3]

    def getOrt(self):
        return self._kundendata[4]

    def getBestellungen(self):
        return self._kundendata[5]

    def getRabatt(self):
        return self._kundendata[6]


class RechnungsDruck(object):
    def druckeSeitenKopf(self, seite):
        print("\t\t\t\t\t\t\t\t\t\t\tSeite " + str(seite))

    def druckeRechnungsKopf(self, kunde, bestellNr):
        temp = kunde.getBestellungen()
        i = 0

        while i < len(temp):
            if temp[i][0] == bestellNr:
                bestellObj = temp[i]
            i += 1

        print(kunde.getName() + "\t\t\t\t\t\t\tRechnungsdatum " + bestellObj.getRechnung().getRechnungsDatum() + "\n" + kunde.getStrasse()+ "\t\t\t\t\t\t\t\tRechnungsnummer " + bestellObj.getRechnung().getRechnungsNr() +"\n" + str(kunde.getPLZ()) + " " + kunde.getOrt() + "\t\t\t\t\t\t\tKundennummer " + kunde.getKundenNr() + "\n\nIhre Bestellung " + bestellNr + " vom " + bestellObj.getBestellDatum())

    def druckeRechnungsFuss(self, summeBrutto, rabatt):
        temp = round((summeBrutto / 1.19) * 100 / (100 - rabatt),2)
    
        print("\t\t\t\t\t\t\tSumme netto\t\t\t" + str(temp))
        print("\t\t\t\t\t\t\tRabatt ("  + str(rabatt) + "%)\t\t\t-" + str(round((temp * rabatt / 100), 2)))
        print("\t\t\t\t\t\t\tSumme netto abzgl. Rabatt\t" + str(round((summeBrutto / 1.19),2)))
        print("\t\t\t\t\t\t\tUSt (19%)\t\t\t" + str(round((summeBrutto * 0.19 / 1.19),2)))
        print("\t\t\t\t\t\t\tSumme brutto\t\t\t" + str(summeBrutto))

    def druckePositionenKopf(self):
        print("Position\tArtikelNr\tBezeichnung\t\tEinzelpreis (EUR)\tMenge\tPreis (EUR)")

    def druckePositionsZeile(self, posNr, artikelNr, bezeichnung, einzelpreis, menge):
        tempPreis = menge * einzelpreis
        print("\t" + str(posNr) + "\t" + artikelNr + "\t\t" + bezeichnung + "\t" + str(einzelpreis) + "\t\t\t" + str(menge) + "\t" + str(tempPreis))





# Daten: Objekten


artObj1 = Artikel("A1001","Shampoo Haarfein")
artObj2 = Artikel("A0345","Körperlotion M100")
artObj3 = Artikel("A4013","Luxusseife Ramona")

bestPosObj1 = BestellPosition("B1234", 1, artObj1, 5.00, 10)
bestPosObj2 = BestellPosition("B1234", 2, artObj2, 3.50, 2)
bestPosObj3 = BestellPosition("B1234", 3, artObj3, 25.00, 1)
bestPosObj4 = BestellPosition("B1234", 4, artObj1, 129.00, 1)
bestPosObj5 = BestellPosition("B1234", 5, artObj2, 0, 2)
bestPosObj6 = BestellPosition("B1234", 6, artObj3, 0, 1)
bestPosObj7 = BestellPosition("B1234", 7, artObj1, 0, 10)
bestPosObj8 = BestellPosition("B1234", 8, artObj2, 0, 2)
bestPosObj9 = BestellPosition("B1234", 9, artObj3, 0, 1)
bestPosObj10 = BestellPosition("B1234", 10, artObj1, 0, 10)
bestPosObj11 = BestellPosition("B1234", 11, artObj1, 0, 10)
bestPosObj12 = BestellPosition("B1234", 12, artObj2, 0, 2)
bestPosObj13 = BestellPosition("B1234", 13, artObj3, 0, 1)
bestPosObj14 = BestellPosition("B1234", 14, artObj1, 0, 10)
bestPosObj15 = BestellPosition("B1234", 15, artObj2, 0, 2)
bestPosObj16 = BestellPosition("B1234", 16, artObj3, 0, 1)
bestPosObj17 = BestellPosition("B1234", 17, artObj1, 0, 10)
bestPosObj18 = BestellPosition("B1234", 18, artObj2, 0, 2)
bestPosObj19 = BestellPosition("B1234", 19, artObj3, 0, 1)
bestPosObj20 = BestellPosition("B1234", 20, artObj1, 0, 10)
bestPosObj21 = BestellPosition("B1234", 21, artObj1, 0, 10)
bestPosObj22 = BestellPosition("B1234", 22, artObj2, 0, 2)
bestPosObj23 = BestellPosition("B1234", 23, artObj3, 0, 1)

bestPosArray = [bestPosObj1, bestPosObj2, bestPosObj3, bestPosObj4, bestPosObj5,
                bestPosObj6, bestPosObj7, bestPosObj8, bestPosObj9, bestPosObj10,
                bestPosObj11, bestPosObj12, bestPosObj13, bestPosObj14, bestPosObj15,
                bestPosObj16, bestPosObj17, bestPosObj18, bestPosObj19, bestPosObj20,
                bestPosObj21, bestPosObj22, bestPosObj23]

rechObj1 = Rechnung("R1234", "14.04.2014")

bestObj1 = Bestellung("B1234", "13.03.2014", rechObj1 , bestPosArray)

### x-Bestellung

xartObj1 = Artikel("A1001","Shampoo Haarfein")
xartObj2 = Artikel("A0345","Körperlotion M100")
xartObj3 = Artikel("A4013","Luxusseife Ramona")

xbestPosObj1 = BestellPosition("X1234", 1, xartObj1, 5.00, 10)
xbestPosObj2 = BestellPosition("X1234", 2, xartObj2, 3.50, 2)
xbestPosObj3 = BestellPosition("X1234", 3, xartObj3, 25.00, 1)

xbestPosArray = [xbestPosObj1, xbestPosObj2, xbestPosObj3]

rechObj2 = Rechnung("R1235", "14.06.2014")

bestObj2 = Bestellung("X1234", "13.05.2014", rechObj2, xbestPosArray)

##################################################################################

bestArray = [bestObj1, bestObj2]

kundeObj1 = Kunde("K1234", "Erwin Mustermann", "Musterweg 7", 77777, "Musterstadt", bestArray, 2.0)

