
kino = [
    [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,1,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

def freieSitze(anzahlSitze):
    i = 0
    ergebnis = 0
    anzahlMatch = 0
    erstesMatch = False
    sitzNummer = 0

    while i < len(kino):
        j = 0 
        while j <= 30 - anzahlSitze:
            z = 0
            while z < anzahlSitze: 
                if kino[i][j+z] == True and erstesMatch == False:
                    anzahlMatch += 1
                    sitzNummer =  (i + 1) * 100 + (j + 1)
                    erstesMatch = True
                elif kino[i][j+z] == True and erstesMatch == True:
                    anzahlMatch += 1                
                elif erstesMatch == True and anzahlMatch == anzahlSitze:
                    ergebnis = sitzNummer
                elif kino[i][j+z] == False:
                    sitzNummer = 0
                    erstesMatch = False
                    anzahlMatch = 0
                z += 1
            j += anzahlSitze      
                
        i += 1
    
    return ergebnis


print(freieSitze(3))