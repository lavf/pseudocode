/* 
Um herauszufinden, von welcher Person ein Fingerabdruck stammt, soll dieser mit Fingerabdrücken 
in einer Datenbank verglichen werden. Zu jedem in der Datenbank gefundenen Fingerabdruck wird 
ein Score ermittelt, der den Prozentsatz der Übereinstimmung angibt. Bei vollständiger 
Übereinstimmung beträgt der Score 100 %. Die vorhandene Funktion suche(abdruck) gibt ein Array 
matches aus, das zu jedem gefunden Fingerabdruck einen Score, eine Personen-ID und eine Finger-ID
enthält.

Die BioScan GmbH soll nun die Prozedur auswertung erstellen, die eine Fingerabdrucksuche 
durchführt und nur Daten der Finger-abdrücke ausgibt, deren Scores oberhalb eines bestimmten
Schwellenwertes liegen.

Der Prozedur werden die folgenden drei Parameter übergeben:
abdruck 	Zeichenkette; Werte des Fingerabdruckbildes als Zeichenkette
schwelle 	ganzzahliger Wert; Werte: 1 bis 100; gibt einen Score an, ab dem Fingerabdrücke aufgelistet werden sollen
finger 		ganzzahliger Wert; 0 = Unbekannter Finger; 1 = Daumen rechts ... 10 = Kleiner Finger links

Folgende Funktionen und Prozeduren sollen verwendet werden:

suche(abdruck) Durchsucht die Datenbank nach Fingerabdrücken, die Übereinstimmungen (Matches) 
			   mit dem der Prozedur übergebenen Fingerabdruck aufweisen.
			   Bei einem Match werden die Übereinstimmung in Prozent (score), die Personen-ID 
			   und die Finger-ID (1, 2 ... 10) in einem Array vom Datentyp Match gespeichert:
			   Match: {score: Integer; idPerson: Integer; idFinger: Integer}.

laenge(array)				Liefert die Länge des Arrays
loesche(array, position) 	Löscht das Array-Element an der entsprechenden Position, die 
							Array-Länge verkürzt sich dabei um 1. Das 1. Array-Element liegt 
							an Position 0.

Zurückgegeben werden soll ein Array vom Datentyp Match:

- Das Array soll nur die Daten derjenigen Fingerabdrücke enthalten, deren Scores oberhalb des 
mit dem Übergabeparameter schwelle übergebenen Wertes liegen.

- Ist der Finger-Typ bekannt, von dem der Abdruck stammt (Übergabewertefinger= 1 bis 10), dann 
sollen nur Daten zu diesem Finger-Typ in das zurückzugebende Array übernommen werden, z. B. nur 
Daten zu rechten Zeigefingern (idfinger = 2), bei denen eine Übereinstimmung festgestellt wurde.

- Ist der Finger-Typ nicht bekannt, von dem der Abdruck stammt (Übergabewertfinger= 0), dann 
sollen die Daten zu allen Finger-Typen (idfinger = 1 bis 10) in das zurückzugebende Array 
übernommen werden, bei denen eine Übereinstimmungen festgestellt wurde.

- Das Array soll nach Score absteigend sortiert sein. Der Sortieralgorithmus muss selbst erstellt
werden.

Array matches vom Typ Match, das von der Funktion suche(abdruck) erstellt wird:

| score | idPerson | idFinger |
|   85  |   93334  |    2     |
|   80  |   48774  |    1     |
|   98  |   56446  |    2     |
|   71  |   33961  |    10    |    
|   21  |   73447  |    2     |
|   81  |   49982  |    2     |

Array, das von der Prozedur auswertung zurückgegeben werden soll.
Übergabewerte: schwelle = 80 und finger = 2

| score | idPerson | idFinger |
|   98  |   56446  |    2     |
|   85  |   93334  |    2     |
|   81  |   49982  |    2     |


*/

auswertung(abdruck: String, schwelle: Integer, finger: Integer) : Match []
	Array vom Typ Match matches := suche(abdruck)
	Integer i := 0

	solange i < laenge(matches)
		wenn (matches[i][2] <> finger und finger <> 0) oder matches[i][0] < schwelle dann
			loesche(matches, i)
		sonst
			i:= i + 1
		ende wenn
	ende solange i

	Integer j := laenge(matches) - 1

	// Bubblesort
	solange j > 0
		Integer z := 0
		solange z < j
			wenn matches[z][0] < matches[z+1][0] dann
				Integer temp:= matches[z+1]
				matches[z+1] := matches[z]
				matches[z] := temp
			ende wenn
			z := z + 1
		ende solange z
	    j := j - 1
	ende solange j

	rueckgabe matches
ende von funktion auswertung