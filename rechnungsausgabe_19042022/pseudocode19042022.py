from daten import RechnungsDruck, kundeObj1

def rechnungsausgabe(kunde):
    seite = 1
    kundenBestellungen = kunde.getBestellungen()
    i = 0
    summeBrutto = 0.0
    gesammtSummeBrutto = 0.0
    rd = RechnungsDruck()    

    while i < len(kundenBestellungen):
        rd.druckeSeitenKopf(seite)
        rd.druckeRechnungsKopf(kunde, kundenBestellungen[i].getBestellNr())
        rd.druckePositionenKopf()
        j = 0
        bestellungPositionen = kundenBestellungen[i].getBestellPositionen()

        while j < len(bestellungPositionen):
            if j % 20 == 0 and j != 0:
                seite += 1
                print("\n")
                rd.druckeSeitenKopf(seite)
                rd.druckePositionenKopf()

            rd.druckePositionsZeile(bestellungPositionen[j].getPosNr(),
								bestellungPositionen[j].getArtikel().getArtikelNr(),
								bestellungPositionen[j].getArtikel().getBezeichnung(),
								bestellungPositionen[j].getEinzelPreis(),
								bestellungPositionen[j].getMenge())
            summeBrutto = bestellungPositionen[j].getEinzelPreis() *  bestellungPositionen[j].getMenge() + summeBrutto
            j += 1
        summeBrutto = summeBrutto - (summeBrutto * kunde.getRabatt() / 100)
        summeBrutto = summeBrutto * 1.19
        gesammtSummeBrutto += summeBrutto
        rd.druckeRechnungsFuss(round(summeBrutto,2), kunde.getRabatt())
        i += 1
        print ("\n")
        seite = 1
        summeBrutto = 0.0
    
    return gesammtSummeBrutto


print(rechnungsausgabe(kundeObj1))