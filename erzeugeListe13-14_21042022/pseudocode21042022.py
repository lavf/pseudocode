zeiten = [
    [  2, 480],
    [  2, 1040],
    [  3, 470],
    [  6, 480],
    [  6, 960],
    [  7, 990],
    [  8, 480],
    [  8, 960],
    [ 30, 990]
]

def erzeugeListe(persnr, zeiten, jahr, monat):
    print("Mitarbeiter: " + str(persnr) + "\t\t" + "Mai" + " " + str(jahr))
    print("Tag\tKommen\tGehen\tAnwesenheit\tBemerkung")
    print("======================================================")

    i = 1
    tag = 1
    ersterTag = zeiten[0][0]
    ersteZeit = zeiten[0][1]
    anzahlTage = 0
    anwMonat = 0

    if monat == 1 or monat == 3 or monat == 5 or monat == 7 or monat == 8 or monat == 10 or monat == 12:
        anzahlTage = 31
    elif monat == 2:
        anzahlTage = 28
    else:
        anzahlTage = 30

    while tag < anzahlTage:
        while i < len(zeiten) - 1 and tag < anzahlTage:
            zweiterTag = zeiten[i][0]
            zweiteZeit = zeiten[i][1]

            if tag != ersterTag:
                print(str(tag) + "\t\t\t00:00\t" + "\tnicht anwesend")
            else:
                if ersterTag == zweiterTag and tag == ersterTag:
                    std1 = int(ersteZeit/60)
                    std2 = int(zweiteZeit/60)
                    min1 = int(ersteZeit % 60)
                    min2 = int(zweiteZeit % 60)
                    anwTag = ((std2 - std1)*60) + min2 + min1
                    anwMonat += anwTag
                    stdTag = int(anwTag/60) 
                    minTag = int(anwTag % 60)
                    print(str(zweiterTag) + "\t" + str(std1) + ":" + str(min1) + "\t" + str(std2) + ":" + str(min2) + "\t" + str(stdTag) + ":" + str(minTag) + "\t\t")
                    i += 1
                    if i != len(zeiten) - 2:
                        ersteZeit = zeiten[i][1]
                        ersterTag = zeiten[i][0]
                        i += 1
                else: 
                    std1 = int(ersteZeit/60)                  
                    min1 = int(ersteZeit % 60)
                    print(str(ersterTag) + "\t" + str(std1) + ":" + str(min1) + "\t\t00:00\t\teine Buchung fehlt")
                    i += 1
                    ersteZeit = zweiteZeit
                    ersterTag = zweiterTag
            
                if i == len(zeiten) - 2 and zweiterTag != ersterTag:
                    std2 = int(zweiteZeit/60)
                    min2 = int(zweiteZeit % 60)
                    print(str(zweiterTag) + "\t" + str(std2) + ":" + str(min2) + "\t\t00:00\t\teine Buchung fehlt")
                
            tag += 1

        while tag <= anzahlTage:
            if tag == ersterTag:
                std1 = int(ersteZeit/60)                  
                min1 = int(ersteZeit % 60)
                print(str(ersterTag) + "\t" + str(std1) + ":" + str(min1) + "  \t\t" + "00:00" + "\t\tBuchung fehlt")
            else:
                print(str(tag) + "\t\t\t00:00\t" + "\tnicht anwesend")
            tag += 1

   
    stdMonat = int(anwMonat/60) 
    minMonat = int(anwMonat % 60)
    print("======================================================")
    print("Summe Anwesenheit:\t" +  str(stdMonat) + ":" + str(minMonat))

erzeugeListe(12345, zeiten, 2014, 5)
