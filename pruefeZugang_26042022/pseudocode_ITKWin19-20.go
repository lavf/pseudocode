/*
Zugang
- AnzahlFehlversuche : int = 0
+ pruefeZugang(pKennung : String, pPasswort : String) : boolean

Methode zur Verfügung:

System.Wait(Sekunden: int)
System.GetPassword(Kennung : String)

*/

integer AnzahlFehler := 0

pruefeZugang(pKennung: String, pPasswort: String) : boolean 
	boolean Ergebnis := false
	String Passwort := ""

	Passwort := System.GetPassword(pKennung)

	wenn Passwort = pPasswort und Passwort <> ""
		Ergebnis := true
	sonst
		AnzahlFehler := AnzahlFehler + 1
		wenn AnzahlFehler > 3 dann
			System.Wait(30)		

	rueckgabe Ergebnis