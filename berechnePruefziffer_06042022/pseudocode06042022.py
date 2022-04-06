
def pruefeId(idNummer):
    i = 0
    schrittEins = ""
    schrittZwei = 0
    schrittVier = 0
    schrittFuenf = 0
    schrittSechs = 0
    ungeradeQuersumme = 0
    geradeQuersumme = 0
    rest = 0

    while i < (len(idNummer) - 1):
        if i % 2 == 0:
            temp = int(idNummer[i]) * 2
            schrittEins = str(temp)

            if int(schrittEins) > 9:
                schrittZwei = int(schrittEins[0]) + int(schrittEins[1])
            else:
                schrittZwei = int(schrittEins[0])
            ungeradeQuersumme = schrittZwei + ungeradeQuersumme
        else:
            geradeQuersumme = int(idNummer[i]) + geradeQuersumme
        i += 1

    schrittVier = ungeradeQuersumme + geradeQuersumme

    if schrittVier % 10 != 0:
        rest = 10 - (schrittVier % 10)
        schrittFuenf = schrittVier + rest
    else:
        schrittFuenf = schrittVier
    
    schrittSechs = schrittFuenf - schrittVier

    if schrittSechs == int(idNummer[9]):
        print("True")
        return True
    else:
        print("False")
        return False

