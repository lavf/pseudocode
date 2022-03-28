#import xlrd

#location = ("VKA.xlsx")

#wb = xlrd.open_workbook(location)
#sheet = wb.sheet_by_index(0)

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

# Tabelle erzeugen

i = 0

agent = Agent()

aufAlreadyPrinted = False
vAlreadyPrinted = False
kAlreadyPrinted = False

custObj = Customer()

summeAuftraege = 0
summeProvAuftraege = 0
vertreterGesamtUmst = 0
vertreterGesamtProv = 0
summenGesamtUmst = 0
summenGesamtProv = 0
hoechsterVertreterUmst = 0
hoechsterVertreterId = 0
hoechsterVertreterName = "d"

while (i < len(auftraege)):
    #vertreterNummerAkt = sheet.cell_value(i,0)
    vertreterNummerAkt = VKA[i][0]
    agent.getAgentData(vertreterNummerAkt)

    while (vertreterNummerAkt == auftraege[i][0]):
        if vAlreadyPrinted == False:
            agent.printAgentData()
            vAlreadyPrinted = True
            summenGesamtUmst = summenGesamtUmst + vertreterGesamtUmst
            summenGesamtProv = summenGesamtProv + vertreterGesamtProv
            vertreterGesamtProv = 0
            vertreterGesamtUmst = 0
        else: 
            vAlreadyPrinted = False
        #kundenNummerAkt = sheet.cell_value(i,1)
        kundenNummerAkt = VKA[i][1]
        custObj.getCustomerData(kundenNummerAkt)

        if kundenNummerAkt == auftraege[i][1] and kAlreadyPrinted == False:  
            custObj.printCustomerData()
            print("Auftrags-Nr. \t Datum \t\t\t Nettoumsatz \t\t Prov.-Satz \t Provision")
            kAlreadyPrinted = True
        else:
            kAlreadyPrinted = False

        while (i < len(auftraege) and kundenNummerAkt == auftraege[i][1]):
            print(str(auftraege[i][2]) + "\t\t" + auftraege[i][3] + "\t\t" + str(auftraege[i][4]) + "\t\t" + auftraege[i][5] + "\t\t" + str(auftraege[i][6]))
            summeAuftraege = summeAuftraege + auftraege[i][4]
            summeProvAuftraege = summeProvAuftraege + auftraege[i][6]
            i = i + 1
        else:
            print("Summe____________________________________" + str(summeAuftraege) + "\t\t\t\t" + str(summeProvAuftraege))
            vertreterGesamtUmst = summeAuftraege + vertreterGesamtUmst
            vertreterGesamtProv = summeProvAuftraege + vertreterGesamtProv            
            summeAuftraege = 0
            summeProvAuftraege = 0               

            if i < 11 and vertreterNummerAkt == auftraege[i][0]:   
                custObj.getCustomerData(auftraege[i][1])
                custObj.printCustomerData()
                print("Auftrags-Nr. \t Datum \t\t\t Nettoumsatz \t\t Prov.-Satz \t Provision")
                vertreterNummerAkt = VKA[i][0]
                agent.getAgentData(vertreterNummerAkt)
            elif i < 11 and vertreterNummerAkt != auftraege[i][0]:  
                print("\nVertreter Gesamt\t\t" + str(vertreterGesamtUmst) + "\t\t" + str(vertreterGesamtProv))
                if hoechsterVertreterUmst < vertreterGesamtUmst:
                    hoechsterVertreterId = agent.vertreteridnumber
                    hoechsterVertreterName = agent.vertretername
                    hoechsterVertreterUmst = vertreterGesamtUmst
            else:
                summenGesamtUmst = summenGesamtUmst + vertreterGesamtUmst
                summenGesamtProv = summenGesamtProv + vertreterGesamtProv
                if hoechsterVertreterUmst < vertreterGesamtUmst:
                    hoechsterVertreterId = agent.vertreteridnumber
                    hoechsterVertreterName = agent.vertretername
                    hoechsterVertreterUmst = vertreterGesamtUmst
                print("\nVertreter Gesamt\t\t" + str(vertreterGesamtUmst) + "\t\t" + str(vertreterGesamtProv))
                break
            

print("\nSummen Gesamt\t\t\t" + str(summenGesamtUmst) + "\t\t" + str(summenGesamtProv))

print("\nVertreter mit dem höchsten Umsatz: " + str(hoechsterVertreterId) + ", " + hoechsterVertreterName + ", " + str(hoechsterVertreterUmst))

        
        
        
                

        
    


