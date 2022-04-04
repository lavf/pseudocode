/* 
Methode =
GetRouten(Klasse AngebotErstellung) : Route []
ErstelleAngebot(Klasse AngebotErstellung) : Angebot
GetStrecken(Klasse Route) : Strecke []
Length()

					AngebotErstellung
+ ErzeugeAngebotsnummer( kundenNummer: string): int
+ GetRouten( startOrt: string, zielOrt: string, versandTermin: DateTime,): Route[]
+ GetPreisOhneRabatt( routenpreis: double, gewicht: double): double
+ GetGewichtsRabattlnProzent(gewicht: double): double
+ GetKundenRabattlnProzent( kundenNummer: string): double
+ ErstelleAngebot( kundennummer: string, startOrt: string, zielOrt: string, gewicht: double, versandTermin: DateTime, ): Angebot

		Strecke
+ Start: string read-only
+ Ziel: string read-only
+ Preis: double read-only

		Route
- Strecken : Strecke [ ]
+ GetStrecken: Strecke[ ] read-only, ordered

		Angebot
+ Angebotsnummer: int
+ Kundennummer: string
+ PreisOhneRabatt: double
+ PreisMitRabatt: double
+ RabattProzentsatz: double
+ Route: Route

Routen
Route 	Strecken
0 		B- HH; HH- K
1 		B-K
2 		B - L; L - F; F - K

Route-Objekts 2
Strecke 	Start 	Ziel 	Preis
0 			B		L 		1.10
1 			L 		F 		1.60
2 			F 		K 		0.90

*/

ErstelleAngebot(kundennummer: string, startOrt: string, zielOrt: string, gewicht: double, versandTermin: DateTime): Angebot {
	Angebot ergebnis = new Angebot()
	ergebnis.Kundennummer := kundennummer
	ergebnis:Angebotsnummer := ErzeugeAngebotsnummer(kundennummer)
	
	Route routenArray := GetRouten(startOrt,zielOrt,versandTermin)
	Integer i := 0	
	Double subSumme := 0
	Integer pos := 0
	
	solange i < routenArray.Length()
		streckenArray = GetStrecken(routenArray[i])
		Integer j := 0		
		
		Double tempSumme := 0

		solange j < streckenArray.Length()
			tempSumme := streckenArray.Preis + tempSumme
			j := j + 1			

		wenn subSumme = 0
			subSumme := tempSumme
			pos := i			

		wenn subSumme <> 0 und subSumme > tempSumme
			subSumme := tempSumme
			pos := i		

		i := i + 1 

		ergebnis.Route := routenArray[pos]
		ergebnis.PreisOhneRabatt := GetPreisOhneRabatt(subSumme, gewicht)

		Double gewichtRabattInProzent := GetGewichtsRabattlnProzent(gewicht)
		Double kundenRabattInProzent := GetGewichtsRabattlnProzent(kundennummer)

		wenn gewichtRabattInProzent > kundenRabattInProzent
			ergebnis.RabattProzentsatz := gewichtRabattInProzent
		sonst
			ergebnis.RabattProzentsatz := kundenRabattInProzent

		ergebnis.PreisMitRabatt := ergebnis.PreisOhneRabatt - ((ergebnis.PreisOhneRabatt * ergebnis.RabattProzentsatz) / 100)

	
	rueckgabe ergebnis

}