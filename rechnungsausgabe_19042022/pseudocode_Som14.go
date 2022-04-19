/*

Zur Rechnungserstellung benötigt die dLine AG ein neues Programm.
Bei der zu erstellenden Methode rechnungsausgabe sind folgende Angaben zu berücksichtigen:
- Die Methode soll für einen Kunden die Rechnungen für dessen Bestellungen ausgeben.
- Der Methode wird eine Referenz auf ein Kundenobjekt als Parameter übergeben.
- Die Methode soll die Rechnungsbeträge der Rechnungen zu einem Gesamtbetrag addieren und zurückgeben.
- Die Methode soll zur Klasse RechnungsDruck (siehe unten) gehören.
- Die Methode soll auf einer Rechnungsseite höchstens 20 Positionszeilen ausgeben, danach soll sie einen
Wechsel auf die nächste Seite durchführen.
- Jede Rechnung beginnt mit der Seiten-Nummer 1.

Kunde
+ getKundenNr() : String
+ getName() : String
+ getStrasse() : String
+ getPLZ() : String 
+ getOrt() : String
+ getBestellungen() : Array von Bestellung
+ getRabatt()) : double
...

Bestellung
+ getBestellNr() : String
+ getBestellDatum() : String
+ getRechnung()· Rechnung
+ getBestellPos1tionen() : Array von BestellPosition
...

Rechnung
+ getRechnungsNr() : String
+ getRechnungsDatum() : String
...

BestellPosition
+ getBestellNr() : String
+ getPosNr() : int
+ getArtikel() : Artikel
+ getEinzelPreis() : double
+ getMenge(): int
...

Artikel
+ getArt1kelNr() : String
+ getBezeichnung() : String
...

Klasse RechnungsDruck

RechnungsDruck
+ druckeSeitenKopf(seite : int)
+ druckeRechnungsKopf(kunde: Kunde, bestellnr : int)

Bestell Position
+ getBestellNr() : Stnng
+ getPosNr() : 1nt
+ getArtikel() : Artikel
+ getEinzelPreis() : double
+ getMenge(): int

Artikel
+ getArtikelNr() : String
+ getBezeichnung() : String
...

Klasse RechnungsDruck

+ druckeSeitenKopf(seite : int)
+ druckeRechnungsKopf(kunde Kunde. bestellnr : int)
+ druckeRechnungsFuss(summeBrutto double, rabatt : double)
+ druckePositionenKopf()
+ druckePositionsZeile(posNr: int, artikelNr : String, bezeichnung: String, 
	einzelpreis : double, menge : int)

*/

rechnungsausgabe(kunde : Kunde) : double
	Integer seite := 1
	Array von Bestellung kundenBestellungen := kunden.getBestellungen()
	Integer i := 0
	Double summeBrutto := 0
	Double gesammtSummeBrutto := 0
	rd := new RechnungsDruck()

	

	solange i < len(kundenBestellungen)
		rd.druckeSeitenKopf(seite)
		rd.druckeRechnungsKopf(kunde, kundenBestellungen[i].getBestellNr())
		rd.druckePositionenKopf()
		Array von BestellPosition bestellungPositionen := kundenBestellungen[i].getBestellPositionen()
		Integer j := 0
		solange j < len(bestellungPositionen)
			wenn j MODULO 20 == 0 und j <> 0 dann
				seite := seite + 1
				rd.druckeSeitenKopf(seite)
				rd.druckePositionenKopf()

			rd.druckePositionsZeile(bestellungPositionen[j].getPosNr(),
								bestellungPositionen[j].getArtikel().getArtikelNr(),
								bestellungPositionen[j].getArtikel().getBezeichnung(),
								bestellungPositionen[j].getEinzelPreis(),
								bestellungPositionen[j].getMenge())
			summeBrutto := bestellungPositionen[j].getEinzelPreis() *  bestellungPositionen[j].getMenge() + summeBrutto
			j := j + 1

		summeBrutto := summeBrutto - (summeBrutto * kunde.getRabatt() / 100)
		summeBrutto := summeBrutto * 1.19
		gesammtSummeBrutto := summeBrutto + gesammtSummeBrutto
		rd.druckeRechnungsFuss(summeBrutto, kunde.getRabatt())
		i := i + 1
		seite := 1
		summeBrutto := 0

	rueckgabe gesamtSummeBrutto
ende der Funktion rechnungsausgabe
