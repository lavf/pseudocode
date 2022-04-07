/*

Array messung
|     | datum      | zeit     | messArt |  istWert | sollWert |
|  0  | 2019-04-01 | 06:00:00 |    1    |    76    |    80    |
|  1  | 2019-04-01 | 06:00:15 |    2    |    197   |    200   |
|  .  | 2019-04-01 | 06:00:15 |    0    |    3,2   |   3,41   |
|     |            |          |         |          |          |
| 301 | 2019-04-02 |          |    0    |    76,5  |    78    |
| 302 | 2019-04-02 |          |    0    |    220   |    200   |
| ... |            |          |         |          |          |
| 426 | 2019-04-03 |          |    2    |    3,6   |    3,4   |
| ... |            |          |         |          |          |

Array tagesProtokoll
| messArt | anzahlFehler |
|    0    |      1       |
|    1    |      0       |
|    2    |      7       |
|   ...   |              |

Hinweis: Die Anzahl der Messarten kann variieren. In diesem Beispiel sind
es drei Messarten, es können aber auch n Messarten sein.

Funktionen zur Verfügung:

setArray(laenge : integer) : arrayTyp
drueckeTag( datum: Datum, tagesProtokoll : arrayTyp integer) : void
laenge(array: arrayTyp X): integer
absolut(wert) : double

Struktur: Messung
  datum:       Datum,
  zeit:        Zeit,
  messArt:     integer,
  istWert:     double,
  sollWert:    double
ENDE STRUKTUR
*/

druckeReport(messung: arrayTyp Messung, messArtAnzahl: integer, maxToleranz: double) : void
	integer i := 0
	double abweichung := 0
	double abweichungProzent := 0
	tagesProtokoll := setArray(messArtAnzahl)
	Datum datum
	datum := messung[0].datum

	solange i <= laenge(messung)
		wenn i <> laenge(messung) und messung[i].datum = datum
			abweichung := absolut(messung[i].sollWert - messung[i].istWert)
			abweichungsProzent := abweichung * 100 / messung[i].sollWert
			wenn abweichungsProzent > maxToleranz
				tagesProtokoll[messung[i].messArt] := tagesProtokoll[messung[i].messArt] + 1
			ende von wenn
			i:= i + 1
		sonst
			drueckeTag(datum,tagesProtokoll)
			tagesProtokoll := setArray(messArtAnzahl)
			wenn i <> laenge(messung)
				datum := messung[i].datum
			ende von wenn
		ende von wenn
		
	ende von solange
ende von funktion druckeReport