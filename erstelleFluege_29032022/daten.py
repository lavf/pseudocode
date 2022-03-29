""" 
Vorberetitung der Klassen

Klasse: Flug
- id: String
- flugDatum: Date // String
- abflugZeit: Date // String
- ankunftZeit: Date // String
- preis: Double
- freiePlaetze: Integer
...


Array Linien_Fluege enthält die Flug-Objekte aller Flüge, die auf einer bestimmten Streke nonstop durchgeführt werden.
"""


Linien_Fluege = [
    [10001, "22.03.2022", "15:33", "17:24", 150.67,  23 ],
    [10002, "12.05.2022", "00:33", "10:24", 2150.67, 134],
    [10003, "23.02.2023", "16:36", "19:26", 550.67,  4  ],
    [10004, "28.08.2022", "11:33", "12:24", 350.47,  55 ],
    [10005, "28.08.2022", "14:33", "16:24", 250.67,  34 ],
    [10006, "13.04.2022", "15:33", "00:24", 750.67,  78 ],
    [10007, "24.02.2022", "05:33", "07:24", 150.60,  100],
    [10008, "20.11.2022", "15:33", "18:24", 350.67,  -3 ],
    [10009, "22.03.2022", "12:33", "14:24", 320.07,  3  ],
    [10010, "22.03.2022", "17:33", "19:24", 330.57,  15 ],
    [10011, "22.03.2022", "23:33", "01:24", 250.67,  2  ],
]

class Flug(object):

    def __init__(self, id = 0, flugDatum= "d", abflugZeit = "d", ankunftZeit = "d", preis = 0, freiePlaetze = 300):
        self.id = id
        self.flugDatum = flugDatum
        self.abflugZeit = abflugZeit
        self.ankunftZeit = ankunftZeit
        self.preis = preis
        self.freiePlaetze = freiePlaetze
        """self.instanz1 = {'flugDatum' : flugDatum,
                         'abflugZeit'  : abflugZeit,
                         'ankunftZeit' : ankunftZeit,
                         'preis': preis,
                         'freiePlaetze': freiePlaetze}"""

    #def __del__(self):
        #print("Destruktor anrufen")

    def getFlugDaten(self, id):
        i = 0

        while i < len(Linien_Fluege):
            if Linien_Fluege[i][0] == id:
                self.id = id
                self.flugDatum = Linien_Fluege[i][1]
                self.abflugZeit = Linien_Fluege[i][2]
                self.ankunftZeit = Linien_Fluege[i][3]
                self.preis = Linien_Fluege[i][4]
                self.freiePlaetze = Linien_Fluege[i][5]
            i += 1            
        return self

    def getId(self):
        return self.id

    def getFlugDatum(self):
        return self.flugDatum

    def printFluegeDaten(self):
        print(str(self.id) + "\t" + self.flugDatum + "\t" + str(self.abflugZeit) + "\t"
         + self.ankunftZeit + "\t" + str(self.preis) + "\t" + str(self.freiePlaetze)) 