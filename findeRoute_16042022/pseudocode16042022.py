Routen = [
	['A','B'],
	['A','C','B'],
	['A','D','E','B'],
]

streckeGewicht = [
    ['AB', 100.0],
    ['AC', 30.0],
    ['CB', 60.0],
    ['AD', 30.0],
    ['DE', 25.0],
    ['EB', 15.0]
]

streckeKosten = [
    ['AB', 100.0],
    ['AC', 30.0],
    ['CB', 60.0],
    ['AD', 30.0],
    ['DE', 25.0],
    ['EB', 15.0]
]

def holeStreckeGewicht(A, B):
    strecke = A + B
    i = 0
    x = ''
    ergebnis = 0.0
    while i < len(streckeGewicht):
        x = streckeGewicht[i][0]
        if strecke == x:
            ergebnis = streckeGewicht[i][1]
            break
        i += 1
    return ergebnis    

def holeStreckePreis(A, B):
    strecke = A + B
    i = 0
    x = ''
    ergebnis = 0.0
    while i < len(streckeKosten):
        x = streckeKosten[i][0]
        if strecke == x:
            ergebnis =  streckeKosten[i][1]
            break
        i += 1
    return ergebnis    



def findeRoute(Gewicht):
    i = 0
    summeGewicht = 0.0
    summeFrachtKosten = 0.0
    summeAktFracht = 0.0
    summeAktGewicht = 0.0

    index = 0
    aktIndex = 0
    indexErgebnis = 0

    while i < len(Routen):
        j = 0
        subGewicht = 0.0
        subFracht = 0.0
        while j < len(Routen[i]) - 1:
            subGewicht = holeStreckeGewicht(Routen[i][j], Routen[i][j+1]) + subGewicht
            subFracht = holeStreckePreis(Routen[i][j], Routen[i][j+1]) + subFracht
            j += 1

        if i == 0:
            summeGewicht = subGewicht
            summeFrachtKosten = subFracht
            index = i
        else:
            summeAktGewicht = subGewicht
            summeAktFracht = subFracht
            aktIndex = i

        if i != 0:
            if summeGewicht <= Gewicht and summeAktGewicht <= Gewicht:
                if summeAktFracht > summeFrachtKosten:
                    indexErgebnis = index
                else:
                    indexErgebnis = aktIndex
            elif summeGewicht > Gewicht and summeAktGewicht <= Gewicht:
                indexErgebnis = aktIndex
            elif summeGewicht <= Gewicht and summeAktGewicht > Gewicht:
                indexErgebnis = index

            summeGewicht = summeAktGewicht
            summeFrachtKosten = summeAktFracht
            index = aktIndex
                
        i += 1

    return indexErgebnis


print(findeRoute(90))

