
def querSumme(zahl):
    tempStr = str(zahl)
    if zahl > 9:
        return int(tempStr[0]) + int(tempStr[1])
    else: 
        return zahl

def rundeAuf(zahl):
    tempStr = str(zahl)
    tempInt = int(tempStr[0]) + 1
    return int(str(tempInt) + "0")

def pruefeKreditkartennummer(kknr):
    i = 0
    schritt2 = 0
    schritt3 = 0
    schritt4 = 0
    pz = 0

    while i < len(kknr) - 1:
        schritt1 = 0
        if i % 2 != 0:
            schritt1 = int(kknr[i]) * 3
            if schritt1 > 9:
                tempSumme = querSumme(schritt1)
                schritt2 += tempSumme
            else:
                schritt2 += schritt1
        else:
            schritt3 += int(kknr[i])
        i += 1

    schritt4 = schritt2 + schritt3
    pz = rundeAuf(schritt4) - schritt4

    return pz == int(kknr[15])


kknr1 = "9342571866601997"

print(pruefeKreditkartennummer(kknr1))  # True