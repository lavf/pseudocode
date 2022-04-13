fehler = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]

liste = [
    [434,1,1,1],
    [434,1,1,4],
    [189,3,3,12],
    [201,4,2,8]
]

produkte = [434,433,189,201]


def entnehmenWaren(liste):
    i = 0
    anzahlFehler = 0

    while i < len(liste):
        print("fahreRegalAn " + str(liste[i][1]))  #fahreRegalAnliste()
        regalStart = liste[i][1]
        while i < len(liste) and regalStart == liste[i][1]:
            print("fahrenEbeneAn " + str(liste[i][2]))  #fahrenEbeneAn()
            ebeneStart = liste[i][2]
            while i < len(liste) and regalStart == liste[i][1] and ebeneStart == liste[i][2]:
                print("fahreFachAn " + str(liste[i][3]))
                if liste[i][0] == produkte[i]:
                    print("Die Ware {} wird entnommen ".format(liste[i][0]) + str(liste[i][1]) + "," + str(liste[i][2]) + "," + str(liste[i][3]))
                else:
                    fehlerZeile = [liste[i][0],liste[i][1],liste[i][2],liste[i][3]]
                    fehler[anzahlFehler] = fehlerZeile
                    anzahlFehler += 1
                    print("Die Ware {:0} wird nicht entnommen, weil es andere Ware (Nr.{:1}) in diesem Platz gibt.".format(liste[i][0] ,produkte[i]))
                i += 1

entnehmenWaren(liste)

print(fehler)
