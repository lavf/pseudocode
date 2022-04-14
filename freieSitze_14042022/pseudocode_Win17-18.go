/*

kino = []

*/

freieSitze(anzahlSitze: int) : int
	int i := 0
	int ergebnis := 0		
	bool erstesMatch := false
	int sitzNummer := 0
	int anzahlMatch := 0

	solange i < laenge(kino)
		int j := 0
		solange j <= 30 - anzahlSitze
			int z := 0
			solange z < anzahlSitze
				wenn kino[i][j+z] = true und erstesMatch = false dann
					anzahlMatch := anzahlMatch + 1
					sitzNummer := (i + 1) * 100 + (j + 1)
					erstesMatch := true
				sonst wenn kino[i][j+z] = true und erstesMatch = true dann
					anzahlMatch := anzahlMatch + 1
				sonst wenn erstesMatch = true und anzahlMatch = anzahlSitze dann
					ergebnis := sitzNummer
				sonst wenn kino[i][j+z] = false dann
					anzahlMatch := 0
					sitzNummer := 0
					erstesMatch := false
				ende wenn
				z := z + 1
			ende solange
			j:= j + anzahlSitze
		ende solange
		i:= i + 1
	ende solange
		
	rueckgabe ergebnis
ende von funktion freieSitze
