"""
Vorberetitung der Klassen
"""

class Agent(object):

    def __init__(self, vertretername = "d", vertreteridnumber = 0):
        self.vertretername = vertretername
        self.vertreteridnumber = vertreteridnumber

    def getAgentData(self, vertreternummer):
        if vertreternummer == 4711:            
            self.vertretername = "Max Mustermann"
            self.vertreteridnumber = vertreternummer
        else:
            self.vertretername = "Bernhard Möllefrau"
            self.vertreteridnumber = 4712
        return self

    def printAgentData(self):
        print("\nVertreter\n" + str(self.vertreteridnumber) + "\t\t" + self.vertretername)


#class Order(object):
class Customer(object):
    def __init__(self, kundenname = "d", kundenidnumber = 0, kundenort = "d"):
        self.kundenname = kundenname
        self.kundenidnumber = kundenidnumber
        self.kundenort = kundenort

    def getCustomerData(self, kundennummer):
        if kundennummer == 22333:            
            self.kundenname = "Winzer e. G."
            self.kundenidnumber = kundennummer
            self.kundenort = "Würzburg"
        elif kundennummer == 33456:
            self.kundenname = "Bierkrug GmbH"
            self.kundenidnumber = kundennummer
            self.kundenort = "Berlin"
        elif kundennummer == 55728:
            self.kundenname = "TechIO"
            self.kundenidnumber = kundennummer
            self.kundenort = "Berlin"
        else:
            self.kundenname = "Lala Tata"
            self.kundenidnumber = 12345
            self.kundenort = "Loro"
        return self

    def printCustomerData(self):
        print("\nKunde\n" + str(self.kundenidnumber) + "\t\t" + self.kundenname + " \t\t" + self.kundenort)


auftraege =  [
    [4711, 22333, 33343, "01.06.2012", 2160.0, "\t 8%",  172.8],
    [4711, 22333, 33349, "12.06.2012", 570.0,  "\t 3%",  17.1],
    [4711, 22333, 34355, "14.06.2012", 430.0,  "\t 3%",  12.9],
    [4711, 22333, 35766, "16.06.2012", 4050.0, "\t 8%",  324.0],
    [4711, 22333, 35777, "29.06.2012", 5100.0, "\t 10%", 510.0],
    [4711, 33456, 31222, "02.06.2012", 1140.0, "\t 3%",  34.2],
    [4711, 33456, 32211, "13.06.2012", 1520.0, "\t 3%",  45.6],
    [4711, 33456, 33231, "15.06.2012", 450.0,  "\t 3%",  13.5],
    [4711, 33456, 35776, "17.06.2012", 4140.0, "\t 8%",  331.2],
    [4712, 55728, 12566, "17.06.2022", 5000.0, "\t 10%", 500.0],
    [4712, 55841, 12728, "17.06.2022", 3000.0, "\t 5%",  150.0]
    ]

VKA = [
    [4711, 22333, 33343],
    [4711, 22333, 33349],
    [4711, 22333, 34355],
    [4711, 22333, 35766],
    [4711, 22333, 35777],
    [4711, 33456, 31222],
    [4711, 33456, 32211],
    [4711, 33456, 33231],
    [4711, 33456, 35776],
    [4712, 55728, 12566],
    [4712, 55841, 12728]
]