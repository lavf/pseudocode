/*

kursteilnehmer[]
Kursnummer		Kursgebühr		Kundennummer		Frühbucherrabatt		Teilnehmer			Kundennummer
				   EUR			des Auftraggebers		   %									Teilnehmer
____________________________________________________________________________________________________________
201105			480,00			5001				20						Anders, Max			123
201105			480,00			4005				0						Meier, Paul			124	
201105			480,00			4005				0						Müller, Anna		125
201105			480,00			3100				0						Müller, Klaus		126
488105			980,00			1200				20						Schneider, Hans		127
488105			980,00			3100				0						Zuse, Maria			128

Übergabeparameter: kundennummer, anzahl (laenge vom Array kursteilnehmer)


*/

rechnungsbetrag_ermittlung(kundennummer : integer, anzahl : integer) : double
	double rechnungsbetrag := 0
	integer i := 0
	integer anzahlKurs := 0

	solange i < anzahl
		wenn kursteilnehmer[i].kundennummer = kundennummer dann
			anzahlKurs := anzahlKurs + 1
			wenn kursteilnehmer[i][3] <> 0
				rechnungsbetrag :=  rechnungsbetrag + (kursteilnehmer[i][1] - ((kursteilnehmer[i][1] * kursteilnehmer[i][3])/100))
			sonst 
				rechnungsbetrag := rechnungsbetrag + kursteilnehmer[i][1]
			ende wenn		
		i:= i + 1
	ende solange

	wenn anzahlKurs >= 5 dann
		rechnungsbetrag := rechnungsbetrag * 0.95
	sonst
		wenn anzahlKurs >= 3 dann
			rechnungsbetrag := rechnungsbetrag * 0.97
		ende wenn
	ende wenn

	reckgabe rechnungsbetrag