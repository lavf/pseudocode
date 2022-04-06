/*
Die IT-Dienst GmbH soll für die CarStar GmbH die Methode pruefe/D für eine Klasse entwickeln. 
Die Methode soll ID-Card-Nummern anhand einer Prüfziffernberechnung prüfen.

Beispiel für die Prüfziffernberechnung der ID 6258431979:


							Ziffernstelle 
			1 	2 	3	4	5	6	7	8	9	pz*	 			Ergebnis 
______________________________________________________________________________
ID 			6 	2	5	8	4	3	1	9	7	9 
Schritt 1 	12 		10 		8 		2 		14 
Schritt 2 	3 		1 		8 		2 		5 						19 
Schritt 3 		2 		8 		3 		9 							22 
Schritt 4 					19 + 22 								41 
Schritt 5 	41 auf nächstgrößere durch 10 teilbare Zahl aufrunden 	50 
Schritt 6 					50 - 41 								9 (PZ*) 


Der Algorithmus soll nach folgenden Vorgaben entwickelt werden: 
Schritt 1:	Multiplikation aller Ziffern an ungerader Stelle mit 2. 
Schritt 2: 	Bildung der Quersummen aller entstandenen Produkte und Addition aller entstandenen 
			Quersummen. 
Schritt 3:	Addition aller Ziffern an gerader Stelle. 
Schritt 4: 	Addition der Ergebnisse aus den Schritten 2 und 3. 
Schritt 5: 	Aufrundung des Ergebnisses aus Schritt 4 auf die nächstgrößere durch 10 teilbare Zahl, 
			falls das Ergebnis nicht ohne Rest durch 10 teilbar ist. 
Schritt 6: 	Berechnung der Differenz aus dem Ergebnis aus Schritt 5 und dem Ergebnis aus Schritt 4.

Die ID-Card-Nummer wird der Methode als String übergeben. 
Stimmen die letzte Ziffer der ID-Card-Nummer und die errechnete Prüfziffer überein, gibt die Methode 
true, sonst false zurück. 
*/

pruefeID(idNummer: String) : Boolean {
	Boolean bewertung := false
	Integer i := 0	
	String schrittEins
	Integer schrittZwei := 0
	Integer schrittVier := 0
	Integer schrittFuenf := 0
	Integer schrittSechs := 0
	Integer ungeradeQuersumme := 0
	Integer geradeQuersumme := 0
	Integer rest := 0

	solange i < 9 // IDNummer.Laenge() - 1
		wenn i modulo 2 <> 0
			schrittEins := int(idNummer[i]) * 2
			wenn int(schrittEins) > 9
				schrittZwei := int(schrittEins[0]) + int(schrittEins[1])
			sonst
				schrittZwei := int(schrittEins[0])
			ungeradeQuersumme := schrittZwei + ungeradeQuersumme
		sonst 
			geradeQuersumme := int(idNummer[i]) + geradeQuersumme
		i := i + 1

	schrittVier := ungeradeQuersumme + geradeQuersumme

	wenn schrittVier modulo 10 <> 0
		rest := 10 - (schrittVier modulo 10)
		schrittFuenf := schrittVier + rest
	sonst
		schrittFuenf := schrittVier

	schrittSechs := schrittFuenf - schrittVier

	wenn schrittSechs = int(idNummer[9])
		bewertung := true
	sonst 
		bewertung := false

	rueckgabe bewertung
}