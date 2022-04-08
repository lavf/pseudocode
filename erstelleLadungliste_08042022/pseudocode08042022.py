
ladungsliste = [
    [800, 0, 276201],
    [500, 0, 276196],
    [600, 0, 276198],
    [700, 0, 276179],
]

def erstelleLadungliste(ladungliste, nutzlast_kg, maxAnzahlPalette):
    summeProLkw = 0
    i = 0
    paletteAnzahl = 0
    lkwNr = 1

    while i < len(ladungliste):
        if ladungsliste[i][1] == 0:
            if (summeProLkw + ladungsliste[i][0]) <= nutzlast_kg and paletteAnzahl <= maxAnzahlPalette and lkwNr <= 10:
                summeProLkw = ladungsliste[i][0] + summeProLkw
                paletteAnzahl = paletteAnzahl + 1
                ladungsliste[i][1] = lkwNr
            else:
                lkwNr += 1
                summeProLkw = 0
                paletteAnzahl = 0
                i -= 1
        i += 1
    return ladungliste

erstelleLadungliste(ladungsliste, 1100, 2)

print(ladungsliste) 

#[[800, 1, 276201], [500, 2, 276196], [600, 2, 276198], [700, 3, 276179]]