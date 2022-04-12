ZufallszifferErzeugen = [3,4,5,7,6,1,9,7]


def AbrufcodeFinden(ergebnis):
    coden = ["SQ3457619856", "SQ3457619956"]

    if ergebnis in coden:
        return True
    else:
        return False


def AbrufcodeGenerieren():
    while True:
        ergebnis = "SQ"
        i = 0
        summe = 0
        
        while i < 8:
            tempZufallsziffer = ZufallszifferErzeugen[i]
            tempZufallszifferStr = str(tempZufallsziffer)
            summe += tempZufallsziffer
            ergebnis += tempZufallszifferStr
            i += 1
		
        pruefzahl = 98 - summe
        ergebnis = ergebnis + str(pruefzahl)

        if(AbrufcodeFinden(ergebnis) == False):
            break

    return ergebnis

print(AbrufcodeGenerieren())