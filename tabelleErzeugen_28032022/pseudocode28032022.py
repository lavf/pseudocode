#import xlrd

#location = ("VKA.xlsx")

#wb = xlrd.open_workbook(location)
#sheet = wb.sheet_by_index(0)

from daten import Agent, Customer, auftraege, VKA

# Tabelle erzeugen
def erstelleTabelle():
    i = 0

    agent = Agent()

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


erstelleTabelle()           
        
                

        
    


