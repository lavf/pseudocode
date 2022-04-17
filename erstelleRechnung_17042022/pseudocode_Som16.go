/*

Journal
|    Datum   | KundenID | LeistungsID | EinzelPreis | Anzahl |
| 01.04.2016 |  K00091  |   100076    |     2,40    |   2    |
| 10.04.2016 |  K00091  |   100076    |     2,40    |   3    |
| 10.04.2016 |  K00091  |   500123    |    15,00    |   1    |
| 03.04.2016 |  K01234  |   200234    |    20,00    |   1    |
| 11.04.2016 |  K01234  |   200234    |    20,00    |   1    |
| 05.04.2016 |  K01234  |   200356    |    15,00    |   1    |


hole_journalsatz() : String
lese_kundenid(satz: String) : Integer
lese_leistungsid(satz: String) : Integer
lese_einzelpreis(satz : String) : Double
lese_anzahl(satz: String) : Integer
hole_bezeichnung(leistungsid: Integer) : String
schreibe_kundenid(kundenid: Integer)
schreibe_kopfzeile()
schreibe_positionszeile(pos: Integer, leistungsid: Integer, bezeichnung: String,
						anzahl: Integer, einzelpreis: Double, gesamtpreis: Double)
schreibe_rechnungssumme(rechnungssumme: Double)

*/

erstelleRechnung() {
	Integer i := 1
	String erstSatz := hole_journalsatz()
	Integer erstKundenID := lese_kundenid(erstSatz)
	Integer erstLeistungsID := lese_leistungsid(erstSatz)

	Double erstEinzelpreis := lese_einzelpreis(erstSatz)
	Integer erstAnzahl:= lese_anzahl(erstSatz) 
	String erstBezeichnung := lese_bezeichnung(erstSatz)
	Double erstGesamtpreis := erstAnzahl * erstEinzelpreis
	Double gesamtpreis := 0
	Double rechnungssumme := 0
	Integer anzahl := 0

	schreibe_kundenid(erstKundenID)
	schreibe_kopfzeile()

	String zweiterSatz := hole_journalsatz()

	solange zweiterSatz <> "" 
		Integer zweiterKundenID := lese_kundenid(zweiterSatz)
		Integer zweiterLeistungID := lese_leistungsid(zweiterSatz)
		Double zweiterEinzelpreis := lese_einzelpreis(zweiterSatz)
		Integer zweiterAnzahl:= lese_anzahl(zweiterSatz) 		
		Double aktGesamtpreis := zweiterAnzahl * zweiterEinzelpreis

		wenn erstKundenID = zweiterKundenID dann
			wenn zweiterLeistungsID = erstLeistungsID
				anzahl := zweiterAnzahl + erstAnzahl + anzahl
				gesamtpreis := (zweiterAnzahl*zweiterEinzelpreis) + (erstAnzahl*erstEinzelpreis) + gesamtpreis
				rechnungssumme := gesamtpreis + rechnungssumme
			sonst
				wenn anzahl <> 0 dann	
					schreibe_positionszeile(i, erstLeistungsID, erstbezeichnung, anzahl, erstEinzelpreis, gesamtpreis)
				sonst
					schreibe_positionszeile(i, erstLeistungsID, erstbezeichnung, erstAnzahl, erstEinzelpreis, erstGesamtpreis)
				
				i:= i + 1
				anzahl := 0
				gesamtpreis := 0
		sonst
			schreibe_positionszeile(i, erstLeistungsID, erstBezeichnung, erstAnzahl, erstEinzelpreis, erstGesamtpreis)	
			rechnungssumme := rechnungssumme + (erstAnzahl * erstEinzelpreis)
			schreibe_rechnungssumme(rechnungssumme)

			schreibe_kundenid(zweiterKundenID)
			schreibe_kopfzeile()
			i := 1
			rechnungssumme := 0

		erstSatz := zweiterSatz
		zweiterSatz := hole_journalsatz()

		wenn zweiterSatz = ""
			wenn erstKundenID = zweiterKundenID und erstLeistungsID = zweiterLeistungID dann
				schreibe_positionszeile(i, erstLeistungsID, erstbezeichnung, anzahl, erstEinzelpreis, gesamtpreis)
			sonst
				schreibe_positionszeile(i, zweiterLeistungsID, zweiterBezeichnung, zweiterAnzahl, zweiterEinzelpreis, erstGesamtpreis)	
				rechnungssumme := (zweiterEinzelpreis * zweiterAnzahl) + rechnungssumme
			
			schreibe_rechnungssumme(rechnungssumme)
		sonst
			erstKundenID := zweiterKundenID
			erstLeistungsID := zweiterLeistungID
	    	erstEinzelpreis := zweiterEinzelpreis
	    	erstAnzahl:= zweiterAnzahl
	    	erstGesamtpreis := aktGesamtpreis

	
}

