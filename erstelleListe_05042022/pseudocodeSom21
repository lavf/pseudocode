/*
hole_satz() : String
lese_m_id(satz: String) : Integer
lese_anz_std(satz: String) : Integer
schreibe_kopf()
schreibe_daten(
	nr: Integer,
	mitgliedId: Integer,
	leistungid: Integer,
	anzahlstunden: Integer,
	stundensatz: Double,
	summe: Double
)
schreibe_summe(summe:Double)
schreibe_gsumme(gsumme:Double)


*/

erstelle_liste(stundensatz: Double) {
	
	Integer anzahlstunden := 0
	Double produkt := 0
	Double summe := 0
	Double gsumme := 0
	Integer nr := 0
	String satz := hole_satz()
	String naechsteSatz
	
	schreibe_kopf()

	solange naechsteSatz := hole_satz() <> ""
		
		wenn lese_m_id(satz) = lese_m_id(naechsteSatz) und lese_l_id(satz) = lese_l_id(naechsteSatz) und anzahlstunden = 0
			anzahlstunden := lese_anz_std(satz) + lese_anz_std(naechsteSatz)
		oder wenn lese_m_id(satz) = lese_m_id(naechsteSatz) und lese_l_id(satz) = lese_l_id(naechsteSatz) und anzahlstunden <> 0
			anzahlstunden := anzahlStunden + lese_anz_std(naechsteSatz)
		sonst
			wenn lese_m_id(satz) <> lese_m_id(naechsteSatz)
				anzahlStunden := lese_anz_std(satz)
			ende von wenn
			
			nr:= nr + 1
			produkt := stundensatz * anzahlstunden
			summe := produkt + summe			
		 	schreibe_daten(nr,lese_m_id(satz), lese_l_id(satz), anzahlStunden, stundensatz, produkt)
			anzahlstunden := 0
			produkt := 0
			
			wenn lese_m_id(satz) <> lese_m_id(naechsteSatz)
				gsumme := summe + gsumme
				schreibe_summe(summe)
				nr := 0
				summe := 0
			ende von wenn
		
		satz := naechsteSatz

		ende von wenn
	ende von solange

	schreibe_daten(nr,lese_m_id(satz), lese_l_id(satz), lese_anz_std(satz), stundensatz, (lese_anz_std(satz)*stundensatz))			
	schreibe_summe(summe + (lese_anz_std(satz)*stundensatz))
	gsumme := summe + (lese_anz_std(satz)*stundensatz) + gsumme
	schreibe_gsumme(gsumme)
}