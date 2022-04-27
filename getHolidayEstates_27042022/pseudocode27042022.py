from daten import List, getEstates 

def getHolidayEstates(destination, persons, bedrooms, maxPrice, arrival, duration):
    listObj = List()
    listObj.createList()
    estates = getEstates(destination)
    i = 0

    while i < len(estates):
        if estates[i].getBedroom() >= bedrooms and estates[i].getPersons() >= persons and estates[i].getPrice() <= maxPrice and estates[i].getVacancies(arrival, duration) == True:
            listObj.add(estates[i])		
        i += 1

    if listObj.len() == 0:
        print("Es gibt kein Ferienhaus bei diesen Suchkriterien")
        return []
    else:
        return listObj


print('Suchkriterien: Kopenhagen, 1 Bett, 1 Person, MaxPreis 300.00, ab dem 04.06.22 für 2 Tage')
ergebnis = getHolidayEstates('Kopenhagen', 1, 1, 300.00, '04.06.22', 2)

# Ergebnisse anzeigen
if ergebnis != 0:
    i = 0
    while i < ergebnis.len():
        print(ergebnis[i][0] + ' mit ' + str(ergebnis[i][1]) + ' Bett, für ' + str(ergebnis[i][2]) + ' Person(en), ' + str(ergebnis[i][3]) + ' EUR pro Nacht')
        i += 1

print('\nSuchkriterien: Kopenhagen, 1 Bett, 1 Person, MaxPreis 0.00, ab dem 04.06.22 für 2 Tage')
ergebnis = getHolidayEstates('Kopenhagen', 1, 1, 00.00, '04.06.22', 2)

# Ergebnisse anzeigen
if ergebnis != 0:
    i = 0
    while i < len(ergebnis):  
        print(ergebnis[i][0] + ' mit ' + str(ergebnis[i][1]) + ' Bett, für ' + str(ergebnis[i][2]) + ' Person(en), ' + str(ergebnis[i][3]) + ' EUR pro Nacht')
        i += 1

# ergebnis.len()