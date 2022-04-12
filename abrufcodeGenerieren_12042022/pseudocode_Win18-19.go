/*
Jeder Abrufcode darf nur einmal existieren.

          SQ   34576197              56
zweistellige   acht Zufallsziffern   zweistellige
Kennung		   (von 1 bis 9)         Prüfzahl  (Quersumme der Stellen 3 bis 10 + Prüfzahl) modulo 97 = 1

ZufallszifferErzeugen() : Integer
AbrufcodeFinden(String) : Boolean

*/

AbrufcodeGenerieren() : String
	wiederhole	
		String ergebnis := "SQ"
		Integer i := 0
		Integer summe := 0
		String pruefzahl := ""
	
		solange i < 8
			Integer tempZufallsziffer := ZufallszifferErzeugen()
			String tempZufallszifferStr := tempZufallsziffer
			summe := summe + tempZufallsziffer
			ergebnis := ergebnis & tempZufallszifferStr
			i := i + 1
		
		pruefzahl := 98 - summe
		ergebnis:= ergebnis & pruefzahl
	solange AbrufcodeFinden(ergebnis) = true

	ruckgabe ergebnis
ende von der Funktion AbrufcodeGenerieren




