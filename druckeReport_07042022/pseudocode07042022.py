
messung = [
    ['2019-04-01', '06:00:00', 1,   76,   80],
    ['2019-04-01', '06:00:15', 2,  197,  200],
    ['2019-04-01', '06:00:15', 0,  3.2, 3.41],
    ['2019-04-02', '06:00:00', 0,   76,   80],
    ['2019-04-02', '06:00:00', 0,  197,  200]
]

def setArray(laenge):
    intArray = []
    i = 0
    while i < laenge:
        intArray.append(0)
        i += 1
    return intArray

def drueckeTag(datum,tagesProtokoll):
    j = 0
    for tp in tagesProtokoll:        
        print("Datum: " + datum + ", MessArt: " + str(j) + ", Anzahl Abweichungen: " + str(tp))
        j += 1

def laenge(array):
    return len(array)

def absolut(wert):
    return abs(wert)

def drueckeReport(messung, messArtAnzahl, maxToleranz):
    i = 0
    abweichung = 0
    abweichungsProzent = 0
    tagesProtokoll = setArray(messArtAnzahl)
    datum = messung[0][0]

    while i <= laenge(messung):
        if i != laenge(messung) and messung[i][0] == datum:
            abweichung = absolut(messung[i][4] - messung[i][3])
            abweichungsProzent = abweichung * 100 / messung[i][4]
            if abweichungsProzent > maxToleranz:
                tagesProtokoll[messung[i][2]] += 1
                   
        else:
            drueckeTag(datum,tagesProtokoll)
            tagesProtokoll = setArray(messArtAnzahl)
            if i != laenge(messung):
                datum = messung[i][0]
                i -= 1 
                
        i += 1 

drueckeReport(messung,3,1)