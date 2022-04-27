/*



*/

getHolidayEstates(destination : String, persons : Integer,
				  bedrooms : Integer, maxPrice : Double,
				  arrival : String, duration: Integer) : Liste vom Typ List mit Estate-Objekte
beginn getHolidayEstates
	ergebnis := createList()
	Liste vom Typ Estate estates := getEstates(destination)
	Integer i := 0

	solange i < laenge von Liste estates
		wenn estates[i].getBedroom() >= bedrooms und
			 estates[i].getPersons() >= persons und 
			 estates[i].getPrice() <= maxPrice und 
			 estates[i].getVacancies(arrival, duration, estates[i]) = True dann
				ergebnis.add(estates[i])
		ende wenn
		i := i + 1
	ende solange

	wenn ergebnis = 0 dann
		Ausgabe: "Es gibt kein Ferienhaus bei diesen Suchkriterien"
		abbruch
	sonst
		rueckgabe ergebnis
ende von getHolidayEstates