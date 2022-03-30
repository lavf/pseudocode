"""
Komprimierungalgorithmus

Die Bilddaten sollen mit einer Lauflängenkodierung komprimiert werden. Dabei werden sich direkt wiederholende Zeichen
zusammengefasst, und nur die Anzahl und das entsprechende Zeichen erfasst. EIne Zusammenfassung soll erst bei mehr als 
vier Zeichen erfolgen. Zur Erkennung der Lauflängekodierung wird das ""%""-Zeichen verwendet, das in den unkomprimierten
Bilddaten nicht vorkommt. Die Bilddaten liegen als String-Arrays vor.

Folgende Funktionen stehen zu Verfügung:
laenge(String[]) : Integer
add(String[], String) : String[]
toString(Integer) : String

"""

from daten import laenge, toString, add, unkomprimiert


def erstelleKomprimierung(unkomprimiert):
    komprimiert = []
    i = 0
    anzahl = 0

    while i <= (laenge(unkomprimiert)-1):
        if i < (laenge(unkomprimiert)-1):
            if unkomprimiert[i] == unkomprimiert[i+1]:
                anzahl += 1
            else:
                if anzahl < 4:
                    j = 0
                    while j <= anzahl:
                        j += 1
                        komprimiert = add(komprimiert, unkomprimiert[i])
                    
                    anzahl = 0 
                else:
                    anzahl = anzahl + 1
                    komprimiereString(anzahl, komprimiert, unkomprimiert, i)
                    anzahl = 0
        else:
            if unkomprimiert[i] == unkomprimiert[i-1]:
                if anzahl == 0 and i != 0:
                    komprimiert = add(komprimiert, unkomprimiert[i-1])
                    komprimiert = add(komprimiert, unkomprimiert[i])
                elif anzahl < 4:
                    j = 0
                    while j <= anzahl:
                        j += 1
                        komprimiert = add(komprimiert, unkomprimiert[i])
                    
                    anzahl = 0 
                else:
                    anzahl = anzahl + 1
                    komprimiereString(anzahl, komprimiert, unkomprimiert, i)
                    anzahl = 0
            else:
                komprimiert = add(komprimiert, unkomprimiert[i])
        i += 1

    return  komprimiert


def komprimiereString(anzahl, komprimiert, unkomprimiert, i):
    komprimiert = add(komprimiert, "%")
    komprimiert = add(komprimiert, toString(anzahl))
    komprimiert = add(komprimiert, unkomprimiert[i])
    return komprimiert

komprimiert = [
    [erstelleKomprimierung(unkomprimiert[0])],
    [erstelleKomprimierung(unkomprimiert[1])],
    [erstelleKomprimierung(unkomprimiert[2])],
    [erstelleKomprimierung(unkomprimiert[3])],
    [erstelleKomprimierung(unkomprimiert[4])],
    [erstelleKomprimierung(unkomprimiert[5])],
    [erstelleKomprimierung(unkomprimiert[6])],
    [erstelleKomprimierung(unkomprimiert[7])]
]

print('Unkomprimiertes Array: {}\n'.format(unkomprimiert[0]) + 'Komprimiertes Array: {}'.format(komprimiert[0]))