/* """
Folgende Klassen sind bereits vorhanden:
 _____________________________________________________________
|                             Value                           |
| - sensor_id: Integer                                        |
| - value: Double                                             |
| - time: Long                                                |
| ____________________________________________________________|
| + Konstruktor(sensor_id: Integer, value: Double, time: Long)|
| + getId() : Integer                                         |
| + getValue(): Double                                        |
| + getTime(): Long											  |
|_____________________________________________________________|
 ____________________________________________
|                 TempList                   |
|+ setValue(value: Value)                    |
|+ getValue(sensor_id, pos: Integer) : Value |
|+ getSize(sensor_id: Integer) : Integer     |
|____________________________________________|
(Beziehung zwischen Value und TempList ist eine Komposition)

Die Methode onNewValue soll mit folgender Funktionalität implementiert werden:
* Erstellen eines Value-Objektes mit den übergeben Parametern
* Speichern des Value-Objektes mit der Methode setValue des Objektes tempList

/////////////////////////////////////////////////////////////////////////////////

Die Methode ermittelt aus allen in tempList gespeicherten Temperaturwerten die höchste
Anzahl von hintereinander gespeicherten Werten des Sensors ermittelt, welche den
vorgegebenen Mindestwert einhalten.

Beispiel:
Es liegen Temperaturwerte 20, 22, 23, 21, 19, 18, 20, *22, *23, *23, *24, *22, 21 vor.
Die höchste Anzahl von hintereinanderliegenden Werten, welche den Mindestwert 22 einhalten,
ist fünf.

HINWEIS: TempList ist schon vorhanden (tempListObj)

""" */

onNewValue(sensor_id: Integer, value: Double, time: Long) {
	Value valueObj := new Value(sensor_id, value, time)

	tempListObj.setValue(valueObj)
	ende der funktion
}

maxPeriod(sensor_id: Integer, mindestwert: Double) : Integer {
	Integer i, hoechstesPeriod := 0

	solange i < tempListObj.getSize(sensor_id)	
		period := 0
		solange tempListObj.getValue(sensor_id, i) >= mindestwert und i < tempListObj.getSize(sensor_id)
			period := period + 1
			i := i + 1	

		wenn period > hoechstePeriod
			dann
				hoechstesPeriod := period	
		
		i := i + 1
		
	rueckgabe hoechstePeriod

	ende der Funktion
}