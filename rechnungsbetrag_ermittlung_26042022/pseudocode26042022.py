kursteilnehmer = [
    [201105, 480.00, 5001, 20, 'Anders, Max', 123],
    [201105, 480.00, 5001, 0, 'Meier, Paul', 124],
    [201105, 480.00, 5001, 0, 'Müller, Anna', 125],
    [488105, 480.00, 5001, 20, 'Anders, Max', 123],
    [488105, 480.00, 5001, 0, 'Müller, Anna', 125],
    [201103, 200.00, 5001, 20, 'Anders, Max', 123],
    [201103, 200.00, 5001, 0, 'Müller, Anna', 125],
    [201103, 200.00, 5001, 0, 'Zuse, Maria', 126],
    [201103, 200.00, 5001, 0, 'Meier, Paul', 124],
    [488109, 480.00, 5001, 20, 'Zuse, Maria', 126],
    [488109, 480.00, 5001, 0, 'Anders, Max', 123],
    [488109, 480.00, 5001, 0, 'Meier, Paul', 124],    
    [488109, 480.00, 5001, 0, 'Müller, Anna', 125],
    [488110, 980.00, 5001, 20, 'Müller, Anna', 125],
    [488110, 480.00, 5001, 0, 'Anders, Max', 123]
]

def rechnungsbetrag_ermittlung(kundennumer):
    anzahl = len(kursteilnehmer)
    i = 0
    anzahlKurs = 0
    rechnungsbetrag = 0.0

    while i < anzahl:
        if kursteilnehmer[i][5] == kundennumer:
            anzahlKurs += 1
            if kursteilnehmer[i][3] != 0:
                rechnungsbetrag += (kursteilnehmer[i][1] - ((kursteilnehmer[i][1] * kursteilnehmer[i][3])/100))
            else:
                rechnungsbetrag += kursteilnehmer[i][1]
        i += 1

    if anzahlKurs >= 5:
        rechnungsbetrag *= 0.95
    else:
        if anzahlKurs >= 3:
            rechnungsbetrag *= 0.97
    
    # decimal 
    return round(rechnungsbetrag, 2)