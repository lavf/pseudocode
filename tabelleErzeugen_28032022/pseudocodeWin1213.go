erzeugeTabelle(Integer : vertreterNummer) {}

Integer i := 0

Bool vertSchonAusgedruckt := False
Bool kunSchonAusgedruckt := False

auftragsNummerAkt := VKA[i][2]

Integer hoechsteUmsatzKunden := 0
Double hoechsteUmsatz := 0

Agent-Objekt agentObj := getAgentData(vertreterNummerAkt)
Customer-Objekt custObj := getCustomerData(kundenNummerAkt)

// Tabelle erzeugen

Double summenUmstGesamt := 0
Double summenProvisionGesamt := 0

solange i < VKA.Length()
        vertreterNummerAkt := VKA[i][0]
        agentObj.getAgentData(vertreterNummer)
          

        Double vertreterUmstGesamt := 0
        Double provisionGesamt := 0

        solange vertreterNummerAkt = VKA[i][0]
            wenn vertSchonAusgedruckt = False dann
                // VertreterNr & Name
                printAgentData(agentObj)
                vertSchonAusgedruckt := True
            sonst
                vertSchonAusgedruckt := False   

            kundenNummerAkt := VKA[i][1]
            custObj.getCustomerData(kundenNummerAkt)
            wenn kunSchonAusgedruckt == False dann
                // KundeNr, Firma & Ort
                printCustomerData(custObj)
                kunSchonAusgedruckt := True
            sonst
                kunSchonAusgedruckt := False   
            
            Double nettoUmsatz := 0
            Double provision := 0

            solange i < VKA.Length() und kundenNummerAkt = VKA[i][1]
                Order-Objekt orderObj := getOrderData(auftragsNummerAkt)
                nettoUmsatz := ordenObj.NettoUmsatz + nettoUmsatz
                provision := orderObj.Provision + provision
                printOrderData(orderObj)
                ++i
            ende von solange

            vertreterUmstGesamt := nettoUmsatz + vertreterUmstGesamt
            provisionGesamt := provision + provisionGesamt
            printSum("Summe", nettoUmsatz, provision)
            
        ende von solange
        summenUmstGesamt := vertreterUmstGesamt + summenUmstGesamt
        summenProvisionGesamt := provisionGesamt + summenProvisionGesamt
        printSum("Vertreter Gesamt", vertreterUmstGesamt, provisionGesamt)
    
ende von solange
wenn hoechsteUmsatz < summenUmstGesamt dann
    hoechsteUmsatz := summenUmstGesamt
    hoechsteUmsatzKunden := vertreterNummerAkt
ende von wenn
printSum("Summen Gesamt", summenUmstGesamt, summenProvisionGesamt)


printMaxText()

