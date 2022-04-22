/*

Angaben zur Zeiterfassung:
- Für jeden Tag werden maximal zwei Zeiten erfasst, Kommen- und Gehen-Zeit. 
(Pausen werden nicht berücksichtig.)

Der Report, der alle Buchungen eines Mitarbeiter für einen Monat anzeigt, 
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

Erläuterung der Kommen- und Gehenzeiten am Beispiel des 2. Mai 2013:
480 Minuten entsprechen 08:00 Uhr (8 * 60); 1.040 Minuten entsprechen 17:20 Uhr (17 * 60 + 20)

Beispiel
Report                                                        Array zeiten
Mitarbeiter: 12345			Mai 2013                          _________________
Tag	 Kommen  Gehen  Anwesenheit  Bemerkung                    | Tag | Minuten |
===================================================           |_____|_________|
1                   00:00        nicht anwesend               |   2 |     480 |
2    08:00   17:20  09:20                                     |   2 |    1040 |
3    07:50          00:00        eine Buchung fehlt           |   3 |     470 |
4                   00:00        nicht anwesend               |   6 |     480 |
5                   00:00        nicht anwesend               |   6 |     960 |
6    08:00   16:00  08:00                                     |   7 |     990 |
7    16:30          00:00        eine Buchung fehlt           |   8 |     480 |
8    08:00   16:00  08:00                                     |   8 |     960 |
...                                                            ...
30   08:10          00:00        eine Buchung fehlt           |  30 |     990 |
31                  00:00        nicht anwesend               |_____|_________|
===================================================
Summe Anwesenheit:  43:20

Funktionen zur Verfügung:

tageImMonat(monat: Integer, jahr: Integer) : Integer

schreibeKopf(persnr: Integer, jahr: Integer, monat: Integer)

schreibeZeile(tag: Integer, std1: Integer, min1: Integer, 
                            std2: Integer, min2: Integer, anwTag: Integer, bemerkung: String)

schreibeFuss(anwMonat: Integer)

*/

erzeugeListe(persnr: Integer, zeiten: zweidimensionale Tabelle vom Typ Integer, jahr: Integer, monat: Integer) {
	schreibeKopf(persnr, jahr, monat)
	Integer i := 1
	tageProMonat := tageImMonat(monat, jahr)
	tag := 1
	anwMonat := 0

	Integer ersteZeit := zeiten[0][1]
	Integre ersterTag := zeiten[0][0]

	solange tag < tageProMonat
		solange i < laenge vom Array zeiten - 1 and tag < tageProMonat
			Integer zweiteZeit := zeiten[i][1]
			Integer zweiterTag := zeiten[i][0]
		
			wenn tag <> ersterTag dann
				schreibeZeile(tag, 0, 0, 0, 0, 0, "nicht anwesend")
				
			sonst
				wenn ersterTag = zweiterTag und tag = ersterTag dann
					Integer std1 = ersteZeit/60
					Integer std2 := zweiteZeit/60
					Integer min1 := ersteZeit MODULO 60
					Integer min2 := zweiteZeit MODULO 60
					Integer anwTag := ((std2 - std1)*60) + min2 + min1
					anwMonat := anwMonat + anwTag
					schreibeZeile(zweiterTag, std1, min1, std2, min2, anwTag, "anwesend")
					i := i + 1
					// Schritt für Schritt: wenn 2 Zeile gibt, muss man die erste neue Zeile speichern und 
					// den Iterator inkrementieren
					wenn i <> laenge vom Array zeiten - 2 dann
						ersteZeit = zeiten[i][1]
						ersterTag = zeiten[i][0]
						i += 1
				sonst
					Integer std1 = ersteZeit/60
					Integer min1 := ersteZeit MODULO 60
					schreibeZeile(ersterTag, std1, min1, -1, -1, -1, "eine Buchung fehlt")
					i := i + 1
					// lokales reset
					ersteZeit = zweiteZeit
                    ersterTag = zweiterTag
				ende wenn

				wenn i = laenge vom Array zeiten - 2 und zweiterTag <> ersterTag
					Integer std2 := zweiteZeit/60
					Integer min2 := zweiteZeit MODULO 60
					schreibeZeile(zweiterTag, std2, min2, -1, -1, -1, "eine Buchung fehlt")
					ende wenn
			ende wenn
			
			tag := tag + 1
		ende solange
		
		// Nach dem Ablauf des Arrays, gibt es mehrere Tage nicht aus gedruckt
		solange tag <= tageImMonat
			wenn tag = ersterTag dann
				Integer std1 = ersteZeit/60 
				Integer min1 = ersteZeit % 60
				schreibeZeile(ersterTag, std1, min1, -1, -1, -1, "eine Buchung fehlt") 
			sonst
				schreibeZeile(tag, 0, 0, 0, 0, 0, "nicht anwesend")
			tag := tag + 1
			ende wenn
		ende solange
		
	ende solange

	schreibeFuss(anwMonat)

ende der Funktion erzeugeListe

	