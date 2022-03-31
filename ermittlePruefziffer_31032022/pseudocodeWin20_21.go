"""
ermittlePruefziffer(ersteAchtZahle : Integer[]) : Integer

Die Prüfziffer soll nach folgender Beschreibung errechnet werden:
- Die einzelnen Ziffern werden alternierend gewichtet von links nach rechts mit 1 und 3:
	- Ziffer_1 * 1, Ziffer_2 * 3, Ziffer_3 * 1... Ziffer_9 * 1
- Die 9 gewichteten Produkte werden addiert.
- Die Prüfziffer ist die Differenz der Summe zum nächstkleineren Vielfachen von 10 (modulo 10).


sucheTopseller(kriterium: Integer, vorgabewert: Integer) : String

für ein übergebendes Kriterium und einen entsprechenden VOrgabewert den absatzstärksten Wein
ermittlen und den Barcode diese Weines als Zeichenkette ohne Prüfziffer zurückgibt. Das 2-D Array
'Absatz' steht in der Funktion zur Verfügung. Alle Weine einen unterschiedlichen, positiven Absatz 
haben.
Hinweis: Für das Zusammenfügen von Zeichenketten kann der + Operator verwendet werden. Gemischte 
Ausdrücke von Typ String und Ganzzahl sind möglich.

"""

ermittlePruefziffer(ersteAchtZahle : Integer[]) : Integer {
	Integer pruefziffer := 0
	Integer i := 0

	solange i < ersteAchtZahle.Laenge()
		wenn i % 2 == 0
			dann
				pruefziffer := ersteAchtZahle[i] * 1 + pruefziffer
			sonst
				pruefziffer := ersteAchtZahle[i] * 3 + pruefziffer
		ende von wenn
		i := i + 1
	ende von solange

	pruefziffer := pruefziffer MODULO 10	

	rueckgabe pruefziffer

ende von funktion
}

sucheTopseller(kriterium: Integer, vorgabewert: Integer) : String {
	Integer i := 0
	Integer absatzStk := 0
	String pruefziffer := ""
	
	solange i < absatz.Laenge()
		wenn absatz[i][kriterium] == vorgabewert			
			dann 
				wenn absatz[i][4] > absatzStk
					dann
						absatzStk := absatz[i][4]
						pruefziffer := absatz[i][0] + absatz[i][1] + absatz[i][2] + absatz[i][3]
				ende von wenn
		ende von wenn	

		i: i + 1
	ende von solange

	wenn pruefziffer = ""
		dann 
			pruefziffer := "Das Kriterium hatte keinen Absatz."

	rueckgabe pruefziffer

ende von funktion	
}