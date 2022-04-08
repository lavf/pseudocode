/*
Die Soft GmbH soll für die FAQ GmbH ein Programm zur statistischen Auswertung von Daten erstellen.
Und zwar soll ermittelt werden, wie viel Prozent die Mieter von ihrem Einkommen für Miete ausgeben.
Die Daten einer Mieterbefragung zum Einkommen und zur Miete liegen in dem zweidimensionalem Array 
einkommen_miete vor, siehe folgendes Beispiel:

Array einkommen_miete
| Einkommen |   Miete  |
| 4.200,00  | 1.200,00 |
|   900,00  |   340,00 |
| 1.800,00  |   600,00 |
| 3.600,00  | 1.100,00 |
| 2.700,00  |   800,00 |
| 5.900,00  | 1.300,00 |
|     ...

Mit der zu entwickelnden Methode prozente() sollen auf Basis diese Arrays
- Einkommensgruppen gebildet werden
- und je Einkommensgruppe der prozentuale Anteil der Mieten am Gruppeneinkommen ermittelt werden.

Die gewünschte Anzahl Einkommensgruppen und deren Staffelung in EUR werden der Methode als Parameter 
anzahlGruppen und staffelung übergeben. Das folgende Beispiel zeigt die Zuordnung von Einkommen zu 
Einkommensgruppen. Übergebene Parameter: anzahlGruppen = 5 und staffelung = 1.000.

| Einkommen (in EUR) | Rechnung zur Ermittlung | Zuordnung zu      |    Bereich    |
|                    | der Einkommensgruppe    |  Einkommensgruppe |    (in EUR)   |
| 900,00             | 900 / 1.000 = 0,9       |        0          |   < 1.000     |
| 1.800,00           | 1.800 / 1.000 = 1,8     |        1          | 1.000 - 1.999 |
| 2.700,00           | 2.700 / 1.000 = 2.7     |        2          | 2.000 - 2.999 |
| 3.600,00           | 3.600 / 1.000 = 3,6     |        3          | 3.000 - 3.999 |
| 4.200,00           | 4.200 / 1.000 = 4,2     |        4          |   >= 4.000    |
| 5.900,00           | 5.900 / 1.000 = 5,9     |        4          |   >= 4.000    |

Nach der Gruppierung der Daten aus dem Array einkommen_miete sollen in der Methode prozente() die 
Daten so zusammengefasst werden, dass für jede Einkommensgruppe angegeben wird, wie viel Prozent vom 
Haushaltseinkommen diese für Miete ausgibt. Die Prozentwerte sollen im eindimensionalen Array prozente 
ausgegeben werden, siehe folgendes Beispiel:

Array prozente
| Einkommensgruppe* | Prozentualer Anteil |
|         0         |         38          |
|         1         |         33          |
|         2         |         30          |
|         3         |         31          |
|         4         |         25          |

*entspricht dem Index des Arrays

*/

prozente(ausgabe: zweidimensionales Array vom Typ Integer): eindimensionales Array vom Typ Double
	eindimensionales Array vom Typ Double prozente 	 			:= [0,0,0,0,0]
	eindimensionales Array vom Typ Double mieteProGruppe 		:= [0,0,0,0,0]
	eindimensionales Array vom Typ Double einkommenProGruppe 	:= [0,0,0,0,0]
	Integer i := 0
	Integer j := 0

	solange i < laenge(einkommen_miete)
		wenn einkommen_miete[i][0] < 1000
			einkommenProGruppe[0] := einkommenProGruppe[0] + einkommen_miete[i][0]
			mieteProGruppe[0]     := mieteProGruppe[0] + einkommen_miete[i][1]			
		sonst wenn einkommen_miete[i][0] >= 1000 und einkommen_miete[i][0] <= 1999
			einkommenProGruppe[1] := einkommenProGruppe[1] + einkommen_miete[i][0]
			mieteProGruppe[1]     := mieteProGruppe[1] + einkommen_miete[i][1]	
		sonst wenn einkommen_miete[i][0] >= 2000 und einkommen_miete[i][0] <= 2999
			einkommenProGruppe[2] := einkommenProGruppe[2] + einkommen_miete[i][0]
			mieteProGruppe[2]     := mieteProGruppe[2] + einkommen_miete[i][1]	
		sonst wenn einkommen_miete[i][0] >= 3000 und einkommen_miete[i][0] <= 3999
			einkommenProGruppe[3] := einkommenProGruppe[3] + einkommen_miete[i][0]
			mieteProGruppe[3]     := mieteProGruppe[3] + einkommen_miete[i][1]	
		sonst
			einkommenProGruppe[4] := einkommenProGruppe[4] + einkommen_miete[i][0]
			mieteProGruppe[4]     := mieteProGruppe[4] + einkommen_miete[i][1]	
		i := i + 1	

	solange j < laenge(prozente)
		prozente[j] := mieteProGruppe[j] * 100 / einkommenProGruppe[j]
		j := j + 1
	
	rueckgabe prozente
