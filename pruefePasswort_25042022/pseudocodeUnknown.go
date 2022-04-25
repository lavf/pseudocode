/*
- Ein Passwort muss aus acht bis zehn Zeichen bestehen.
- In jedem Passwort müssen Groß- und Kleinbuchstaben sowie Ziffern und SOnderzeichen verwendet werden.
- Andere als die genannten Zeichen, dürfen nicht verwendet werden.

*/


Integer pos := 0
Integer laenge = 0
Integer zaehl_Gross = 0
Integer zaehl_Klein := 0
Integer zaehl_Sonder := 0
Integer zaehl_Ziff := 0
String zeichen := ""

String Passwort := ""

pruefePasswort(passwort : String) : String 
	String ergebnis := ""
	laenge := laenge(passwort)
	gross := "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	klein := "abcdefghijklmnopqrstuvwxyz"
	sonder := "§$%&/()=?*'-:;#+"
	ziffer := "1234567890"
	verbotenesZeichen := 0

	wenn laenge >= 8 und laenge <= 10 dann
		solange pos < laenge
			Integer i, y, j, z, x := 0
			zeichen := passwort[pos]

			solange i < laenge(gross)
				wenn zeichen = gross[i]
					zaehl_Gross := zaehl_Gross + 1
					y := 1
					abbruch
				ende wenn
				i := i + 1
			ende solange
			
			i := 0

			solange i < laenge(gross)
				wenn zeichen = klein[i] dann
					zaehl_Klein := zaehl_Klein + 1
					j := 1
					abbruch				
				ende wenn
				i := i + 1
			ende solange
			
			i := 0
			solange i < laenge(gross)
				wenn zeichen = sonder[i] dann
					zaehl_Sonder := zaehl_Sonder + 1
					z := 1
					abbruch				
				ende wenn
				i := i + 1
			ende solange

			i := 0
			solange i < laenge(gross)
				wenn zeichen = ziffer[i] dann
					zaehl_Ziffer:= zaehl_Ziffer + 1
					x := 1
					abbruch
				ende wenn
				i := i + 1
			ende solange

			wenn y + j + z + x = 0 dann
				verbotenesZeichen := verbotenesZeichen + 1

			pos := pos + 1 
		ende solange

		wenn zaehl_Gross * zaehl_Klein * zaehl_Sonder * zaehl_Ziff > 0 und verbotenesZeichen = 0 dann
			ergebnis := "Passwort ist gültig."
		sonst
			ergebnis := "Passwort ist nicht gültig"
		ende wenn
	sonst
		ergebnis := "Länge des Passworts ist nicht gültig. Es muss vom 8 bis zum 10 zeichen haben."
	ende wenn

	rueckgabe ergebnis
ende der Funktion pruefePasswort
