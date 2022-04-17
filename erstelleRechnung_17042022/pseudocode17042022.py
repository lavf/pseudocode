journal = [
    ['01.04.2016', 'K00091', 100076, 2.40, 2],
    ['10.04.2016', 'K00091', 100076, 2.40, 3],
    ['10.04.2016', 'K00091', 500123, 15.0, 1],
    ['03.04.2016', 'K01234', 200234, 20.0, 1],
    ['11.04.2016', 'K01234', 200234, 20.0, 1],
    ['05.04.2016', 'K01234', 200356, 15.0, 1],
    ['05.04.2016', 'K01234', 200357, 15.0, 1]
]

def erstelleRechnung():
    i = 1
    j = 1
   # erstSatz = journal[0]
    erstKundenID = journal[0][1]
    erstLeistungsID =  journal[0][2]

    erstEinzelpreis = journal[0][3]
    erstAnzahl = journal[0][4]
    erstGesamtpreis = erstAnzahl * erstEinzelpreis
    gesamtpreis = 0.0
    rechnungssumme = 0.0
    anzahl = 0

    print(erstKundenID)
    print("Pos\tLeistungsID\tAnzahl\tEinzelpreis\tGesamtpreis")

    while j < len(journal):
        zweiterKundenID = journal[j][1]
        zweiterLeistungsID =  journal[j][2]

        zweiterEinzelpreis = journal[j][3]
        zweiterAnzahl = journal[j][4]
        zweiterGesamtpreis = zweiterAnzahl * zweiterEinzelpreis

        if erstKundenID == zweiterKundenID:
            if zweiterLeistungsID == erstLeistungsID:
                anzahl += zweiterAnzahl + erstAnzahl
                gesamtpreis += (zweiterAnzahl*zweiterEinzelpreis) + (erstAnzahl*erstEinzelpreis)
                rechnungssumme += gesamtpreis

                if j == len(journal)-1:
                    print(str(i) + '\t' + str(zweiterLeistungsID) + '\t\t' + str(anzahl) + '\t' + str(zweiterEinzelpreis) + '\t\t' + str(gesamtpreis))
                    print('\t\t\t\tRechnungsbetrag(netto)\t' + str(rechnungssumme))
                    break              
            
            else:
                if anzahl != 0:
                    print(str(i) + '\t' + str(erstLeistungsID) + '\t\t' + str(anzahl) + '\t' + str(erstEinzelpreis) + '\t\t' + str(gesamtpreis))
                else:
                    print(str(i) + '\t' + str(erstLeistungsID) + '\t\t' + str(erstAnzahl) + '\t' + str(erstEinzelpreis) + '\t\t' + str(erstGesamtpreis))

                i += 1
                anzahl = 0
                gesamtpreis = 0.0
                
        else:
            print(str(i) + '\t' + str(erstLeistungsID) + '\t\t' + str(erstAnzahl) + '\t' + str(erstEinzelpreis) + '\t\t' + str(erstGesamtpreis))
            rechnungssumme += (erstAnzahl*erstEinzelpreis)
            print('\t\t\t\tRechnungsbetrag(netto)\t' + str(rechnungssumme))

            print('\n' + str(zweiterKundenID))
            print("Pos\tLeistungsID\tAnzahl\tEinzelpreis\tGesamtpreis")
            i = 1
            rechnungssumme = 0.0

        if j == len(journal)-1:
            print(str(i) + '\t' + str(zweiterLeistungsID) + '\t\t' + str(zweiterAnzahl) + '\t' + str(zweiterEinzelpreis) + '\t\t' + str(zweiterGesamtpreis))
            rechnungssumme += (zweiterAnzahl*zweiterEinzelpreis)
            print('\t\t\t\tRechnungsbetrag(netto)\t' + str(rechnungssumme))

        # erstSatz = zweiterSatz
        erstKundenID = zweiterKundenID
        erstLeistungsID = zweiterLeistungsID
        erstEinzelpreis = zweiterEinzelpreis
        erstAnzahl= zweiterAnzahl
        erstGesamtpreis = zweiterGesamtpreis

        j += 1

erstelleRechnung()




