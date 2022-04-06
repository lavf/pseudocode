journal = [
    ['01.04.2021', 100062, 100076, 2],
    ['11.04.2021', 100062, 100076, 3],
    ['10.04.2021', 100062, 500123, 1],
    ['13.04.2021', 201235, 200234, 1],
    ['14.04.2021', 201235, 200234, 1],
    ['07.04.2021', 201235, 200356, 1]
]

def erstelle_Liste(stundensatz):
    anzahlstunden = 0
    produkt = 0
    summe = 0
    gsumme = 0
    nr = 0
    i = 0

    print('Nr\t' + 'MitgliedID\t'+'Name\t'+'Vorname\t\t'+'LeistungID\t'+'Leistung\t'+'AnzahlStunden\t'+'Stundensatz\t'+'Gesamt\t')

    while i < len(journal):
        if i < (len(journal) - 1) and journal[i][1] == journal[i+1][1] and journal[i][2] == journal[i+1][2] and anzahlstunden == 0:
            anzahlstunden = journal[i][3] + journal[i+1][3]
        elif i < (len(journal) - 1) and journal[i][1] == journal[i+1][1] and journal[i][2] == journal[i+1][2] and anzahlstunden != 0:
            anzahlstunden = journal[i+1][3] + anzahlstunden       
        else:
            if i < (len(journal) - 1) and journal[i][1] != journal[i+1][1]:            
                anzahlstunden = journal[i][3]
            elif i == (len(journal) - 1):
                anzahlstunden = journal[i][3]
            nr += 1
            produkt = stundensatz * anzahlstunden
            summe = produkt + summe
            print(str(nr) + '\t' + str(journal[i][1]) + '\t\t' + 'XXXXX' + '\t' + 'XXXXX' + '\t\t' + str(journal[i][2]) + '\t\t' + 'XXXXX' + '\t\t' + str(anzahlstunden) + '\t\t' + str(stundensatz) + '\t\t' + str(produkt))
            anzahlstunden = 0
            produkt = 0

            if i < (len(journal) - 1) and journal[i][1] != journal[i+1][1]:
                gsumme = summe + gsumme
                print('\t\t\t\t\t\t\t\t\t\t\t\tSumme\t\t' +  str(summe))
                nr = 0
                summe = 0
            elif i == (len(journal) - 1):
                gsumme = summe + gsumme
                print('\t\t\t\t\t\t\t\t\t\t\t\tSumme\t\t' +  str(summe))
                nr = 0
                summe = 0

        i += 1

    print('\t\t\t\t\t\t\t\t\t\t\t\tGesammtsumme\t' +  str(gsumme))


erstelle_Liste(6.00)