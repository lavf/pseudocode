/*  
Der Algorithmus soll nach folgenden Vorgaben entwickelt werden: 
Schritt 1:	Multiplikation aller Ziffern an gerader Stelle mit 3. 
Schritt 2: 	Bildung der Quersummen aller Ergebnisse aus Schritt 1 und 
			Addition dieser Quersummen.
Schritt 3:	Addition aller Ziffern an ungerader Stelle. 
Schritt 4: 	Addition der Ergebnisse aus den Schritten 2 und 3. 
Schritt 5: 	Berechnung der Differenz zwischen dem Ergebnis aus Schritt 4 und der nächstgrößeren
			durch 10 teilbaren Zahl. Eribt sich als Differenz 10, wird diese auf 0 gesetzt.

Ziffern-Nr			1 	2 	3	4	5	6	7	8	9	10	11	12	13	14	15	pz		Ergebnis 
_________________________________________________________________________________________________________________________
Kreditkarten-Nr 	9 	3	4	2	5	7	1	8	6	6	6	0	1	9	9	7
Schritt 1 				9 		6 		21 		24 		18		0		27 
Schritt 2 				9 		6 		2+1 	2+4 	1+8 	0		2+7 			42
Schritt 3 			9		4 		5 		1 		6 		6		1 		9			41
Schritt 4 										42 + 41			 						83 
Schritt 5 										90 - 83 						        7 (PZ) 


Die Methode wird die Kreditkartennummer als String übergeben. 
Ist die Kartennummer gültig, wird true, sonst false zurückgeben.

Methode zur Verfügung:

querSumme(zahl : int) : int
rundeAuf(zahl: int) : int

*/

pruefeKreditkartennummer(kknr : String) : Boolean {
	Integer i = 0
	
	Integer schritt2 := 0
	Integer schritt3 := 0
	Integer schritt4 := 0
	Integer pz := 0 


	solange i < laenge(kknr) - 1
		Integer schritt1 := 0
		wenn i MODULO 2 <> 0 dann			
			schritt1 := Ganzzahlwert vom kknr[i] * 3  // int(kknr[i]) * 3
			wenn schritt1 > 9 dann
				Integer tempSumme := querSumme(schritt1)
				schritt2 := schritt2 + tempSumme
			sonst
				schritt2 := schritt2 + schritt1
			ende wenn
		sonst
			schritt3 := schritt3 + Ganzzahlwert vom kknr[i] // int(kknr[i])
		ende wenn	
		i := i + 1
	ende solange

	schritt4 := schritt2 + schritt3
	pz := rundeAuf(schritt4) - schritt4

	rueckgabe pz = Ganzzahl vom kknr[15]   // int(kknr[i])
}

querSumme(zahl : Integer) : Integer {
	String tempStr := Zeichenkette vom zahl // str(zahl)
	wenn zahl > 9 dann
		rueckgabe Ganzzahlwert vom tempStr[0] + Ganzzahlwert vom tempStr[1]
	sonst
		rueckgabe zahl

}