/*
Der Logistik GmbH stehen zehn LKWs (LKW-Nr. 1 bis 1O) für den Transport von Gütern auf Routen zur Verfügung. Jeder LKW kann
nutzlast_kg Nutzlast transportieren und auf der Ladefläche eines LKWs haben bis zu maxAnzahlPaletten Paletten Platz.

Die zu transportierenden Güter sind auf Paletten geladen. Die Daten der Paletten, die auf einer bestimmten Route transportiert
werden sollen, sind in einem zweidimensionalen Array ladungsliste gespeichert.

Für jede Palette sind Gewicht in Kilogramm, die Zuordnung zum transportierenden LKW (Nr. 1 bis 1O) und die Palettennummer
angeben. Ist die Palette noch keinem LKW zugeordnet, dann ist als LKW-Nummer der Wert 0 angegeben.

Array ladungsliste
| Gewicht der Palette in kg | LKW-Nr.| Palette-Nr.
|          800              |    0   | 276201
|          500              |    0   | 276196
|          600              |    0   | 276198
|          ...              |   ...  |
|          700              |    0   | 276179

Zur Erstellung einer Ladungsliste muss jede Palette einem LKW zugeordnet werden. Dabei gelten folgende Vorgaben:

- Ein LKW wird maximal bis zur angegeben Nutzlast (z.B. 7,5 t) oder bis zur angegebenen Anzahl Paletten (z.B. 17 Paletten)
beladen.

- Ist ein LKW vollständig beladen, und es sind noch Paletten vorhanden, dann werden die verbleibenden Paletten weiteren gleich
großen LKWs, insgesamt bis zu zehn LKWs, zugewiesen. (Übrige Paletten werden nicht mehr verladen.)

Der Methode erstelleladungsliste() werden die Daten für die LKW (Nutzlast/LKW und Anzahl zuladbare Paletten/LKW) sowie die
zweidimensionale Tabelle ladungsliste übergeben.

Die Methode soll in der zweiten Spalte der Tabelle zu jeder Palette die Nummer des LKW speichern, auf den sie verladen werden
soll: 1 für den ersten LKW, 2 für den zweiten usw.
*/



erstelleLadungliste(ladungsliste : zweidimensionales Array vom Typ Integer,	nutzlast_kg : Double, maxAnzahlPalette : Integer)
	double summeProLkw := 0
	integer i := 0
	integer paletteAnzahl := 0
	integer lkwNr := 1

	solange i < laenge(ladungsliste)
		wenn ladungsliste[i][1] = 0
			wenn (summeProLkw + ladungsliste[i][0]) <= nutzlast_kg und paletteAnzahl <= maxAnzahlPalette und lkwNr <= 10
				summeProLkw := ladungsliste[i][0] + summeProLkw
				paletteAnzahl := paletteAnzahl + 1
				ladungsliste[i][1] := lkwNr
			sonst
				lkwNr := 1 + lkwNr
				summeProLkw := 0
				paletteAnzahl := 0
				i := i - 1
			ende von wenn
		ende von wenn
		i := i + 1
	ende solange

	rueckgabe ladungsliste
ende von funktion erstelleLadungliste