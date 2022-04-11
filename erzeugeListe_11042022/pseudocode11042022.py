
zeiten = [
    [  2,  8, 10],
    [  2, 17, 20],
    [  3,  7, 50],
    [  6,  8, 00],
    [  6, 16, 00],
    [  7, 16, 30],
    [  8,  8, 20],
    [  8, 16, 40],
    [ 30,  8, 10]

]


def erzeugeListe(persnnr, zeiten, jahr, monat):
    i = 1
    tag = 1
    aktuellerTag = zeiten[0][0]
    aktuellerStd = zeiten[0][1]
    aktuellerMin = zeiten[0][2]
    anwMonat = 0
    anzahlTage = 0

    if monat == 1 or monat == 3 or monat == 5 or monat == 7 or monat == 8 or monat == 10 or monat == 12:
        anzahlTage = 31
    elif monat == 2:
        anzahlTage = 28
    else:
        anzahlTage = 30

    print("Mitarbeiter: " + str(persnnr) + "\t\t" + "Oktober" + " " + str(jahr))
    print("Tag\tKommen\tGehen\tAnwesenheit\tBemerkung")
    print("======================================================")

    while tag <= anzahlTage and i < len(zeiten):
        while tag != aktuellerTag:
            if zeiten[i][0] != tag:
                print(str(tag) + "\t\t\t00:00\t" + "\tnicht anwesend")
                tag += 1
        
        if aktuellerTag == zeiten[i][0]:
            anwTag = ((zeiten[i][1]-12) + (12-aktuellerStd))*60 + (zeiten[i][2]-aktuellerMin)
            anwMonat += anwTag
            print(str(aktuellerTag) + "\t" + str(aktuellerStd) + ":" + str(aktuellerMin) + "\t" + str(zeiten[i][1]) + ":" + str(zeiten[i][2]) + "\t" + str(anwTag) + "\t\t")
            i += 1
        else:
            print(str(aktuellerTag) + "\t" + str(aktuellerStd) + ":" + str(aktuellerMin) + "  \t\t" + "00:00" + "\t\tBuchung fehlt")

        if i < len(zeiten) - 1:
            aktuellerTag = zeiten[i][0]
            aktuellerStd = zeiten[i][1]
            aktuellerMin = zeiten[i][2]
        else:
            aktuellerTag = zeiten[len(zeiten) - 1][0]
            aktuellerStd = zeiten[len(zeiten) - 1][1]
            aktuellerMin = zeiten[len(zeiten) - 1][2]
            
        tag += 1
        i += 1

    while tag <= anzahlTage:
        if tag == aktuellerTag:
            print(str(aktuellerTag) + "\t" + str(aktuellerStd) + ":" + str(aktuellerMin) + "  \t\t" + "00:00" + "\t\tBuchung fehlt")
        else:
            print(str(tag) + " \t\t\t00:00\t" + "\tnicht anwesend")
        
        tag += 1
    
    print("======================================================")
    print("Summe Anwesenheit:\t" +  str(anwMonat))

erzeugeListe(12345, zeiten, 2019, 10)