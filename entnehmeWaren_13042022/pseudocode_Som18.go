fehler = []

entnehmeWare(liste: zweidimensionales Array vom Typ int)
	Integer i := 0
	Integer anzahlFehler := 0	

	solange i < laenge(liste)
		fahreRegalAn(liste[i][1])
		Integer regalStart := liste[i][1]
		solange i < laenge(liste) und regalStart = liste[i][1]
			fahreEbeneAn(liste[i][2])
			Integer ebeneStart := liste[i][2]
			solange i < laenge(liste) und ebeneStart = liste[i][2] und regalStart = liste[i][1]
				fahreFachAn(liste[i][3])
				wenn pruefeWare(liste[i][0]) = true
					entnehmeWare(liste[i][1],liste[i][2],liste[i][3])
				sonst
					kopiereZeile(liste, fehler, i, anzahlFehler)
					anzahlFehler := anzahlFehler + 1
				ende wenn
				i:= i + 1
			ende solange
		ende solange
	ende solange
ende von Funktion entnehmeWare
