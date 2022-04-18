/*
Erstellen Sie eine Methode sortProzente(prozent: eindimensionales Array von Double): 
zweidimensionales Array von Double,welche aus den Daten des eindimensonalen Arrays prozente 
ein zweidimensionales Array mit aufsteigend sortierten prozentualen Anteilen erstellt.

Beispiel für Ausgangs-Array prozente

|        Einkommensgruppe         | Prozentualer Anteil |
|(entspricht dem Index des Arrays)|                     |
|               0                 |          38         |
|               1                 |          33         |
|               2                 |          30         |
|               3                 |          31         |
|               4                 |          25         |

Beispiel für Ergebnis-Array sortProzente

|        Einkommensgruppe         | Prozentualer Anteil |
|(entspricht dem Index des Arrays)|                     |
|               4                 |          25         |
|               2                 |          30         |
|               3                 |          31         |
|               1                 |          33         |
|               0                 |          38         |

Verwenden Sie dazu folgende Idee zum Sortieren:
- Erstellen eines zweidimensionalen Arrays sortProzente:
	Anzahl Zeilen: Länge des Arrays prozente
	Anzahl Spalten: 2
- Initialisieren der Spalte 0 mit den Werten 0, 1, 2, 3, ... , Länge prozente - 1
	(Einkommensgruppen)
- Initialisieren der Spalte 1 mit den Werten aus dem Array prozente (prozentualer Anteil 
	der Miete je Einkommensgruppe)
- Durchgang 1: für alle j von 0 bis Anzahl Zeilen von sortProzente - 2
	Wenn der prozentuale Anteil (Wert) der Zeile j größer ist als der prozentuale Anteil (Wert) 
	der Zeile (j+ 1 ), dann Daten der Zeile j mit den Daten der Zeile (+ 1) vertauschen.
- Wiederholen von Durchgang 1 bis die Daten gemäß Aufgabenstellung sortiert sind.

*/

sortProzente(prozent: eindimensionales Array von Double): zweidimensionales Array von Double
	zweidimensionales Array von Double sortProzente[laenge(prozent)][2]
	Integer i := 0	

	solange i < laenge(sortProzente)
		sortProzente[i][0] := i
		sortProzente[i][1] := prozente[i]
		i := i + 1
	ende solange
	
	i := 0

	// Bubblesort
	solange i < laenge(sortProzente) - 1
		Integer j := 0
		solange j < laenge(sortProzente) - i - 1
			wenn sortProzente[j][1] > sortProzente[j+1][1] dann
				tempProAnt := sortProzente[j][1]
				tempInd := sortProzente[j][0]
				sortProzente[j][1] := sortProzente[j+1][1] 
				sortProzente[j][0] := sortProzente[j+1][0]
				sortProzente[j+1][1] := tempProAnt
				sortProzente[j+1][0] := tempInd
			ende wenn
			j := j + 1
		ende solange
		i := i + 1
	ende solange

	rueckgabe sortProzente
ende von Funktion sortProzente