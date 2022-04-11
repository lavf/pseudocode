/*
Angaben zur Zeiterfassung:
- Für jeden Tag werden maximal zwei Zeiten erfasst, Kommen- und Gehen-Zeit. 
(Pausen werden nicht berücksichtig.)

Die Zeiterfassungsliste, die alle Buchungen eines Mitarbeiter für einen Monat anzeigt, 
soll wie folgt aufgebaut werden (siehe auch Beispiel).
- Liegen für einen Tag die Kommen- und Gehen-Buchungen vor, werden diese Zeiten und die berechnete
Anwesenheitszeit in Stunden und Minuten angegeben.
- Liegt für einen Tag nur eine Zeitbuchung vor, ist diese Zeit als Kommen-Zeit, die Anwesenheitszeit
00:00 und der Text "Buchung fehlt" auszugeben.
- Liegt für einen Tag keine Zeitbuchung vor, ist die Anwesenheitszeit 00:00 und der Text "nicht 
anwesend" auszugeben.
- Zum Ende der Liste ist die Summe der Anwesenheitszeiten auszugeben.

Die Kommen- und Gehen-Zeiten eines Mitarbeiter für einen Monat liegen in einer zweidimensionalen
Zeiterfassungstabelle vor.

Beispiel
Zeiterfassungsliste                                            Zeiterfassungstabelle
Mitarbeiter: 12345			Oktober 2019                       _______________________
Tag	 Kommen  Gehen  Anwesenheit  Bemerkung                    | Tag | Stunde | Minute |
===================================================           |_____|________|________|
1                   00:00        nicht anwesend               |   2 |      8 |     10 |
2    08:10   17:20  09:10                                     |   2 |     17 |     20 |
3    07:50          00:00        Buchung fehlt                |   3 |      7 |     50 |
4                   00:00        nicht anwesend               |   6 |      8 |     00 |
5                   00:00        nicht anwesend               |   6 |     16 |     00 |
6    08:00   16:00  08:00                                     |   7 |     16 |     30 |
7    16:30          00:00        Buchung fehlt                |   8 |      8 |     20 |
8    08:20   16:40  08:20                                     |   8 |     16 |     40 |
...                                                            ...
30   08:10          00:00        Buchung fehlt                |  30 |      8 |     10 |
31                  00:00        nicht anwesend               |_____|________|________|
===================================================
Summe Anwesenheit:  43:10

Funktionen zur Verfügung:

tageImMonat(monat: Integer, jahr: Integer) : Integer

schreibeKopf(persnr: Integer, jahr: Integer, monat: Integer)

schreibeZeile(tag: Integer, std1: Integer, min1: Integer, 
                            std2: Integer, min2: Integer, anwTag: Integer, bemerkung: String)

schreibeFuss(anwMonat: Integer)

* Hinweis: Für fehlende Zeiten ist der Wert -1 anzugeben. anwTag wird in der Funktion in Minuten übergeben.

*/

erzeugeListe(persnr: Integer, zeiten: zweidimensionale Tabelle vom Typ Integer, jahr: Integer, monat: Integer)
	Integer i := 1
	Integer tag := 1
	Integer aktuellerTag := zeiten[0][0]
	Integer aktuellerStd := zeiten[0][1]
	Integer aktuellerMin := zeiten[0][2]
	Integer anwMonat := 0
	Integer anzahlTage := 0

	anzahltage := tageImMonat(monat, jahr)

	schreibeKopf(persnr, jahr, monat)
	
	solange i < laenge(zeiten) und tag <= anzahlTage
		solange tag <> aktuellerTag oder zeiten[i][0] <> tag
			schreibeZeile(tag, -1, -1, -1, -1, -1, "nicht anwesend")
			tag := tag + 1

		wenn aktuellerTag = zeiten[i][0]
			Integer anwTag := ((zeiten[i][1]-12) + (12-aktuellerStd))*60 + (zeiten[i][2]-aktuellerMin)
			anwMonat := anwTag + anwMonat
			schreibeZeile(aktuellerTag, aktuellerStd, aktuellerMin, zeiten[i][1], zeiten[i][2], anwTag, "")
			i := i + 1
		sonst
			schreibeZeile(zeiten[i][0], zeiten[i][1], zeiten[i][2], -1, -1, -1, "Buchung fehlt")
		
		// Hinweis: Es muss immer die letzte Zeile berucksichtigt werden
		wenn i < laenge(zeiten) - 1
			aktuellerTag := zeiten[i][0]
			aktuellerStd := zeiten[i][1]
			aktuellerMin := zeiten[i][2]
		sonst: 
			aktuellerTag := zeiten[laenge(zeiten) - 1][0]
			aktuellerStd := zeiten[laenge(zeiten) - 1][1]
			aktuellerMin := zeiten[laenge(zeiten) - 1][2]
		
		tag := tag + 1
		i := i + 1

	solange tag <= anzahlTage
		wenn tag = aktuellerTag
			schreibeZeile(aktuellerTag, aktuellerStd, aktuellerMin, -1, -1, -1, "Buchung fehlt")
		sonst
			schreibeZeile(tag, -1, -1, -1, -1, -1, "nicht anwesend")
		
			tag := tag + 1			     

	schreibeFuss(anwMonat)
ende der Funktion erzeugeListe