"""
Komprimierungalgorithmus

Die Bilddaten sollen mit einer Lauflängenkodierung komprimiert werden. Dabei werden sich direkt wiederholende Zeichen
zusammengefasst, und nur die Anzahl und das entsprechende Zeichen erfasst. EIne Zusammenfassung soll erst bei mehr als 
vier Zeichen erfolgen. Zur Erkennung der Lauflängekodierung wird das ""%""-Zeichen verwendet, das in den unkomprimierten
Bilddaten nicht vorkommt. Die Bilddaten liegen als String-Arrays vor.

Funktionen stehen zu Verfügung:
laenge(String[]) : Integer
add(String[], String) : String[]
toString(Integer) : String


"""


erstelleKomprimierung(unkomprimiert: String[]) : String[] {
	String [] komprimiertesArray := []

	Integer i := 0
	Integer anzahl := 0

	von i := 0 solange i <= (laenge(unkomprimiert)-1), Schrittweite := 1
		wenn unkomprimiert[i] == unkomprimiert[i+1] und i < (laenge(unkomprimiert)-1)
		dann
			anzahl := anzahl + 1
		sonst
			wenn anzahl < 4
			dann
				Integer j := 0
				von j := 0 solange j <= anzahl, Schrittweite := 1 
					komprimiertesArray := add(komprimiertesArray, unkomprimiert[i])
				anzahl := 0
			sonst
				anzahl := anzahl +1
				komprimiertesArray := add(komprimiertesArray, "%")
				komprimiertesArray := add(komprimiertesArray, toString(anzahl))
				komprimiertesArray := add(komprimiertesArray, unkomprimiert[i])
				anzahl := 0
			

	Rueckgabe komprimiertesArray
}