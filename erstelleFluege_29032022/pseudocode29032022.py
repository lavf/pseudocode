""" 
Die neue Funktion:

* soll aus dem Array Linien-Fluege die Flug-Objekte derjenigen Flüge, die einer bestimmten Strecke nonstop durchgeführt werden und die benötigen Plätze bieten.
* soll die ausgewählten Flug-Objekte in einem neuen eindimensionalen Array Auswahl_Fluege speichern. Die Flug-Objekte sollen nach Preis aufsteigend sortiert sein.
* soll eine Referenz auf das Array Auswahl_Fluege zurückgeben.

Hinweis: Umsetzung der Liste statt des Arrays, um viele Datentypen anzuwenden.
"""

from daten import Flug, Linien_Fluege

# Eingabe des Benutzers
eingabeDatum = "28.08.2022"
eingabePlaetze = 10

def erstelleFluege(datum, plaetze):
    
    Auswahl_Fluege = [0]
    Auswahl_Fluege = [Flug() for j in range(11)]

    flugObj = Flug()
    #flugObj.getFlugDaten(10004)
    #flugObj.getFluegeGemaessDatumUndPlaetze(datum, plaetze)
    #flugObj.printFluegeDaten()
    i = 0


    while i < len(Linien_Fluege):
        #if Linien_Fluege[i][1] == datum and Linien_Fluege[i][5] >= plaetze:            
        for flugObj in Auswahl_Fluege:
            if Linien_Fluege[i][1] == datum and Linien_Fluege[i][5] >= plaetze: 
                flugObj.id = Linien_Fluege[i][0]
                flugObj.flugDatum = Linien_Fluege[i][1]
                flugObj.abflugZeit = Linien_Fluege[i][2]
                flugObj.ankunftZeit = Linien_Fluege[i][3]
                flugObj.preis = Linien_Fluege[i][4]
                flugObj.freiePlaetze = Linien_Fluege[i][5]                                     
            i += 1 
        # break  
        #return Auswahl_Fluege

    return Auswahl_Fluege
    

ergebnis = erstelleFluege(eingabeDatum, eingabePlaetze)

# Debugging
keinenFlug = True

print('Eingabedatum: {:2}, Eingabeplätze: {:3}\n'.format(eingabeDatum, eingabePlaetze))



for flug in ergebnis:
    if flug.id != 0 and ergebnis != 0:
        print(flug.id, ', Preis: {:0}, freie Plätze: {:1}'.format(flug.preis, flug.freiePlaetze))
        keinenFlug = False

if keinenFlug == True:
    print('Es gibt keinen Flug am {}'.format(eingabeDatum) + ' für {} Persone*n'.format(eingabePlaetze))