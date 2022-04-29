/*
Im Rahmen des Projekts werden Sie damit beauftragt, eine Funktion generateCode() zu erstellen. 
Diese Funktion soll eine Ziffernfolge generieren, aus der das Herkunftsland, die Kalenderwoche 
und das Jahr hervorgehen. Die Ziffernfolge soll als Teil einer Auftragsnummer verwendet werden.

Der Funktion soll die Kundennummer (kdnr) und das Auftragsdatum (date) als Parameter übergeben 
werden.

Folgende Funktionen stehen zur Verfügung:

getHerkunft(kdnr)	: liefert anhand der Kundennummer die Länderkennung (z.B. GER)
getKWJahr(date)		: liefert die Kalenderwoche und Jahr des Datums im Format ,wwyyyy'

XXX 			|	Länderkennung für das Herkunftsland des Kunden
wwyyyy 			|	Kalenderwoche und Jahr des Auftrags
zzzzzzzzzzz 	|	Die Ziffernfolge setzt sich folgendermaßen zusammen:
					(
						(
							(ASCII-Wert von 1. Stelle von XXX * 91 +ASCII-Wert von 2. Stelle von XXX
							) * 91
							+ASCII-Wert von 3. Stelle von XXX
						) * 54
						+ ww
					) * 2300 + yyyy

Beispiel:

Für einen Kunden aus Deutschland (Länderkennung GER) berechnet sich die Nummer für einen Auftrag aus 
der KW 39 im Jahre 2011 wie folgt:

ASCII-Codes: G = 71; E = 69; R = 82
( ( (71 * 91 + 69) • 91 + 82) * 54 + 39)* 2300 + 2011 = 73.813.642.111

*/

generateCode(kdnr: Integer, date: String) : Integer
beginn der Funktion generateCode
	Integer code := 0
	String kwjahr := getKWJahr(date)
	String herkunft := getHerkunft(kdnr)
	String woche := kwjahr[0] & kwjahr[1]
	String jahr := kwjahr[2] & kwjahr[3] & kwjahr[4] & kwjahr[5]

	code := (
				(
					(
						(ASCII-Wert vom herkunft[0] * 91 + ASCII-Wert vom herkunft[1]) 
							* 91 + ASCII-Wert vom herkunft[2]) 
								* 54 + Ganzzahl-Wert vom woche) 
										* 2300 + Ganzzahl-Wert vom jahr


	rueckgabe code
ende der Funktion generateCode